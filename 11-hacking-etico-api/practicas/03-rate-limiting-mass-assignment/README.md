# 03 | Rate limiting y mass assignment

El cliente no debería decidir el ID de un producto ni cuántas peticiones puede enviar por minuto. La práctica comprueba que los DTOs ignoran los campos reservados y deja el rate limit y el límite de cuerpo definidos pero sin probar bajo carga.

**Referencias:** OWASP API3, API4 · MCSB PA-1

| Control | Implementación | Estado |
|---|---|---|
| DTO de producto | `CreateProductRequest` sin `Id` | Probado |
| DTO de pedido | `CreateOrderRequest` con `ProductIds` | Probado |
| Validación | DataAnnotations y `[ApiController]` | Probada |
| Rate limit | 120 req/min por IP | Definido; sin prueba de carga |
| Límite de cuerpo | 16 KB en escrituras | Definido; sin prueba de borde |

| Prueba | Resultado |
|---|---|
| `id: 999999` en `POST /api/products` | PASS: `CreateProduct_IgnoresClientSuppliedId` |
| Precio negativo, nombre vacío, pedido vacío, producto inexistente | PASS: `400` |
| 121 peticiones en un minuto | Pendiente: sin prueba de carga |
| Cuerpo mayor de 16 KB | Pendiente |

Queda un hueco de autorización: `POST /api/products` exige autenticación pero no rol, así que cualquier usuario válido puede crear productos con precio entre 0 y 1.000.000. No es mass assignment, es BFLA, y está anotado como H-03.

El rate limit es por IP: los usuarios detrás de NAT comparten cuota y las IPs distribuidas lo esquivan. Sin prueba de carga, 120/min es una intención, no un umbral calibrado.

El DTO resuelve el binding, no los permisos; y un límite sin prueba no protege de nada.
