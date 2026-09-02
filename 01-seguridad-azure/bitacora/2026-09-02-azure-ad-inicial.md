# Bitácora - Fase 2: Integración Azure AD y limpieza del repositorio - 02/09/2026

**Fecha**: 2026-09-02  
**Proyecto**: Portfolio Ciberseguridad - Lorenzo  
**Bloque**: 01-seguridad-azure / Azure AD + Portfolio Cleanup  
**Estado**: ✅ COMPLETADO

---

## Objetivo del Bloque

Integrar **Azure Active Directory (Azure AD)** como proveedor de identidad para la API EcommerceApi y, además, revisar la estructura del repositorio para separar claramente el trabajo profesional del portfolio de pruebas experimentales. Durante esta jornada se desarrolló la autenticación JWT Bearer, se validaron flujos de token y se decidió limpiar los artefactos del laboratorio PKCE para mantener la presentación del repositorio profesional.

---

## Acciones Realizadas

### 1. Integración de Azure AD en la API local
- **Acción**: Configurar autenticación JWT Bearer en la API EcommerceApi.
- **Archivo principal**: `Program.cs`
- **Resultado**: Validación de token con Azure AD, middleware `UseAuthentication()` y `UseAuthorization()` configurados.
- **Estado**: ✅ Completado

### 2. Ajuste de configuración de identidad
- **Acción**: Añadir configuración Azure AD a `appsettings.json`.
- **Valores clave**:
  - TenantId
  - ClientId
  - Audience
  - Authority
- **Resultado**: La API queda preparada para aceptar tokens emitidos por Azure AD.
- **Estado**: ✅ Completado

### 3. Protección de endpoints
- **Acción**: Decorar controladores con `[Authorize]`.
- **Archivos afectados**:
  - `Controllers/ProductsController.cs`
  - `Controllers/OrdersController.cs`
- **Resultado**: Los endpoints protegidos requieren token válido antes de poder responder.
- **Estado**: ✅ Completado

### 4. Documentación técnica del flujo Azure AD
- **Acción**: Generar documentación de registro, configuración y pruebas.
- **Archivos creados**:
  - `azure-ad-register.md`
  - `azure-ad-config.md`
  - `AZURE-AD-TESTS.md`
  - `azure-ad-tests.md`
- **Resultado**: Se documentaron configuración, permisos, uso de curl, pruebas con Swagger y resolución de errores.
- **Estado**: ✅ Completado

### 5. Obtención y validación de tokens JWT
- **Acción**: Estudiar y documentar flujos de autenticación con Azure AD.
- **Flujos revisados**:
  - Client Credentials Flow
  - Device Code Flow
  - Authorization Code Flow
- **Objetivo**: Obtener tokens JWT para autenticar llamadas a la API local y comprobar el comportamiento real con credenciales autenticas.
- **Estado**: ✅ Completado

### 6. Auditoría del repositorio y limpieza del laboratorio PKCE
- **Acción**: Revisar el repositorio completo para detectar artefactos experimentales no relacionados con el portfolio.
- **Hallazgos**:
  - API local experimental de PKCE
  - scripts y utilidades no documentados en el README del portfolio
  - archivos `.js`, `.sh`, `.env` y `package.json` ajenos al proyecto principal
  - documentación del laboratorio con formato no alineado al portfolio
- **Decisión**: Mover esos artefactos fuera del repositorio del portfolio para mantener una estructura profesional y enfocada en proyectos reales.
- **Estado**: ✅ Completado

---

## Configuración y validación realizadas

### Compilación y ejecución

```bash
cd 01-seguridad-azure/api-local/EcommerceApi
dotnet build
# Resultado: ✅ Compilación exitosa
```

```bash
dotnet run
# API ejecutándose en: http://localhost:5177
```

### Verificación funcional

**Endpoint sin token**
```bash
curl -i http://localhost:5177/api/products
# Resultado: ✅ 401 Unauthorized
```

**Swagger disponible**
```bash
curl http://localhost:5177/swagger/index.html
# Resultado: ✅ acceso correcto
```

**CORS configurado**
- ✅ Permite cualquier origen
- ✅ Permite cualquier método
- ✅ Permite cualquier encabezado

---

## Archivos relevantes de la sesión

- `01-seguridad-azure/api-local/EcommerceApi/Program.cs`
- `01-seguridad-azure/api-local/EcommerceApi/appsettings.json`
- `01-seguridad-azure/api-local/EcommerceApi/Controllers/ProductsController.cs`
- `01-seguridad-azure/api-local/EcommerceApi/Controllers/OrdersController.cs`
- `01-seguridad-azure/api-local/EcommerceApi/azure-ad-register.md`
- `01-seguridad-azure/api-local/EcommerceApi/azure-ad-config.md`
- `01-seguridad-azure/api-local/EcommerceApi/AZURE-AD-TESTS.md`
- `01-seguridad-azure/bitacora/2026-09-02-azure-ad-inicial.md` (esta bitácora)

---

## Decisión de estructura del portfolio

Se concluyó que el portfolio debe mantener una apariencia profesional y un enfoque claro en proyectos reales. En consecuencia:

- la API de Azure AD y la documentación asociada se mantienen como evidencia técnica del bloque,
- pero los artefactos de laboratorio experimental (PKCE, scripts, API auxiliar, documentación de pruebas de laboratorio) deben mantenerse fuera del repositorio principal.

Esto evita que el portfolio se vea como un cuaderno de pruebas y mejora su capacidad de presentación para clientes, recruiters o revisores técnicos.

---

## Laboratorio PKCE en repositorio independiente

**Fecha**: 2026-09-02  
**Actividad**: Finalización del laboratorio OAuth2 Authorization Code Flow con PKCE para Azure AD  
**Estado**: ✅ SEPARADO EN REPOSITORIO EXTERNO

Durante esta jornada se completó el laboratorio PKCE con Azure AD, incluyendo la implementación de la API local, el flujo de autorización con `code_challenge` y `code_verifier`, la generación de scripts de automatización y la validación end-to-end de la autenticación con Microsoft Entra ID.

### Trabajo realizado
- Desarrollo y validación del flujo PKCE con Azure AD.
- Preparación de scripts para generación de `code_verifier` y `code_challenge`.
- Configuración de la API local para aceptar tokens emitidos por Azure AD.
- Documentación de pruebas para flujos OAuth2 y validación de accesos.
- Verificación de errores de autenticación y resolución de configuración.

### Errores encontrados
- `501481`: Error asociado a la configuración del cliente/registro de aplicación en Azure AD, relacionado con permisos y flujo de autorización.
- `90013`: Error de audiencia/tenant o de solicitud de autorización no válida durante la ejecución del flujo PKCE.

### Soluciones aplicadas
- Revisado el registro de la aplicación en Azure AD y corregida su configuración.
- Confirmado el uso correcto del `client_id`, `redirect_uri`, `scope` y del flujo Authorization Code con PKCE.
- Validado el formato del token JWT y la audiencia esperada por la API local.
- Ajustado el enfoque de pruebas para diferenciar correctamente errores de autorización de errores del cliente.

### Decisión final
Se concluyó que el laboratorio, por su volumen y naturaleza experimental, debía mantenerse en un repositorio independiente para no contaminar el portfolio principal. Esta decisión permite mantener una presentación profesional, libre de artefactos de prueba y más alineada con proyectos de cartera técnica real.

### Enlace del laboratorio
- https://github.com/lanuzalorenzo/lab-azuread-oauth2-pkce-api

Este repositorio del portfolio queda como referencia técnica y de documentación del trabajo realizado, mientras que el laboratorio completo continúa disponible como proyecto separado con scripts, API, pruebas y documentación de soporte.

---

## Estado final del bloque

### ✅ Completado
- [x] Configuración de Azure AD en la API
- [x] Validación JWT Bearer
- [x] Protección de endpoints
- [x] Documentación técnica completa
- [x] Pruebas de token y validación
- [x] Auditoría del repositorio
- [x] Limpieza de artefactos experimentales no profesionales
- [x] Referencia del laboratorio PKCE en repositorio independiente

### ⏳ Pendiente
- [ ] Implementación de autorización granular por roles/scopes
- [ ] Integración con identidad real de cliente de prueba en Azure AD
- [ ] Ajuste final de seguridad para entorno de producción

---

## Conclusión

Este día se consolida el trabajo real del bloque Azure AD como una actividad técnica útil y documentada dentro del portfolio, mientras se aplica una limpieza disciplinada para mantener la estructura del repositorio alineada con una presentación profesional. La integración con Azure AD queda validada a nivel conceptual y técnico, y el proyecto mantiene un enfoque claro: portfolio de ciberseguridad con evidencias técnicas reales y reproducibles.


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

