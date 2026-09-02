# Bitácora - Fase 2: Integración Azure AD - 02/09/2026

## 📋 Objetivo del Bloque

Integrar **Azure Active Directory (Azure AD)** como proveedor de identidad y autenticación para la API EcommerceApi, implementando:

- Autenticación JWT Bearer con tokens de Azure AD
- Autorización basada en scopes y roles
- Configuración segura de credenciales
- Validación de tokens
- Testing y debugging completo

---

## 🎯 Acciones Realizadas Hoy (02/09/2026)

### 1. Trabajo en Azure Portal ✅
- Creación de la App Registration **EcommerceApi**
- Tipo: Single-tenant
- Ubicación: Microsoft Entra ID → App registrations

**Valores Obtenidos:**
- **Tenant ID:** `7133f9a8-4c6c-47a3-b9a7-55bad5090288`
- **Client ID:** `d6800b3e-a409-4129-ba4d-7d56bd55f1a8`
- **Application ID URI:** `api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8`
- **Scope:** `access_as_user`

### 2. Configuración JWT Bearer en Program.cs ✅
Implementado:
```csharp
builder.Services.AddAuthentication("Bearer")
    .AddJwtBearer("Bearer", options =>
    {
        options.Authority = "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0";
        options.TokenValidationParameters = new TokenValidationParameters
        {
            ValidateIssuer = true,
            ValidIssuer = "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0",
            ValidateAudience = true,
            ValidAudience = "api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8",
            ValidateLifetime = true
        };
    });
```

Middleware configurado:
- `app.UseAuthentication();`
- `app.UseAuthorization();`

### 3. Configuración en appsettings.json ✅
```json
"AzureAd": {
  "TenantId": "7133f9a8-4c6c-47a3-b9a7-55bad5090288",
  "ClientId": "d6800b3e-a409-4129-ba4d-7d56bd55f1a8",
  "Audience": "api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8",
  "Authority": "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0"
}
```

### 4. Protección de Endpoints ✅
- **ProductsController.cs**: Agregado `[Authorize]`
- **OrdersController.cs**: Agregado `[Authorize]`
- Ambos controllers ahora requieren JWT válido

### 5. Documentación Completa ✅
- **AZURE-AD-TESTS.md**: Guía de testing con curl y Swagger
- **azure-ad-register.md**: Registro en Azure AD (creado el 01/09)
- **azure-ad-config.md**: Configuración técnica (creado el 01/09)
- Incluye: ejemplos de curl, errores comunes, script automatizado

## 📋 Próximos Pasos (Fase 2)

1. **Obtener Token Real:** Ejecutar comando curl para obtener JWT desde Azure AD
2. **Testing Swagger:** Autorizar en Swagger UI con token JWT
3. **Testing curl:** Probar endpoints protegidos con Authorization Bearer
4. **Validación:** Verificar que endpoints sin token devuelven 401
5. **Documentación Final:** Crear bitácora final del bloque Azure AD

---

## 📁 Estructura Actual del Proyecto

```
01-seguridad-azure/
├── api-local/
│   └── EcommerceApi/
│       ├── Controllers/
│       │   ├── OrdersController.cs
│       │   └── ProductsController.cs
│       ├── Models/
│       │   ├── Order.cs
│       │   └── Product.cs
│       ├── Program.cs (pendiente: configuración Azure AD)
│       ├── appsettings.json (pendiente: configuración Azure AD)
│       ├── appsettings.Development.json
│       ├── EcommerceApi.csproj
│       ├── EcommerceApi.http
│       ├── azure-ad-notes.md (old)
│       ├── azure-ad-register.md (NEW)
│       ├── azure-ad-config.md (NEW)
│       ├── azure-ad-tests.md (NEW)
│       ├── README.md
│       ├── tests.md
│       ├── bin/
│       ├── obj/
│       └── Properties/
└── bitacora/
    ├── 2026-09-01-api-local-inicial.md
    └── 2026-09-02-azure-ad-inicial.md (NEW)
```

---

## ✅ Preparación Realizada (01/09/2026)

- [x] Creación de la API base con 2 controllers (Orders, Products)
- [x] Modelos Order y Product creados
- [x] Configuración básica de launchSettings.json
- [x] Documentación inicial de Azure AD
- [x] Documentación de pruebas (tests.md)

---

## 🔐 Checklist de la Fase Azure AD

### 1️⃣ Documentación ✅ (COMPLETADO HOY)

- [x] **azure-ad-register.md**: Guía para registrar API en Azure AD
  - Qué es Azure AD y App Registration
  - Pasos para registrar la API
  - Obtener Tenant ID, Client ID, Application ID URI
  - Crear Scopes (API Permissions)
  - Asignar permisos a aplicaciones cliente
  - Notas de seguridad y mejores prácticas

- [x] **azure-ad-config.md**: Configuración técnica en .NET
  - Configuración en Program.cs (AddAuthentication, AddAuthorization)
  - appsettings.json con valores de Azure AD
  - Configuración por entorno (Development/Production)
  - Autorizar endpoints con [Authorize] attribute
  - Middleware y orden correcto
  - Validación de tokens explicada
  - Ejemplo completo de endpoint protegido
  - Troubleshooting

- [x] **azure-ad-tests.md**: Pruebas y debugging
  - Obtener token JWT desde Azure AD
  - Pruebas con curl
  - Pruebas en Swagger
  - Errores comunes y soluciones
  - Script automatizado de testing
  - Checklist pre-producción

### 2️⃣ Configuración en Azure AD (PRÓXIMO)

- [ ] Registrar EcommerceApi en Azure Portal
  - [ ] Obtener Tenant ID
  - [ ] Obtener Client ID (Application ID)
  - [ ] Crear Application ID URI
  - [ ] Crear Scopes: `order.read`, `order.write`, `admin`
  
- [ ] Registrar aplicación cliente de testing (opcional)
  - [ ] Crear Client Secret
  - [ ] Asignar API Permissions
  - [ ] Grant admin consent

### 3️⃣ Implementación en Código (PRÓXIMO)

- [ ] Actualizar `Program.cs`:
  - [ ] AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
  - [ ] ConfigureJwtBearerOptions
  - [ ] AddAuthorization con políticas de scopes
  - [ ] Agregar middleware UseAuthentication() y UseAuthorization()
  - [ ] Configurar Swagger con Bearer JWT

- [ ] Actualizar `appsettings.json`:
  - [ ] Agregar sección AzureAd
  - [ ] Configurar TenantId, ClientId, Audience

- [ ] Actualizar `appsettings.Development.json`:
  - [ ] Valores específicos para desarrollo

- [ ] Actualizar Controllers:
  - [ ] Agregar [Authorize] en endpoints protegidos
  - [ ] Agregar [AllowAnonymous] en endpoints públicos
  - [ ] Crear endpoint de testing de claims

### 4️⃣ Testing Manual (PRÓXIMO)

- [ ] Obtener token JWT desde Azure AD
- [ ] Pruebas con curl:
  - [ ] Endpoint público (sin token)
  - [ ] Endpoint protegido (con token)
  - [ ] Endpoint protegido (sin token) - debe fallar
  - [ ] Token inválido - debe fallar
  - [ ] Verificar claims del usuario
  
- [ ] Pruebas en Swagger:
  - [ ] Authorize con token
  - [ ] Ejecutar requests protegidos

- [ ] Ejecutar script de testing automatizado

### 5️⃣ Handling de Errores (PRÓXIMO)

- [ ] Validación de tokens fallidos
- [ ] Manejo de scopes insuficientes
- [ ] Errores de configuración (Tenant, Client ID)
- [ ] Logging de intentos fallidos
- [ ] Respuestas HTTP adecuadas (401, 403)

### 6️⃣ Seguridad (PRÓXIMO)

- [ ] Almacenamiento seguro de credenciales (no hardcodear)
- [ ] HTTPS obligatorio
- [ ] Validación de firma de token
- [ ] Clock skew configurado
- [ ] Monitoreo de logs de autenticación

---

## 📊 Pasos Siguientes

### Día 2 (03/09/2026): Implementación

1. Registrar API en Azure Portal
2. Crear aplicación cliente para testing
3. Actualizar Program.cs con autenticación JWT
4. Configurar appsettings.json
5. Proteger endpoints con [Authorize]

### Día 3 (04/09/2026): Testing

1. Obtener token desde Azure AD
2. Realizar pruebas con curl
3. Pruebas en Swagger
4. Verificar scopes y roles
5. Documentar resultados

### Día 4 (05/09/2026): Refinamiento

1. Manejo de errores robusto
2. Logging detallado
3. Validaciones adicionales
4. Performance testing

### Día 5 (06/09/2026): Auditoría

1. Revisión de seguridad
2. Monitoreo en Azure AD
3. Testing de renovación de tokens
4. Plan de incident response

---

## 📝 Referencias y Documentos

### Documentación Interna
- [azure-ad-register.md](./api-local/EcommerceApi/azure-ad-register.md) - Registro en Azure AD
- [azure-ad-config.md](./api-local/EcommerceApi/azure-ad-config.md) - Configuración técnica
- [azure-ad-tests.md](./api-local/EcommerceApi/azure-ad-tests.md) - Pruebas y debugging
- [tests.md](./api-local/EcommerceApi/tests.md) - Tests de la API

### Enlaces Útiles
- [Azure AD Documentation](https://docs.microsoft.com/en-us/azure/active-directory/)
- [JWT.io - Decodificar tokens](https://jwt.io/)
- [.NET JWT Bearer Documentation](https://docs.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.jwtbearer)

---

## 📌 Notas Importantes

### Configuración Segura
- **NUNCA** guardar Client Secret en código o git
- Usar variables de entorno o Key Vault
- Rotación de secrets cada 6-12 meses
- Usar Managed Identity cuando sea posible en Azure

### Orden de Middlewares
```csharp
// ✅ CORRECTO
app.UseAuthentication();
app.UseAuthorization();

// ❌ INCORRECTO
app.UseAuthorization();
app.UseAuthentication();  // Demasiado tarde
```

### Validación de Tokens
- Verificar firma del token
- Validar issuer (debe ser Azure AD)
- Validar audience (debe ser tu Application ID URI)
- Verificar expiración
- Clock skew de 5 segundos

### Testing sin Producción
- Usar tenant de desarrollo separado
- Client Secret en variables de entorno (`.env` local)
- No compartir tokens en repositorios
- Usar Swagger con cuidado en production

---

## 🎓 Lecciones Aprendidas (Se actualizarán)

- (Por completar tras implementación)

---

## ✉️ Contactos y Recursos

### Azure Portal
- URL: https://portal.azure.com
- Sección: Azure Active Directory > App registrations

### Herramientas Útiles
- **JWT.io**: Decodificar y debuggear tokens
- **Postman**: Testing de APIs con JWT
- **curl**: Línea de comandos para requests HTTP

---

**Última actualización:** 02/09/2026
**Estado:** Documentación completada - Iniciando Día 2 (Implementación)

