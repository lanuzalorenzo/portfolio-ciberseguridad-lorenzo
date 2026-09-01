# Tests - EcommerceApi

Este archivo contiene ejemplos de pruebas usando `curl` para validar los endpoints de la API.

**Prerequisitos:**
- La API debe estar ejecutándose: `dotnet run`
- Tener `curl` instalado en el sistema

---

## Productos

### 1. Obtener todos los productos

```bash
curl http://localhost:5000/api/products
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "name": "Laptop",
    "price": 999.99,
    "stock": 5
  },
  {
    "id": 2,
    "name": "Mouse",
    "price": 19.99,
    "stock": 50
  }
]
```

---

### 2. Obtener un producto específico

```bash
curl http://localhost:5000/api/products/1
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "name": "Laptop",
  "price": 999.99,
  "stock": 5
}
```

---

### 3. Crear un nuevo producto

```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Keyboard","price":29.99,"stock":20}'
```

**Respuesta esperada:**
```json
{
  "id": 3,
  "name": "Keyboard",
  "price": 29.99,
  "stock": 20
}
```

---

## Pedidos

### 1. Obtener todos los pedidos

```bash
curl http://localhost:5000/api/orders
```

**Respuesta esperada:**
```json
[
  {
    "id": 1,
    "productIds": [1, 2],
    "totalAmount": 1019.98,
    "orderDate": "2024-01-15T10:30:00"
  }
]
```

---

### 2. Obtener un pedido específico

```bash
curl http://localhost:5000/api/orders/1
```

**Respuesta esperada:**
```json
{
  "id": 1,
  "productIds": [1, 2],
  "totalAmount": 1019.98,
  "orderDate": "2024-01-15T10:30:00"
}
```

---

### 3. Crear un nuevo pedido

```bash
curl -X POST http://localhost:5000/api/orders \
  -H "Content-Type: application/json" \
  -d '{"productIds":[1,2]}'
```

**Respuesta esperada:**
```json
{
  "id": 2,
  "productIds": [1, 2],
  "totalAmount": 1019.98,
  "orderDate": "2024-01-15T14:45:00"
}
```

---

## Pruebas con Powershell (Windows)

Si usas Windows con PowerShell, puedes adaptar los comandos:

### Obtener productos
```powershell
Invoke-WebRequest -Uri "http://localhost:5000/api/products" -Method GET
```

### Crear producto
```powershell
$body = @{
    name = "Keyboard"
    price = 29.99
    stock = 20
} | ConvertTo-Json

Invoke-WebRequest -Uri "http://localhost:5000/api/products" `
  -Method POST `
  -ContentType "application/json" `
  -Body $body
```

---

## Pruebas con Postman

1. Importa estos endpoints en Postman
2. Configura la URL base: `http://localhost:5000`
3. Realiza las pruebas según los ejemplos anteriores

**Endpoints Postman:**
- GET `{{base_url}}/api/products`
- GET `{{base_url}}/api/products/1`
- POST `{{base_url}}/api/products`
- GET `{{base_url}}/api/orders`
- GET `{{base_url}}/api/orders/1`
- POST `{{base_url}}/api/orders`

---

## Códigos HTTP Esperados

| Método | Endpoint | Código | Descripción |
|--------|----------|--------|-------------|
| GET | /api/products | 200 | Éxito |
| GET | /api/products/{id} | 200 | Éxito |
| GET | /api/products/999 | 404 | No encontrado |
| POST | /api/products | 201 | Creado |
| POST | /api/products | 400 | Solicitud inválida |
| GET | /api/orders | 200 | Éxito |
| GET | /api/orders/{id} | 200 | Éxito |
| POST | /api/orders | 201 | Creado |

---

## Próximas Pruebas (Post Azure AD)

Una vez integrado Azure AD, las pruebas incluirán:

```bash
# Con JWT Token
curl -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  http://localhost:5000/api/products
```

---

**Nota**: Estos ejemplos asumen que la API corre en `http://localhost:5000`. Ajusta el puerto si es necesario.
