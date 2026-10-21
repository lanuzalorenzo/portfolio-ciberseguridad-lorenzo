# 04 | Informe final y matriz OWASP API Top 10

> **Estado:** documentado. Resume pruebas locales ejecutadas y trabajo pendiente contra un entorno desplegado.

## Resumen ejecutivo

La API de referencia implementa autenticación JWT, aislamiento de pedidos por usuario, DTOs de entrada, validación, CORS restrictivo, rate limiting y límites de cuerpo. Las pruebas locales confirman BOLA y mass assignment mitigados. Quedan pendientes la autorización granular por scopes/roles, las pruebas con tokens reales, el rate limit bajo carga y el pentest contra APIM/WAF.

## Matriz OWASP API Security Top 10

| Riesgo | Hallazgo | Severidad | Estado | Evidencia |
|---|---|---|---|---|
| **API1 BOLA** | Pedido ajeno accesible sin control de propiedad | Alta | Mitigado | `UserCannotReadAnotherUsersOrder` |
| **API2 Broken Authentication** | Validación JWT incompleta o laxa | Alta | Parcial | Configuración revisada; token real pendiente |
| **API3 Mass Assignment** | Cliente controla `id`, `total` o `userId` | Alta | Mitigado | `CreateProduct_IgnoresClientSuppliedId` |
| **API4 Resource Consumption** | Sin límites de peticiones/cuerpo | Media | Parcial | Rate limit 120/min y 16 KB; prueba de carga pendiente |
| **API5 BFLA** | Sin políticas por rol/scope; `POST /api/products` accesible a cualquier usuario | Alta | Parcial | Solo `[Authorize]`; ver H-03 |
| **API6 Business Flows** | Sin antifraude ni límites de negocio | Media | Pendiente | Fuera del alcance actual |
| **API7 SSRF** | No aplica | — | No aplica | La API no consume URLs del usuario |
| **API8 Misconfiguration** | CORS, headers, HTTPS, contenedor | Media | Parcial | CORS deny-by-default; WAF/despliegue pendientes |
| **API9 Inventory** | Swagger solo en Development | Baja | Parcial | No hay inventario formal de versiones |
| **API10 Unsafe Consumption** | No aplica | — | No aplica | Sin APIs de terceros |

## Hallazgos y remediaciones

### H-01 — BOLA en pedidos (Alta, mitigado)

- **Descripción:** el acceso a pedidos no comprobaba la propiedad del recurso.
- **Evidencia:** prueba con dos identidades; B recibía el pedido de A.
- **Remediación:** `UserId` desde el claim, filtro por usuario y `404` para recursos ajenos.
- **Regresión:** `OrdersEndpointsTests`.

### H-02 — Mass assignment en productos (Alta, mitigado)

- **Descripción:** el modelo `Product` se enlazaba directamente y aceptaba `Id`.
- **Evidencia:** payload con `id: 999999`.
- **Remediación:** `CreateProductRequest` y asignación de ID en servidor.
- **Regresión:** `ProductsEndpointsTests`.

### H-03 — Autorización granular ausente (Alta, pendiente)

- **Descripción:** todos los endpoints requieren autenticación, pero no scopes/roles. Ejemplo concreto: `POST /api/products` permite a cualquier usuario autenticado crear un producto con precio 0, dentro del rango `0–1.000.000`.
- **Impacto:** un token válido puede acceder a cualquier operación permitida por la API y alterar el catálogo.
- **Remediación propuesta:** políticas por scope/rol, pruebas negativas y matriz de permisos; validación de negocio del precio.
- **Estado:** pendiente.

### H-04 — Rate limit no calibrado (Media, parcial)

- **Descripción:** 120 req/min por IP sin prueba de carga.
- **Impacto:** posible bypass con IPs distribuidas o bloqueo de usuarios tras NAT.
- **Remediación propuesta:** cuotas por usuario, APIM/WAF y prueba con k6.
- **Estado:** pendiente.

## Cobertura de pruebas

| Prueba | Estado |
|---|---|
| 401 sin token | PASS |
| BOLA lectura | PASS |
| BOLA listado | PASS |
| Mass assignment | PASS |
| Validación de entrada | PASS |
| Token real (firma/issuer/audience) | Pendiente |
| Rate limit 429 | Pendiente |
| Cuerpo 413 | Pendiente |
| BFLA con roles | Pendiente |

## Conclusión

El laboratorio demuestra un ciclo completo de hallazgo, remediación y regresión para BOLA y mass assignment. La madurez del módulo se completará cuando se ejecuten las pruebas contra un despliegue real con Entra ID, APIM y dos identidades delegadas.

## Artefactos relacionados

- [Pruebas de pedidos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/tests/EcommerceApi.Tests/OrdersEndpointsTests.cs)
- [Pruebas de productos](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/tests/EcommerceApi.Tests/ProductsEndpointsTests.cs)
- [Threat model](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/threat-model-appsec.md)
