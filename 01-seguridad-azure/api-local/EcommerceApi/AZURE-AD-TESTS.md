# Pruebas de Integración con Azure AD

## Obtener un Token JWT desde Azure AD

### Prerequisitos
- Application Registration creada en Azure AD (EcommerceApi)
- Aplicación Cliente registrada con Client Secret configurado
- Permisos de API asignados a la aplicación cliente

### Valores Necesarios
```
TENANT_ID = 7133f9a8-4c6c-47a3-b9a7-55bad5090288
CLIENT_ID = d6800b3e-a409-4129-ba4d-7d56bd55f1a8
CLIENT_SECRET = <tu-client-secret-aqui>
AUDIENCE = api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8
```

## Métodos para Obtener Token

### Método 1: Usar curl (Linux/Mac/Windows PowerShell)

```bash
# Definir variables
TENANT_ID="7133f9a8-4c6c-47a3-b9a7-55bad5090288"
CLIENT_ID="d6800b3e-a409-4129-ba4d-7d56bd55f1a8"
CLIENT_SECRET="tu-client-secret-aqui"
AUDIENCE="api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8"

# Obtener token
curl -X POST \
  "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${CLIENT_ID}" \
  -d "scope=${AUDIENCE}/.default" \
  -d "client_secret=${CLIENT_SECRET}" \
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

### Método 2: Guardar Token en Variable

```bash
TOKEN=$(curl -s -X POST \
  "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=d6800b3e-a409-4129-ba4d-7d56bd55f1a8" \
  -d "scope=api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8/.default" \
  -d "client_secret=tu-client-secret-aqui" \
  -d "grant_type=client_credentials" | jq -r '.access_token')

echo "Token: $TOKEN"
```

## Pruebas con curl

### Prueba 1: Endpoint Protegido - GET /api/products

```bash
curl -H "Authorization: Bearer <TOKEN>" \
  http://localhost:5000/api/products
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

### Prueba 2: Endpoint Protegido - GET /api/products/{id}

```bash
curl -H "Authorization: Bearer <TOKEN>" \
  http://localhost:5000/api/products/1
```

**Respuesta esperada (200 OK):**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "stock": 10
}
```

### Prueba 3: Endpoint Protegido - GET /api/orders

```bash
curl -H "Authorization: Bearer <TOKEN>" \
  http://localhost:5000/api/orders
```

**Respuesta esperada (200 OK):**
```json
[]
```

### Prueba 4: Endpoint Protegido - POST /api/orders

```bash
curl -X POST \
  -H "Authorization: Bearer <TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"productId":1,"quantity":2,"totalPrice":1999.98}' \
  http://localhost:5000/api/orders
```

**Respuesta esperada (201 Created):**
```json
{
  "id": 1,
  "productId": 1,
  "quantity": 2,
  "totalPrice": 1999.98
}
```

### Prueba 5: Sin Token - Debe Fallar

```bash
curl http://localhost:5000/api/products
```

**Respuesta esperada (401 Unauthorized):**
```
HTTP/1.1 401 Unauthorized
```

### Prueba 6: Token Inválido - Debe Fallar

```bash
curl -H "Authorization: Bearer invalid-token-12345" \
  http://localhost:5000/api/products
```

**Respuesta esperada (401 Unauthorized):**
```
HTTP/1.1 401 Unauthorized
```

## Pruebas en Swagger

### Paso 1: Ejecutar la API

```bash
dotnet run
```

La API estará disponible en: `http://localhost:5000`
Swagger UI: `http://localhost:5000/swagger`

### Paso 2: Obtener Token JWT

Como se describe arriba, obtener un token válido desde Azure AD.

### Paso 3: Autorizar en Swagger

1. Abrir `http://localhost:5000/swagger`
2. Hacer clic en el botón **"Authorize"** (arriba a la derecha)
3. En el modal, pegar el token (sin la palabra "Bearer"):
   ```
   eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9...
   ```
4. Hacer clic en **"Authorize"**

### Paso 4: Probar Endpoints

1. Expandir un endpoint (ej: `GET /api/products`)
2. Hacer clic en **"Try it out"**
3. Hacer clic en **"Execute"**

El header `Authorization: Bearer <token>` se agregará automáticamente.

### Respuestas Esperadas en Swagger

**Éxito (200 OK):**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "stock": 10
}
```

**Error (401 Unauthorized):**
```
Unauthorized
```

## Errores Comunes y Soluciones

### Error 1: AADSTS50058 - Invalid tenant format

**Causa:** El `TENANT_ID` es incorrecto o mal formateado.

**Solución:**
```bash
# Verificar formato: debe ser GUID válido
# Copiar desde Azure Portal > Azure Active Directory > Properties
TENANT_ID="7133f9a8-4c6c-47a3-b9a7-55bad5090288"
```

### Error 2: AADSTS700016 - Application not found

**Causa:** El `CLIENT_ID` es incorrecto o no pertenece al tenant.

**Solución:**
```bash
# Usar el Application (client) ID, no el Object ID
# Copiar desde Azure Portal > App registrations > Application ID
CLIENT_ID="d6800b3e-a409-4129-ba4d-7d56bd55f1a8"
```

### Error 3: AADSTS7000215 - Invalid client secret

**Causa:** El `CLIENT_SECRET` es incorrecto o ha expirado.

**Solución:**
1. Ir a Azure Portal
2. App registrations > tu aplicación cliente
3. Certificates & secrets > Client secrets
4. Crear un nuevo secret
5. Copiar el valor (se muestra solo una vez)

### Error 4: 401 Unauthorized en la API

**Problema:** El token se obtiene correctamente, pero la API lo rechaza.

**Posibles causas:**
1. El `Audience` no coincide con la API
2. El token está expirado
3. Configuración de validación incorrecta en Program.cs

**Solución:**
```bash
# Decodificar token en https://jwt.io
# Verificar:
# - "aud" debe ser: api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8
# - "iss" debe ser: https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0
# - "exp" (expiración) debe ser en el futuro
```

### Error 5: CORS Error

**Problema:** Cross-Origin Request Blocked

**Causa:** Aplicación cliente en diferente origen

**Solución:** La API ya tiene CORS habilitado:
```csharp
policy.AllowAnyOrigin()
      .AllowAnyMethod()
      .AllowAnyHeader();
```

## Script Automatizado para Testing

Guardar en `test-auth.sh`:

```bash
#!/bin/bash

set -e

# Configuración
TENANT_ID="7133f9a8-4c6c-47a3-b9a7-55bad5090288"
CLIENT_ID="d6800b3e-a409-4129-ba4d-7d56bd55f1a8"
CLIENT_SECRET="${CLIENT_SECRET:-tu-client-secret-aqui}"
AUDIENCE="api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8"
API_URL="http://localhost:5000"

echo "🔐 Obteniendo token JWT desde Azure AD..."

# Obtener token
RESPONSE=$(curl -s -X POST \
  "https://login.microsoftonline.com/${TENANT_ID}/oauth2/v2.0/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=${CLIENT_ID}" \
  -d "scope=${AUDIENCE}/.default" \
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

# Prueba 1: GET /api/products
echo "📝 Prueba 1: GET /api/products"
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API_URL/api/products" | jq '.'
echo ""

# Prueba 2: GET /api/orders
echo "📝 Prueba 2: GET /api/orders"
curl -s -H "Authorization: Bearer $TOKEN" \
  "$API_URL/api/orders" | jq '.'
echo ""

# Prueba 3: Sin token (debe fallar)
echo "📝 Prueba 3: Sin token (debe fallar con 401)"
curl -s -w "\nStatus: %{http_code}\n" \
  "$API_URL/api/products" || true
echo ""

echo "✅ Pruebas completadas"
```

Usar:
```bash
chmod +x test-auth.sh
./test-auth.sh
```

## Checklist de Testing

- [ ] Token se obtiene correctamente desde Azure AD
- [ ] GET /api/products funciona con token
- [ ] GET /api/products/{id} funciona con token
- [ ] GET /api/orders funciona con token
- [ ] POST /api/orders funciona con token
- [ ] Requests sin token devuelven 401
- [ ] Token inválido devuelve 401
- [ ] Swagger muestra opción "Authorize"
- [ ] Swagger funciona con JWT
- [ ] Headers Authorization: Bearer <token> se envían correctamente

## Verificar Token en jwt.io

1. Ir a https://jwt.io
2. Pegar el token completo en "Encoded"
3. Verificar el payload:

```json
{
  "iss": "https://login.microsoftonline.com/7133f9a8-4c6c-47a3-b9a7-55bad5090288/v2.0",
  "aud": "api://d6800b3e-a409-4129-ba4d-7d56bd55f1a8",
  "exp": 1234567890,
  "iat": 1234567800,
  "scp": "access_as_user"
}
```

## Referencia Rápida

| Método | Endpoint | Requiere Token | Esperado |
|--------|----------|---|---|
| GET | /api/products | ✅ Sí | 200 OK |
| GET | /api/products/{id} | ✅ Sí | 200 OK |
| POST | /api/products | ✅ Sí | 201 Created |
| DELETE | /api/products/{id} | ✅ Sí | 204 No Content |
| GET | /api/orders | ✅ Sí | 200 OK |
| GET | /api/orders/{id} | ✅ Sí | 200 OK |
| POST | /api/orders | ✅ Sí | 201 Created |
| DELETE | /api/orders/{id} | ✅ Sí | 204 No Content |

---

**Última actualización:** 2026-09-02
**Autor:** Sistema de Seguridad en Azure
