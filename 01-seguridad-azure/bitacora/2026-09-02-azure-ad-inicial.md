# 📄 Bitácora — Integración inicial de Azure AD

## 📘 Proyecto
Portfolio de Ciberseguridad — Módulo 01: Seguridad Azure

## 🎯 Objetivo
Integrar Azure Active Directory como proveedor de identidad en la API local y asegurar los endpoints mediante autenticación JWT Bearer.

---

## 🛠 Trabajo realizado

### 1. Integración de Azure AD en la API
- Configuración de autenticación JWT Bearer en `Program.cs`.
- Activación de `UseAuthentication()` y `UseAuthorization()`.
- Validación de tokens emitidos por Azure AD.

### 2. Ajustes de configuración de identidad
- Añadido `TenantId`, `ClientId`, `Audience` y `Authority` en `appsettings.json`.
- Validación correcta de tokens emitidos por Azure AD.

### 3. Protección de endpoints
- Aplicación de `[Authorize]` en controladores.
- Endpoints protegidos: `ProductsController`, `OrdersController`.

### 4. Validación de flujos OAuth2
- Revisión de los flujos:
  - Client Credentials  
  - Device Code  
  - Authorization Code  
- Validación de tokens JWT y su audiencia.

### 5. Limpieza del repositorio
- Separación del laboratorio PKCE experimental en un repositorio independiente.
- Eliminación de artefactos no alineados con el portfolio profesional.

---

## 🔍 Validaciones realizadas
- API compilada y ejecutada correctamente.
- Endpoints protegidos responden 401 sin token.
- Swagger accesible y funcional.
- CORS configurado correctamente.

---

## 📂 Archivos relevantes
- `Program.cs`
- `appsettings.json`
- `Controllers/ProductsController.cs`
- `Controllers/OrdersController.cs`

---

## ⚠️ Problemas encontrados
- Error 501481: configuración incorrecta del registro de aplicación.
- Error 90013: audiencia o tenant incorrecto en la solicitud.

---

## 🛠 Soluciones aplicadas
- Revisión completa del registro de aplicación en Azure AD.
- Corrección de `client_id`, `redirect_uri`, `scope` y flujo Authorization Code con PKCE.
- Validación del token JWT y su audiencia esperada.

---

## 🧠 Aprendizajes clave
- Integración real de Azure AD con API local mediante JWT Bearer.
- Importancia de proteger endpoints con `[Authorize]`.
- Validación de flujos OAuth2 y tokens JWT.
- Mantener el portfolio limpio y modular.

---

## 📎 Recursos útiles
- Azure Portal  
- JWT.io  
- Postman  
- curl
