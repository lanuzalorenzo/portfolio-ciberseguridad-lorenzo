# 03 | Rate limiting y mass assignment

> **Estado:** mass assignment y validación de entrada validados localmente; rate limit y límite de cuerpo definidos, pendientes de prueba de carga.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Una API sin límites de consumo puede ser saturada con peticiones o cuerpos enormes. Un binding directo del modelo permite que el cliente modifique campos reservados (ID, total, propietario).  
**Objetivo de seguridad:** Limitar el consumo por IP y evitar que el cliente controle campos del servidor.  
**Alcance:** `POST /api/products`, `POST /api/orders`, rate limiter global y límite de cuerpo.

## Controles implementados

| Control | Implementación | Estado |
|---|---|---|
| Rate limit | 120 req/min por IP | Implementado; prueba de carga pendiente |
| Límite de cuerpo | 16 KB en escrituras | Implementado; prueba de borde pendiente |
| DTO de producto | `CreateProductRequest` sin `Id` | Implementado y probado |
| DTO de pedido | `CreateOrderRequest` con `ProductIds` | Implementado y probado |
| Validación | DataAnnotations + `[ApiController]` | Implementado y probado |
| Propagación de errores | `ProblemDetails` | Implementado |

## Pruebas ejecutadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Mass assignment de `id` | `POST /api/products` con `id: 999999` | ID asignado por el servidor | PASS: `CreateProduct_IgnoresClientSuppliedId` |
| Precio negativo | `POST /api/products` con `price: -1` | `400` | PASS |
| Nombre vacío | `POST /api/products` con `name: " "` | `400` | PASS |
| Pedido vacío | `POST /api/orders` con `[]` | `400` | PASS |
| Producto inexistente | `POST /api/orders` con ID desconocido | `400` | PASS |
| Rate limit | 121 peticiones en un minuto | `429` | Pendiente: prueba manual/carga |
| Cuerpo > 16 KB | `POST` con payload grande | `413` | Pendiente |

## Remediación aplicada

- DTOs de entrada sin campos reservados.
- `Order.UserId` y `Order.Total` se calculan en servidor.
- Validación declarativa y comprobación de productos existentes.
- Rate limiter global y `RequestSizeLimit`.

## Limitaciones

- El rate limit es por IP; usuarios detrás de NAT comparten cuota.
- No hay cuota por usuario ni por operación.
- No se ha ejecutado una prueba de carga; el umbral no está calibrado.
- El límite de 16 KB puede ser demasiado bajo para futuros endpoints de carga.
- `POST /api/products` solo exige autenticación: cualquier usuario válido puede crear productos y fijar `price` dentro del rango permitido (`0–1.000.000`). Falta una política de rol y una regla de negocio sobre el precio mínimo.

## Recomendaciones

- Añadir cuotas por usuario y por endpoint.
- Exigir rol o scope para crear o modificar el catálogo, y definir si el precio 0 es válido para el negocio.
- Probar `429` y `413` con k6 o JMeter.
- Revisar el umbral con métricas reales.
- Añadir un WAF/APIM para límites de perímetro.

## Artefactos relacionados

- [`Program.cs`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Program.cs)
- [`ProductsController.cs`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Controllers/ProductsController.cs)
- [`OrdersController.cs`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Controllers/OrdersController.cs)
- [Pruebas de productos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/tests/EcommerceApi.Tests/ProductsEndpointsTests.cs)
