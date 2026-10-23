# 04 | Informe final y matriz OWASP API Top 10

El cierre del módulo pone en una tabla los diez riesgos de OWASP API, lo que se probó y lo que sigue abierto. No es una certificación: es el estado real de una API local con dos pruebas de autorización y tres de entrada ejecutadas.

**Referencias:** OWASP API Security Top 10 (2023) · MCSB PA-7

| Riesgo | Hallazgo | Severidad | Estado | Evidencia |
|---|---|---|---|---|
| **API1 BOLA** | Pedido ajeno accesible sin control de propiedad | Alta | Mitigado | `UserCannotReadAnotherUsersOrder` |
| **API2 Broken Authentication** | Validación JWT incompleta o laxa | Alta | Parcial | Configuración revisada; token real pendiente |
| **API3 Mass Assignment** | Cliente controla `id`, `total` o `userId` | Alta | Mitigado | `CreateProduct_IgnoresClientSuppliedId` |
| **API4 Resource Consumption** | Sin límites de peticiones ni de cuerpo | Media | Parcial | Rate limit 120/min y 16 KB; carga pendiente |
| **API5 BFLA** | Sin políticas por rol; `POST /api/products` abierto a cualquier usuario | Alta | Parcial | Ver H-03 |
| **API6 Business Flows** | Sin antifraude ni límites de negocio | Media | Pendiente | Fuera de alcance |
| **API7 SSRF** | No aplica | — | No aplica | La API no consume URLs del usuario |
| **API8 Misconfiguration** | CORS, headers, HTTPS, contenedor | Media | Parcial | CORS deny-by-default; WAF pendiente |
| **API9 Inventory** | Swagger solo en Development | Baja | Parcial | Sin inventario formal de versiones |
| **API10 Unsafe Consumption** | No aplica | — | No aplica | Sin APIs de terceros |

Se ejecutaron el `401` sin token, las dos pruebas de BOLA, mass assignment y validación de entrada. Siguen pendientes el token real, el `429`, el `413` y la prueba de BFLA con roles.

El ciclo hallazgo-remediación-regresión está cerrado para BOLA y mass assignment. Lo que falta no es documentación: es un tenant, un despliegue con APIM y una prueba de carga. Los detalles de cada hallazgo están en las prácticas [01](../01-bola-bfla/README.md), [02](../02-jwt-claims/README.md) y [03](../03-rate-limiting-mass-assignment/README.md).
