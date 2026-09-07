# 📄 **BITÁCORA — 2026-09-02 — Integración Azure AD + Limpieza del repositorio**

## 📅 Fecha
2026-09-02

## 📘 Proyecto
Portfolio de Ciberseguridad — Módulo 01: Seguridad Azure

## 🎯 Objetivo del día
Integrar Azure Active Directory como proveedor de identidad para la API `EcommerceApi` y realizar una auditoría del repositorio para separar el trabajo profesional del portfolio respecto a los artefactos experimentales del laboratorio PKCE.

---

## 🛠 Trabajo realizado

### 1. Integración de Azure AD en la API local
- Configuración de autenticación **JWT Bearer** en `Program.cs`.
- Activación de `UseAuthentication()` y `UseAuthorization()`.
- Validación de tokens emitidos por Azure AD.

### 2. Ajuste de configuración de identidad
- Añadido `TenantId`, `ClientId`, `Audience` y `Authority` en `appsettings.json`.
- La API acepta tokens válidos emitidos por Azure AD.

### 3. Protección de endpoints
- Decoración de controladores con `[Authorize]`.
- Endpoints protegidos correctamente:
  - `ProductsController.cs`
  - `OrdersController.cs`

### 4. Documentación técnica del flujo Azure AD
Archivos creados:
- `azure-ad-register.md`
- `azure-ad-config.md`
- `AZURE-AD-TESTS.md`
- `azure-ad-tests.md`

### 5. Obtención y validación de tokens JWT
Flujos revisados:
- Client Credentials
- Device Code
- Authorization Code

### 6. Auditoría del repositorio y limpieza del laboratorio PKCE
Hallazgos:
- API PKCE experimental mezclada con el portfolio.
- Scripts, utilidades y archivos no alineados con el estilo profesional.
- Documentación duplicada o fuera de contexto.

Decisión:
- Mover el laboratorio PKCE a un **repositorio independiente**.
- Mantener el portfolio limpio, profesional y modular.

---

## 🔍 Validaciones realizadas

### Compilación y ejecución
```bash
cd 01-seguridad-azure/api-local/EcommerceApi
dotnet build
dotnet run
```

### Endpoint sin token
```bash
curl -i http://localhost/api/products
# 401 Unauthorized
```

### Swagger
```bash
curl http://localhost/swagger/index.html
# Acceso correcto
```

### CORS
- Orígenes permitidos: ✔
- Métodos permitidos: ✔
- Encabezados permitidos: ✔

---

## 📂 Archivos relevantes del día
- `Program.cs`
- `appsettings.json`
- `Controllers/ProductsController.cs`
- `Controllers/OrdersController.cs`
- `azure-ad-register.md`
- `azure-ad-config.md`
- `AZURE-AD-TESTS.md`
- `azure-ad-tests.md`
- `bitacora/2026-09-02-azure-ad-inicial.md`

---

## ⚠️ Problemas encontrados

### Error 501481
Configuración incorrecta del registro de aplicación en Azure AD.

### Error 90013
Audiencia o tenant incorrecto en la solicitud de autorización.

---

## 🛠 Soluciones aplicadas
- Revisión completa del registro de aplicación en Azure AD.
- Corrección de `client_id`, `redirect_uri`, `scope` y flujo Authorization Code con PKCE.
- Validación del token JWT y su audiencia esperada.
- Separación clara entre errores del cliente y errores de autorización.

---

## 🧠 Aprendizajes clave
- Integración real de Azure AD con API local mediante JWT Bearer.
- Importancia de proteger endpoints con `[Authorize]`.
- Validación de flujos OAuth2 y tokens JWT en escenarios reales.
- Mantener el portfolio limpio y profesional separando laboratorios experimentales.
- Documentación técnica clara facilita reproducibilidad y auditoría.

---

## 🔜 Próximos pasos
- Implementar autorización granular por roles y scopes.
- Integrar identidad real de cliente de prueba en Azure AD.
- Ajustar seguridad para entorno de producción.

---

## 🔗 Laboratorio PKCE (repositorio independiente)
[https://github.com/lanuzalorenzo/lab-azuread-oauth2-pkce-api](https://github.com/lanuzalorenzo/lab-azuread-oauth2-pkce-api)

---

## 📎 Recursos útiles
- Azure Portal: [https://portal.azure.com](https://portal.azure.com)
- JWT.io
- Postman
- curl

---

## 🏁 Estado final del día
Bloque completado. Integración Azure AD validada, documentación técnica generada, pruebas realizadas y repositorio limpiado para mantener profesionalidad.
``
