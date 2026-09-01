# Azure AD Integration - Notas de Preparación

Este documento explica los conceptos clave de **Azure Active Directory (Azure AD)** y cómo se integrará con la EcommerceApi.

---

## Conceptos Fundamentales

### 1. ¿Qué es Azure Active Directory (Azure AD)?

**Azure AD** (ahora conocido como **Microsoft Entra ID**) es un servicio de identidad en la nube que proporciona:

- **Autenticación centralizada**: Gestión de identidades y accesos
- **Autorización basada en roles**: Control de qué pueden hacer los usuarios
- **Federated Identity**: Integración con otros proveedores de identidad
- **Multi-factor Authentication (MFA)**: Seguridad adicional

Es la solución empresarial estándar de Microsoft para gestionar identidades.

---

### 2. ¿Qué es una App Registration?

Una **App Registration** es un objeto en Azure AD que representa tu aplicación (.NET API).

**Propósito:**
- Registrar la aplicación en Azure AD
- Permitir que Azure AD reconozca y valide la aplicación
- Establecer credenciales de seguridad (Client ID, Client Secret)

**Pasos para crear:**
1. Ir a Azure Portal (https://portal.azure.com)
2. Buscar "App registrations"
3. Hacer clic en "New registration"
4. Rellenar nombre: "EcommerceApi"
5. Configurar los "Redirect URIs" (para APIs: https://localhost:5001)

---

### 3. ¿Qué es un Client ID?

El **Client ID** es un identificador único asignado a tu aplicación por Azure AD.

**Características:**
- Es público (no es secreto)
- Formato: GUID (ej: `550e8400-e29b-41d4-a716-446655440000`)
- Se usa en solicitudes de autenticación
- Se envía en las peticiones HTTP para identificar la aplicación

**Ejemplo:**
```
Client ID: 550e8400-e29b-41d4-a716-446655440000
```

---

### 4. ¿Qué es un Scope?

Un **Scope** define permisos específicos que la aplicación puede solicitar.

**Ejemplos en nuestra API:**
```
api://550e8400-e29b-41d4-a716-446655440000/.default
api://550e8400-e29b-41d4-a716-446655440000/access_as_user
```

**Propósito:**
- Especificar qué recursos puede acceder la aplicación
- Implementar el principio de "least privilege" (menor privilegio)
- Controlar permisos granulares

**En Program.cs, se configurarían así:**
```csharp
services.AddMicrosoftIdentityWebApiAuthentication(Configuration);
```

---

### 5. ¿Qué es un JWT (JSON Web Token)?

Un **JWT** es un estándar abierto para transmitir información de forma segura.

**Estructura:** `header.payload.signature`

**Ejemplo decodificado:**
```json
{
  "header": {
    "alg": "RS256",
    "typ": "JWT"
  },
  "payload": {
    "aud": "550e8400-e29b-41d4-a716-446655440000",
    "iss": "https://login.microsoftonline.com/tenant-id/v2.0",
    "iat": 1234567890,
    "exp": 1234571490,
    "preferred_username": "usuario@empresa.com",
    "roles": ["Admin", "User"]
  },
  "signature": "HMAC_SHA256(...)"
}
```

**Información que contiene:**
- Identidad del usuario: `preferred_username`, `oid` (Object ID)
- Roles y permisos: `roles`, `groups`
- Fecha de expiración: `exp`
- Audiencia (para qué app es): `aud`

---

## Cómo se Conectará la API a Azure AD

### Flujo de Autenticación (OAuth 2.0)

```
1. Cliente (Postman/Aplicación) solicita acceso
   └─> Envía credenciales (usuario/contraseña)

2. Azure AD valida las credenciales
   └─> Genera un JWT token

3. Cliente recibe el JWT token
   └─> Lo almacena en memoria

4. Cliente envía solicitud a la API con el token
   └─> Header: "Authorization: Bearer {JWT_TOKEN}"

5. API valida el token con Azure AD
   └─> Verifica firma digital
   └─> Comprueba fecha de expiración
   └─> Valida roles y permisos

6. Si es válido, la API procesa la solicitud
   └─> Si no es válido, devuelve 401 Unauthorized
```

---

## Cambios en Program.cs

### Configuración Actual (Sin Azure AD)
```csharp
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

### Configuración Futura (Con Azure AD)
Se añadirán estas líneas en Program.cs:

```csharp
using Microsoft.Identity.Web;

var builder = WebApplication.CreateBuilder(args);

// Autenticación con Azure AD
builder.Services.AddMicrosoftIdentityWebApiAuthentication(
    builder.Configuration.GetSection("AzureAd"));

builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();
builder.Services.AddAuthorization();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthentication();  // NUEVO: Validar tokens
app.UseAuthorization();   // NUEVO: Autorizar usuarios
app.MapControllers();

app.Run();
```

**Cambios principales:**
- Agregar `AddMicrosoftIdentityWebApiAuthentication()`
- Agregar middleware `UseAuthentication()`
- Leer configuración de Azure AD desde `appsettings.json`

---

## Middleware para Validar Tokens

### ¿Qué es un Middleware?

Un middleware es un componente que se ejecuta en cada solicitud HTTP, como un filtro.

### Middleware a Añadir

La librería `Microsoft.Identity.Web` proporciona middleware automático que:

1. **Extrae el JWT** del header `Authorization: Bearer {token}`
2. **Valida la firma** usando la clave pública de Azure AD
3. **Verifica la expiración** del token
4. **Valida la audiencia** (que el token es para nuestra API)
5. **Extrae información del usuario** (roles, claims)

### Decoradores en Controladores

Después de implementar Azure AD, los controladores lucirán así:

```csharp
[ApiController]
[Route("api/[controller]")]
[Authorize]  // NUEVO: Requiere autenticación
public class ProductsController : ControllerBase
{
    [HttpGet]
    [Authorize(Roles = "Admin,User")]  // NUEVO: Solo roles específicos
    public IActionResult GetAllProducts()
    {
        // ...
    }

    [HttpPost]
    [Authorize(Roles = "Admin")]  // NUEVO: Solo Admins
    public IActionResult CreateProduct([FromBody] Product product)
    {
        // ...
    }
}
```

---

## Configuración en appsettings.json

Se añadirá una sección de Azure AD:

```json
{
  "AzureAd": {
    "Instance": "https://login.microsoftonline.com/",
    "TenantId": "YOUR_TENANT_ID",
    "ClientId": "YOUR_CLIENT_ID",
    "Audience": "api://YOUR_CLIENT_ID"
  },
  "Logging": {
    "LogLevel": {
      "Default": "Information"
    }
  },
  "AllowedHosts": "*"
}
```

---

## Pasos para Implementar

### Fase 1: Preparación (Actual)
- ✅ Estructura base del proyecto
- ✅ Modelos y controladores
- ✅ Documentación

### Fase 2: Configuración Azure AD
- [ ] Crear App Registration en Azure Portal
- [ ] Obtener Client ID y Tenant ID
- [ ] Configurar appsettings.json
- [ ] Instalar NuGet: `Microsoft.Identity.Web`

### Fase 3: Implementación de Autenticación
- [ ] Modificar Program.cs con AddMicrosoftIdentityWebApiAuthentication()
- [ ] Agregar middleware UseAuthentication()
- [ ] Decorar controladores con [Authorize]

### Fase 4: Testing
- [ ] Obtener token de Azure AD
- [ ] Probar endpoints con JWT token
- [ ] Validar roles y permisos

### Fase 5: Seguridad Avanzada
- [ ] Implementar rate limiting
- [ ] Agregar logging de seguridad
- [ ] Configurar CORS para aplicaciones autorizadas
- [ ] Implementar refresh tokens

---

## Recursos Útiles

- **Microsoft Identity Web**: https://github.com/AzureAD/microsoft-identity-web
- **Azure AD Documentación**: https://learn.microsoft.com/en-us/azure/active-directory/
- **JWT.io**: https://jwt.io (decodificar tokens)
- **OAuth 2.0**: https://oauth.net/2/

---

## Seguridad: Checklist

- [ ] Usar HTTPS (obligatorio en producción)
- [ ] Validar siempre tokens en cada solicitud
- [ ] Implementar MFA en Azure AD
- [ ] Usar roles para autorización granular
- [ ] Registrar intentos fallidos de autenticación
- [ ] Implementar rate limiting por usuario
- [ ] Mantener secretos en Azure Key Vault (no en código)
- [ ] Renovar tokens periódicamente

---

**Próximo paso**: Revisar este documento y comenzar con la Fase 2 en el siguiente sprint.
