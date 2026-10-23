# 02 | Endurecimiento de JWT y claims

Un JWT válido para otra API, otro tenant o con la fecha pasada no debería abrir una puerta. La revisión comprueba qué valida el `JwtBearer` de la API y qué casos siguen sin probarse por falta de un tenant autorizado.

**Referencias:** OWASP API2 · MCSB IA-2

| Control | Implementación | Estado |
|---|---|---|
| Firma | JWKS de la autoridad | Implementado |
| Emisor y audiencia | `ValidIssuer`, `ValidAudience` | Implementado |
| Vida útil | `ValidateLifetime`, desfase de 2 minutos | Implementado |
| Algoritmos | Configuración por defecto | Revisar allowlist explícita |
| Scopes y roles | No aplicados por endpoint | Pendiente |

| Prueba | Resultado |
|---|---|
| Sin token | PASS: `GetProducts_WithoutToken_ReturnsUnauthorized` |
| Token inválido, de otro tenant, expirado o con audiencia incorrecta | Pendiente: el esquema de test no valida JWT |
| `alg: none` | Pendiente: sin allowlist explícita |

La configuración revisada está en `Program.cs` y `AzureAdOptions`; las pruebas con tokens reales necesitan dos aplicaciones y dos usuarios en un tenant, que no hay en este laboratorio.

Sin allowlist, el middleware acepta los algoritmos que considere válidos; fijar `RS256` de forma explícita reduce la superficie, aunque no sustituye la validación de firma. Validar la firma sin validar la audiencia deja pasar tokens de otras APIs; y una prueba de integración con la autenticación sustituida no dice nada del JWT real.
