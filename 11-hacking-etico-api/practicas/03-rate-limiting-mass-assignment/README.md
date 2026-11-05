# 03 | Rate limiting y mass assignment

El cliente no debería decidir el ID de un producto ni cuántas peticiones puede enviar por minuto. La práctica comprueba que los DTOs ignoran los campos reservados y que la API corta con `429` al superar el límite, medido el 2026-11-05.

**Referencias:** OWASP API3, API4 · MCSB PA-1

| Control | Implementación | Estado |
|---|---|---|
| DTO de producto | `CreateProductRequest` sin `Id` | Validado |
| DTO de pedido | `CreateOrderRequest` con `ProductIds` | Validado |
| Validación | DataAnnotations y `[ApiController]` | Validado |
| Rate limit | 120 req/min por IP | Validado en local ([runbook](runbook.md)) |
| Límite de cuerpo | 16 KB en escrituras | Pendiente (sin prueba de borde) |

| Prueba | Resultado |
|---|---|
| `id: 999999` en `POST /api/products` | PASS: `CreateProduct_IgnoresClientSuppliedId` |
| Precio negativo, nombre vacío, pedido vacío, producto inexistente | PASS: `400` |
| 130 peticiones en un minuto | PASS: 120 × `200` y `429` desde la 121 |
| Reinicio de ventana | PASS: tres `200` al minuto siguiente |
| `X-Forwarded-For` inventada | PASS: sigue `429` |
| Cuerpo mayor de 16 KB | Pendiente |

La ejecución completa está en la [evidencia del 2026-11-05](../../../laboratorio-final/evidencias/2026-11-05-11-api-rate-limit/README.md).

Queda un hueco: `POST /api/products` exige autenticación pero no rol, así que cualquier usuario válido puede crear productos de hasta 1.000.000. No es mass assignment, es BFLA (H-03).

El rate limit es por IP: los usuarios detrás de NAT (salida compartida) comparten cuota y las IPs distribuidas lo esquivan. La ventana fija permite hasta 240 peticiones en el borde entre dos minutos, y la respuesta `429` no incluye `Retry-After`. La prueba fue secuencial: 120/min sigue sin calibrar bajo carga.

El DTO resuelve el binding, no los permisos; y un límite sin calibración protege menos de lo que aparenta.
