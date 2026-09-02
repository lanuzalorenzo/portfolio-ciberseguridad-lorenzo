# Configuración de Azure AD en la API

## Configuración en Program.cs

### 1. Agregar Servicios de Autenticación

Añade el siguiente código en `Program.cs` después de crear el builder:

```csharp
var builder = WebApplicationBuilder.CreateBuilder(args);

// Obtener configuración de Azure AD desde appsettings.json
var azureAdConfig = builder.Configuration.GetSection("AzureAd");
var tenantId = azureAdConfig["TenantId"];
var clientId = azureAdConfig["ClientId"];
var audience = azureAdConfig["Audience"];

// 1. Agregar autenticación JWT Bearer
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(options =>
    {
        // Authority es la URL base de Azure AD donde está el tenant
        options.Authority = $"https://login.microsoftonline.com/{tenantId}/v2.0";
        
        // Audience es el identificador de tu API (Application ID URI)
        options.Audience = audience;
        
        // Validaciones de seguridad
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = $"https://login.microsoftonline.com/{tenantId}/v2.0",
            
            ValidateAudience = true,
            ValidAudience = audience,
            
            ValidateLifetime = true,
            ValidateIssuerSigningKey = true,
            
            // Permitir un pequeño margen de tiempo para reloj desincronizado
            ClockSkew = TimeSpan.FromSeconds(5)
        };
        
        // Opcional: configurar eventos para logging
        options.Events = new JwtBearerEvents
        {
            OnAuthenticationFailed = context =>
            {
                Console.WriteLine($"Authentication failed: {context.Exception.Message}");
                return Task.CompletedTask;
            },
            OnTokenValidated = context =>
            {
                Console.WriteLine("Token validated successfully");
                return Task.CompletedTask;
            }
        };
    });

// 2. Agregar autorización con políticas
builder.Services.AddAuthorization(options =>
{
    // Política por defecto: requiere autenticación
    options.DefaultPolicy = new AuthorizationPolicyBuilder()
        .RequireAuthenticatedUser()
        .Build();
    
    // Política para lectura de órdenes
    options.AddPolicy("OrderRead", policy =>
        policy.RequireClaim("scp", "order.read"));
    
    // Política para escritura de órdenes
    options.AddPolicy("OrderWrite", policy =>
        policy.RequireClaim("scp", "order.write"));
    
    // Política para administrador
    options.AddPolicy("Admin", policy =>
        policy.RequireClaim("roles", "Admin"));
});

// 3. Agregar controladores
builder.Services.AddControllers();

// 4. Agregar Swagger (con configuración de JWT)
builder.Services.AddSwaggerGen(options =>
{
    options.AddSecurityDefinition("Bearer", new OpenApiSecurityScheme
    {
        Type = SecuritySchemeType.Http,
        Scheme = "Bearer",
        BearerFormat = "JWT",
        Description = "JWT Authorization header using the Bearer scheme",
        Name = "Authorization"
    });
    
    options.AddSecurityRequirement(new OpenApiSecurityRequirement
    {
        {
            new OpenApiSecurityScheme
            {
                Reference = new OpenApiReference
                {
                    Type = ReferenceType.SecurityScheme,
                    Id = "Bearer"
                }
            },
            new string[] { }
        }
    });
});

var app = builder.Build();

// Usar Swagger en development
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

// 5. Ordenar los middlewares correctamente
app.UseHttpsRedirection();

// ⚠️ IMPORTANTE: El orden es CRÍTICO
// 1. Authentication debe ir antes de Authorization
app.UseAuthentication();
app.UseAuthorization();

app.MapControllers();

app.Run();
```

## Configuración en appsettings.json

Agrega la sección de Azure AD en tu `appsettings.json`:

```json
{
  "AzureAd": {
    "TenantId": "00000000-0000-0000-0000-000000000000",
    "ClientId": "11111111-1111-1111-1111-111111111111",
    "Audience": "api://ecommerce-api"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    }
  },
  "AllowedHosts": "*"
}
```

**Reemplazar:**
- `TenantId` con tu Directory (tenant) ID de Azure AD
- `ClientId` con tu Application (client) ID
- `Audience` con tu Application ID URI

### Configuración por Entorno

Para desarrollo, puedes usar `appsettings.Development.json`:

```json
{
  "AzureAd": {
    "TenantId": "dev-tenant-id",
    "ClientId": "dev-client-id",
    "Audience": "api://ecommerce-api-dev"
  }
}
```

## Configurar Variable de Entorno (Alternativa a appsettings.json)

Si prefieres usar variables de entorno (más seguro para producción):

```bash
export AzureAd__TenantId="00000000-0000-0000-0000-000000000000"
export AzureAd__ClientId="11111111-1111-1111-1111-111111111111"
export AzureAd__Audience="api://ecommerce-api"
```

## Autorizar Endpoints

### Opción 1: Usar [Authorize] Attribute

```csharp
using Microsoft.AspNetCore.Authorization;

[ApiController]
[Route("api/[controller]")]
public class OrdersController : ControllerBase
{
    // Requiere autenticación general
    [HttpGet]
    [Authorize]
    public IActionResult GetOrders()
    {
        return Ok("All orders");
    }

    // Requiere específicamente el scope "order.read"
    [HttpGet("{id}")]
    [Authorize(Policy = "OrderRead")]
    public IActionResult GetOrder(int id)
    {
        return Ok($"Order {id}");
    }

    // Requiere específicamente el scope "order.write"
    [HttpPost]
    [Authorize(Policy = "OrderWrite")]
    public IActionResult CreateOrder([FromBody] Order order)
    {
        return Created("", order);
    }

    // Requiere rol de Admin
    [HttpDelete("{id}")]
    [Authorize(Policy = "Admin")]
    public IActionResult DeleteOrder(int id)
    {
        return NoContent();
    }

    // Endpoint público (sin autenticación)
    [AllowAnonymous]
    [HttpGet("public/info")]
    public IActionResult PublicInfo()
    {
        return Ok("This is public");
    }
}
```

### Opción 2: Verificar Autenticación en el Código

```csharp
[HttpGet("current-user")]
[Authorize]
public IActionResult GetCurrentUser()
{
    var userId = User.FindFirst(ClaimTypes.NameIdentifier)?.Value;
    var email = User.FindFirst(ClaimTypes.Email)?.Value;
    var scopes = User.FindFirst("scp")?.Value;
    
    return Ok(new
    {
        userId = userId,
        email = email,
        scopes = scopes
    });
}
```

### Opción 3: Autorización Global

Si quieres que todos los endpoints requieran autenticación por defecto:

```csharp
builder.Services.AddControllers(options =>
{
    var policy = new AuthorizationPolicyBuilder()
        .RequireAuthenticatedUser()
        .Build();
    
    options.Filters.Add(new AuthorizeFilter(policy));
});
```

Luego usa `[AllowAnonymous]` solo en endpoints públicos.

## Middleware de Autenticación y Autorización

El orden de los middlewares en `Program.cs` es crítico:

```csharp
// ✅ CORRECTO
app.UseRouting();
app.UseAuthentication();  // PRIMERO: Autentica al usuario
app.UseAuthorization();   // SEGUNDO: Autoriza basado en políticas
app.MapControllers();
app.Run();
```

```csharp
// ❌ INCORRECTO - No funcionará
app.UseAuthorization();   // PRIMERO
app.UseAuthentication();  // SEGUNDO - Se ejecuta después, muy tarde
app.MapControllers();
```

## Validación de Tokens Explicada

Azure AD genera tokens JWT que contienen:

1. **Header (Encabezado)**: Algoritmo y tipo
2. **Payload (Cuerpo)**: Claims (información del usuario, scopes, etc.)
3. **Signature (Firma)**: Validación criptográfica

Ejemplo de payload decodificado:

```json
{
  "iss": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/v2.0",
  "aud": "api://ecommerce-api",
  "exp": 1234567890,
  "iat": 1234567800,
  "nbf": 1234567800,
  "scp": "order.read order.write",
  "sub": "user-object-id",
  "email": "user@example.com"
}
```

El middleware JWT Bearer valida automáticamente:
- ✅ Firma del token (usando claves públicas de Azure AD)
- ✅ Issuer es correcto (Azure AD de tu tenant)
- ✅ Audience es correcta (tu Application ID URI)
- ✅ Token no ha expirado (exp claim)
- ✅ Token es válido ahora (nbf y iat claims)

## Ejemplo Completo: Endpoint Protegido

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductsController : ControllerBase
{
    [HttpGet]
    [AllowAnonymous]
    public IActionResult GetAllProducts()
    {
        return Ok(new[] { "Product 1", "Product 2" });
    }

    [HttpGet("{id}")]
    [Authorize(Policy = "OrderRead")]
    public IActionResult GetProductDetails(int id)
    {
        return Ok($"Product {id} details (requires order.read scope)");
    }

    [HttpPost]
    [Authorize(Policy = "OrderWrite")]
    public IActionResult CreateProduct([FromBody] string productName)
    {
        return Created("", new { id = 1, name = productName });
    }

    [HttpDelete("{id}")]
    [Authorize(Policy = "Admin")]
    public IActionResult DeleteProduct(int id)
    {
        return NoContent();
    }
}
```

## Troubleshooting Común

| Problema | Causa | Solución |
|----------|-------|----------|
| Todos los requests fallan con 401 | Middleware en orden incorrecto | Asegurar `UseAuthentication()` antes de `UseAuthorization()` |
| Token válido pero sigue rechazándose | Audience incorrecto en config | Verificar `Audience` en appsettings.json coincide con Application ID URI |
| Swagger funciona sin token | Falta configuración de seguridad | Agregar `AddSecurityDefinition` y `AddSecurityRequirement` |
| Claims no aparecen en el token | Scopes no asignados al cliente | Agregar API Permission desde aplicación cliente |

