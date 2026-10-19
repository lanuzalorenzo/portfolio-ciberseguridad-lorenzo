# 02 | Endurecimiento de JWT y claims

> **Estado:** configuración revisada. La validación con tokens reales de Entra ID queda pendiente de un tenant autorizado.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Una API que acepta JWT debe validar firma, emisor, audiencia y expiración. Una configuración laxa permite tokens de otro tenant, algoritmos no esperados o tokens expirados.  
**Objetivo de seguridad:** Verificar que la API solo acepta tokens emitidos por la autoridad configurada, para la audiencia correcta y dentro de su vida útil.  
**Alcance:** `Program.cs`, `AzureAdOptions`, configuración de `JwtBearer` y endpoints protegidos.

## Hipótesis

1. Un token sin firma válida es rechazado.
2. Un token de otro tenant o con `aud` incorrecta es rechazado.
3. Un token expirado es rechazado.
4. La API no acepta `alg: none` ni claves simétricas no configuradas.

## Configuración revisada

| Control | Implementación | Estado |
|---|---|---|
| Firma | JWKS de la autoridad | Implementado |
| Issuer | `ValidIssuer = Authority` | Implementado |
| Audience | `ValidAudience = Audience` | Implementado |
| Lifetime | `ValidateLifetime = true` | Implementado |
| Clock skew | 2 minutos | Implementado |
| Algoritmos | Configuración por defecto de `JwtBearer` | Revisar allowlist explícita |
| Scopes/roles | No aplicados por endpoint | Pendiente |
| Rotación de claves | Gestionada por Entra ID | Depende del tenant |

## Pruebas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Sin token | `GET /api/products` | `401` | PASS: prueba `GetProducts_WithoutToken_ReturnsUnauthorized` |
| Token inválido | `Authorization: Bearer invalid-token` | `401` | Pendiente con JwtBearer real; el esquema de test no valida JWT |
| Token de otro tenant | Token de tenant B | `401` | Pendiente: requiere dos tenants |
| Token expirado | Token con `exp` pasado | `401` | Pendiente |
| Audience incorrecta | Token para otra API | `401` | Pendiente |
| Algoritmo no permitido | Token `alg: none` | `401` | Pendiente: revisar allowlist |

## Remediación / recomendaciones

- Mantener `ValidateIssuer`, `ValidateAudience`, `ValidateLifetime` y `ValidateIssuerSigningKey` en `true`.
- No deshabilitar `RequireHttpsMetadata` en producción.
- Considerar una allowlist explícita de algoritmos (`RS256`) si el tenant lo permite.
- Añadir políticas de scopes/roles y pruebas negativas.
- No registrar tokens completos en logs.

## Limitaciones

- No se dispone de un tenant con dos aplicaciones y dos usuarios para ejecutar todos los casos.
- El esquema de test sustituye la autenticación en las pruebas de integración; por eso las pruebas de JWT real quedan pendientes.
- La rotación de claves es responsabilidad de Entra ID y no se ha simulado.

## Artefactos relacionados

- [`Program.cs`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Program.cs)
- [`AzureAdOptions.cs`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/EcommerceApi/Configuration/AzureAdOptions.cs)
- [Guía de pruebas con tokens](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/azure-ad-tests.md)
