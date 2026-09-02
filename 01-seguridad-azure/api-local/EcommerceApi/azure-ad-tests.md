# Pruebas de Azure AD - Guía Completa

## Obtener un Token JWT desde Azure AD

### Opción 1: Usando curl (Terminal/PowerShell)

#### Paso 1: Preparar los valores necesarios

```bash
TENANT_ID="00000000-0000-0000-0000-000000000000"      # Tu Directory (tenant) ID
CLIENT_ID="11111111-1111-1111-1111-111111111111"      # Application ID de tu aplicación cliente
CLIENT_SECRET="your-client-secret-here"               # Client Secret
RESOURCE="api://ecommerce-api"                         # Application ID URI de tu API
```

#### Paso 2: Solicitar un token

```bash
curl -X POST \
  "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${CLIENT_ID}" \
  -d "scope=${RESOURCE}/.default" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "grant_type=client_credentials"
```

**Ejemplo con valores concretos:**

```bash
curl -X POST \
  "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=11111111-1111-1111-1111-111111111111" \
  -d "scope=api://ecommerce-api/.default" \
  -d "client_secret=your-client-secret-here" \
  -d "grant_type=client_credentials"
```

**Respuesta exitosa:**

```json
{
  "token_type": "Bearer",
  "expires_in": 3599,
  "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### Paso 3: Guardar el token en una variable

```bash
# En bash
TOKEN=$(curl -s -X POST \
  "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${CLIENT_ID}" \
  -d "scope=${RESOURCE}/.default" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "grant_type=client_credentials" \
  | jq -r '.access_token')

echo "Token obtenido: $TOKEN"
```

```powershell
# En PowerShell
$params = @{
    Uri = "https://login.microsoftonline.com/$TENANT_ID/oauth2/v2.0/token"
    Method = "POST"
    ContentType = "application/x-www-form-urlencoded"
    Body = "client_id=$CLIENT_ID&scope=$RESOURCE/.default&client_secret=$CLIENT_SECRET&grant_type=client_credentials"
}

$response = Invoke-RestMethod @params
$TOKEN = $response.access_token
Write-Host "Token: $TOKEN"
```

### Opción 2: Usando jwt.io para Debugging

1. Ir a [jwt.io](https://jwt.io)
2. Pegar el token completo en el área "Encoded"
3. Verás el payload decodificado con los claims

**Ejemplo de payload:**
```json
{
  "iss": "https://login.microsoftonline.com/00000000-0000-0000-0000-000000000000/v2.0",
  "aud": "api://ecommerce-api",
  "exp": 1672531200,
  "scp": "order.read order.write"
}
```

## Pruebas con curl

### Prueba 1: Endpoint Público (Sin Token)

```bash
curl http://localhost:5000/api/products/public/info
```

**Respuesta esperada (200 OK):**
```json
{
  "message": "This is public"
}
```

---

### Prueba 2: Endpoint Protegido (Con Token)

```bash
# Asegúrate de tener el TOKEN primero
TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/api/orders
```

**Respuesta esperada (200 OK):**
```json
{
  "data": "All orders"
}
```

---

### Prueba 3: Endpoint Protegido Sin Token (Debe Fallar)

```bash
curl http://localhost:5000/api/orders
```

**Respuesta esperada (401 Unauthorized):**
```
HTTP/1.1 401 Unauthorized
```

---

### Prueba 4: Token Inválido (Debe Fallar)

```bash
curl -H "Authorization: Bearer invalid-token-here" \
  http://localhost:5000/api/orders
```

**Respuesta esperada (401 Unauthorized):**
```json
{
  "error": "Invalid token"
}
```

---

### Prueba 5: Verificar Claims en Token

```bash
TOKEN="eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9..."

curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:5000/api/orders/current-user
```

**Respuesta esperada (200 OK):**
```json
{
  "userId": "user-object-id",
  "email": "user@example.com",
  "scopes": "order.read order.write"
}
```

---

### Prueba 6: Token Expirado (Debe Fallar)

Si el token ha expirado:
```bash
curl -H "Authorization: Bearer expired-token" \
  http://localhost:5000/api/orders
```

**Respuesta esperada (401 Unauthorized):**
```json
{
  "error": "Token expired"
}
```

---

### Prueba 7: Endpoint Requiere Scope Específico

Si intentas acceder a un endpoint que requiere `order.write` pero tu token solo tiene `order.read`:

```bash
# Token con solo order.read
curl -H "Authorization: Bearer token-with-order-read-only" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"name": "New Product"}' \
  http://localhost:5000/api/products
```

**Respuesta esperada (403 Forbidden):**
```json
{
  "error": "Insufficient permissions"
}
```

## Pruebas en Swagger

### Paso 1: Configurar Swagger

En tu aplicación con `http://localhost:5000/swagger`, deberías ver un botón **"Authorize"**.

### Paso 2: Obtener Token

Como se describe arriba, obtener un token JWT válido.

### Paso 3: Usar Token en Swagger

1. Hacer clic en el botón **"Authorize"**
2. En el modal que aparece, pegar el token (sin "Bearer"):
   ```
   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
3. Hacer clic en **"Authorize"**

### Paso 4: Hacer Requests

1. Expandir un endpoint (ej: `GET /api/orders`)
2. Hacer clic en **"Try it out"**
3. Hacer clic en **"Execute"**

El header `Authorization: Bearer <token>` se agregará automáticamente.

### Ejemplo de Respuesta Exitosa

```
200 OK

{
  "data": "All orders"
}
```

### Ejemplo de Respuesta con Error

```
401 Unauthorized

{
  "error": "Invalid token"
}
```

## Errores Comunes y Soluciones

### 1. AADSTS50058: Invalid tenant format

**Error completo:**
```json
{
  "error": "invalid_request",
  "error_description": "AADSTS50058: Invalid tenant format"
}
```

**Causa:** El `TENANT_ID` es incorrecto o mal formateado.

**Solución:**
- Verificar que el `TENANT_ID` es un GUID válido (formato: `00000000-0000-0000-0000-000000000000`)
- Copiar desde Azure Portal > Azure Active Directory > Properties > Directory ID

---

### 2. AADSTS700016: Application not found in directory

**Error completo:**
```json
{
  "error": "invalid_client",
  "error_description": "AADSTS700016: Application not found in directory"
}
```

**Causa:** El `CLIENT_ID` es incorrecto o no pertenece al tenant.

**Solución:**
- Verificar que es el Application ID (no Object ID)
- Verificar que está registrado en el mismo tenant
- Copiar desde Azure Portal > App registrations > Application ID

---

### 3. AADSTS7000215: Invalid client secret provided

**Error completo:**
```json
{
  "error": "invalid_client",
  "error_description": "AADSTS7000215: Invalid client secret provided"
}
```

**Causa:** El `CLIENT_SECRET` es incorrecto o ha expirado.

**Solución:**
- Verificar que el secret es correcto (copiar de Azure Portal)
- Verificar que no ha expirado (fecha en Certificates & secrets)
- Si expiró, crear uno nuevo

---

### 4. 401 Unauthorized en la API

**Problema:** El token se obtiene correctamente, pero la API lo rechaza.

**Causas posibles:**
1. El `Audience` en `appsettings.json` no coincide con el Application ID URI
2. El `TenantId` es incorrecto
3. La API no está validando correctamente

**Solución:**
```bash
# Decodificar el token para verificar claims
# Ir a jwt.io y pegar el token

# Verificar que estos valores coinciden:
# - "aud": debe coincidir con Audience en appsettings.json
# - "iss": debe incluir el TENANT_ID correcto
```

---

### 5. 403 Forbidden (Scope insuficiente)

**Problema:** El token es válido, pero no tiene los permisos (scopes) necesarios.

**Causa:** La aplicación cliente no tiene los permisos asignados.

**Solución:**
1. En Azure Portal, ir a la aplicación **cliente**
2. API permissions > Add a permission
3. Seleccionar la API (EcommerceApi)
4. Seleccionar los scopes necesarios
5. Grant admin consent

---

### 6. Token inválido o malformado

**Problema:** `Authorization: Bearer token-inválido`

**Soluciones a probar:**
1. Verificar que el token comienza con "eyJ" (Base64 URL encoded)
2. Verificar que tiene exactamente 3 partes separadas por puntos: `header.payload.signature`
3. Verificar que no tiene espacios extra al inicio o final
4. Obtener un token nuevo

---

## Script Automatizado para Testing

### Bash Script

Guardar en `test-api.sh`:

```bash
#!/bin/bash

set -e

# Configuración
TENANT_ID="00000000-0000-0000-0000-000000000000"
CLIENT_ID="11111111-1111-1111-1111-111111111111"
CLIENT_SECRET="your-client-secret"
RESOURCE="api://ecommerce-api"
API_URL="http://localhost:5000"

echo "📋 Iniciando pruebas de Azure AD..."
echo "=================================="

# Obtener token
echo "🔑 Obteniendo token JWT..."
RESPONSE=$(curl -s -X POST \
  "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${CLIENT_ID}" \
  -d "scope=${RESOURCE}/.default" \
  -d "client_secret=${CLIENT_SECRET}" \
  -d "grant_type=client_credentials")

TOKEN=$(echo "$RESPONSE" | jq -r '.access_token')

if [ "$TOKEN" = "null" ]; then
    echo "❌ Error obteniendo token:"
    echo "$RESPONSE" | jq '.'
    exit 1
fi

echo "✅ Token obtenido"
echo ""

# Prueba 1: Endpoint público
echo "📝 Prueba 1: Endpoint público"
curl -s "$API_URL/api/products/public/info" | jq '.'
echo ""

# Prueba 2: Endpoint protegido con token
echo "📝 Prueba 2: Endpoint protegido (con token)"
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API_URL/api/orders" | jq '.'
echo ""

# Prueba 3: Endpoint protegido sin token
echo "📝 Prueba 3: Endpoint protegido (sin token) - Debe fallar"
curl -s "$API_URL/api/orders" || echo "Error esperado"
echo ""

# Prueba 4: Información del usuario
echo "📝 Prueba 4: Información del token"
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API_URL/api/orders/current-user" | jq '.'
echo ""

echo "✅ Pruebas completadas"
```

Usar:
```bash
chmod +x test-api.sh
./test-api.sh
```

---

## Checklist de Testing

### Antes de Ir a Producción

- [ ] Token se obtiene correctamente desde Azure AD
- [ ] Endpoint público funciona sin token
- [ ] Endpoint protegido rechaza sin token (401)
- [ ] Endpoint protegido acepta con token válido (200)
- [ ] Token inválido es rechazado (401)
- [ ] Scopes se validan correctamente (403 si insuficiente)
- [ ] Swagger muestra configuración de JWT
- [ ] Bearer schema aparece en Swagger UI
- [ ] Errores se registran correctamente en logs
- [ ] HTTPS funciona en todos los endpoints
- [ ] Token expira correctamente después del tiempo especificado

