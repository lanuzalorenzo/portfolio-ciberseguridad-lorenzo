# Bitácora — Obtención de Tokens JWT desde Azure AD (02/09/2026)

## 📋 Objetivo

Establecer el flujo de trabajo para obtener tokens JWT desde Azure AD (Microsoft Entra ID) y utilizarlos para autenticar solicitudes a la API EcommerceApi.

## 🔑 Valores de Configuración

### App Registration en Azure AD

| Campo | Valor |
|-------|-------|
| **Tenant ID** | `7133f9a8-4c6c-47a3-b9a7-55bad5090288` |
| **Client ID (App ID)** | `d6800b3e-a409-4129-ba4d-7d56bd55f1a8` |
| **Application ID URI** | `api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8` |
| **Scope** | `access_as_user` |

### Endpoints de Azure AD

| Endpoint | URL |
|----------|-----|
| **Authority (v2.0)** | `https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0` |
| **Token Endpoint** | `https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/token` |
| **Authorization Endpoint** | `https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/authorize` |

## 🔐 Flujos de Obtención de Token

### Opción 1: Client Credentials Flow (Para aplicaciones del servidor)

**Uso:** Aplicación backend se autentica directamente con Azure AD.

**Requisitos:**
- Client Secret (se genera en Certificates & secrets)
- Persmisos de API asignados

**Comando curl:**

```bash
curl -X POST \
  "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=d6800b3e-a409-4129-ba4d-7d56bd55f1a8" \
  -d "scope=api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8/.default" \
  -d "client_secret=<YOUR_CLIENT_SECRET>" \
  -d "grant_type=client_credentials"
```

**Respuesta:**

```json
{
  "token_type": "Bearer",
  "expires_in": 3599,
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### Opción 2: Device Code Flow (Para aplicaciones sin navegador)

**Uso:** Flujo interactivo para dispositivos sin navegador web.

**Paso 1: Solicitar device_code**

```bash
curl -X POST \
  "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/devicecode" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=d6800b3e-a409-4129-ba4d-7d56bd55f1a8" \
  -d "scope=api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8/.default"
```

**Respuesta:**

```json
{
  "device_code": "DAQABAAEAAABd...",
  "user_code": "ABC123DEF",
  "verification_uri": "https://microsoft.com/devicelogin",
  "expires_in": 900,
  "interval": 5,
  "message": "To sign in, use a web browser to open the page https://microsoft.com/devicelogin and enter the code ABC123DEF to authenticate."
}
```

**Paso 2: Usuario ingresa el código en el navegador**

1. Ir a: `https://microsoft.com/devicelogin`
2. Ingresar código: `ABC123DEF`
3. Iniciar sesión con credenciales de Azure AD
4. Autorizar permisos

**Paso 3: Sondear el token (cada 5 segundos)**

```bash
curl -X POST \
  "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=urn:ietf:params:oauth:grant-type:device_code" \
  -d "client_id=d6800b3e-a409-4129-ba4d-7d56bd55f1a8" \
  -d "device_code=DAQABAAEAAABd..."
```

**Respuesta (cuando se autoriza):**

```json
{
  "token_type": "Bearer",
  "expires_in": 3599,
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

## 🧪 Testing con Token JWT

### Obtener Token

```bash
# Guardar token en variable
TOKEN=$(curl -s -X POST \
  "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=d6800b3e-a409-4129-ba4d-7d56bd55f1a8" \
  -d "scope=api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8/.default" \
  -d "client_secret=<YOUR_CLIENT_SECRET>" \
  -d "grant_type=client_credentials" | jq -r '.access_token')

echo "Token obtenido: $TOKEN"
```

### Probar Endpoints Protegidos

**GET /api/products**

```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5177/api/products
```

**Respuesta esperada (200 OK):**

```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "stock": 10
  },
  ...
]
```

**GET /api/products/{id}**

```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5177/api/products/1
```

**POST /api/orders**

```bash
curl -X POST \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"productId":1,"quantity":2,"totalPrice":1999.98}' \
  http://localhost:5177/api/orders
```

**GET /api/orders**

```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5177/api/orders
```

### Sin Token (Debe Fallar)

```bash
curl -i http://localhost:5177/api/products
```

**Respuesta esperada (401 Unauthorized):**

```
HTTP/1.1 401 Unauthorized
Content-Length: 0
WWW-Authenticate: Bearer
```

## 🌐 Testing en Swagger

### Paso 1: Ejecutar la API

```bash
cd 01-seguridad-azure/api-local/EcommerceApi
dotnet run
# API en: http://localhost:5177
```

### Paso 2: Acceder a Swagger

```
http://localhost:5177/swagger
```

### Paso 3: Obtener Token

Como se describe arriba, obtener un token JWT válido.

### Paso 4: Autorizar en Swagger

1. Hacer clic en **"Authorize"** (botón arriba a la derecha)
2. Pegar el token (sin "Bearer"):
   ```
   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
3. Hacer clic en **"Authorize"**

### Paso 5: Probar Endpoints

1. Expandir endpoint (ej: `GET /api/products`)
2. Hacer clic en **"Try it out"**
3. Hacer clic en **"Execute"**

El header se agregará automáticamente.

## 🔍 Decodificar Token en jwt.io

1. Ir a: `https://jwt.io`
2. Pegar token en **"Encoded"**
3. Verificar payload:

```json
{
  "iss": "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0",
  "aud": "api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8",
  "exp": 1234567890,
  "iat": 1234567800,
  "scp": "access_as_user"
}
```

## ⚠️ Errores Comunes

### Error: Invalid tenant

```
AADSTS50058: Invalid tenant format
```

**Causa:** Tenant ID incorrecto

**Solución:** Verificar formato GUID en Azure Portal

---

### Error: Application not found

```
AADSTS700016: Application not found in directory
```

**Causa:** Client ID incorrecto

**Solución:** Verificar Application ID en App registrations

---

### Error: Invalid client secret

```
AADSTS7000215: Invalid client secret provided
```

**Causa:** Secret expirado o incorrecto

**Solución:** Crear nuevo secret en Certificates & secrets

---

### Error: 401 Unauthorized

**Causa:** Token expirado o inválido

**Solución:**
- Verificar expiración en jwt.io
- Verificar Audience coincide
- Obtener nuevo token

---

### Error: 403 Forbidden

**Causa:** Token válido pero sin permisos

**Solución:**
- Asignar API permissions a aplicación cliente
- Grant admin consent en Azure Portal

## 📊 Validación de Token

La API valida automáticamente:

- ✅ **Firma:** Usando claves públicas de Azure AD
- ✅ **Issuer:** Debe ser el endpoint v2.0 de tu tenant
- ✅ **Audience:** Debe ser tu Application ID URI
- ✅ **Expiración:** Verifica que no esté expirado
- ✅ **No Before (nbf):** Verifica timing

## 🔒 Seguridad

### Mejores Prácticas

1. **Nunca compartir Client Secret**
   - No guardar en git
   - No hardcodear en código
   - Usar variables de entorno o Key Vault

2. **Usar HTTPS siempre**
   - Tokens viajan en Authorization header
   - Usar certificados válidos

3. **Rotación de Secretos**
   - Cambiar cada 6-12 meses
   - Tener rotation plan

4. **Monitoreo de Logs**
   - Revisar intentos fallidos
   - Alertas para cambios

## 📝 Checklist de Testing

- [ ] Token obtenido correctamente desde Azure AD
- [ ] GET /api/products funciona con token
- [ ] GET /api/products/{id} funciona con token
- [ ] GET /api/orders funciona con token
- [ ] POST /api/orders funciona con token
- [ ] Requests sin token devuelven 401
- [ ] Token inválido devuelve 401
- [ ] Token expirado devuelve 401
- [ ] Swagger muestra botón Authorize
- [ ] Swagger funciona con JWT
- [ ] Device Code Flow funciona (opcional)

## 📚 Referencias

- [Azure AD OAuth 2.0 Flows](https://docs.microsoft.com/en-us/azure/active-directory/develop/active-directory-v2-flows)
- [Device Code Flow](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-device-code)
- [JWT.io - Decodificar tokens](https://jwt.io)
- [Postman - Colecciones de prueba](https://www.postman.com)

---

**Fecha:** 02/09/2026
**Estado:** ✅ Configuración completada
**Próximos Pasos:** Testing con tokens reales desde Azure AD
