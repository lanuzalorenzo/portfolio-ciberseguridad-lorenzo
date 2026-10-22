# 11 | Hacking ético de APIs

> **Estado:** validación local ejecutada. Las pruebas de autorización, mass assignment y validación de entrada se ejecutan contra la API local. El pentest contra un despliegue real de Azure/APIM está pendiente.

Este módulo convierte la API de referencia en un objetivo controlado para validar controles del **OWASP API Security Top 10 (2023)**. No es un catálogo de ataques: cada prueba tiene una hipótesis, una evidencia y una remediación verificable.

## Autorización y ética

- Todas las pruebas se ejecutan contra `lab-api-local-azure`, un laboratorio propio.
- No se escanean dominios, APIs ni tenants de terceros.
- No se incluyen tokens, secretos ni datos de clientes.
- Las pruebas que requieren Azure se describen como pendientes hasta disponer de un entorno autorizado.

El alcance, las condiciones de ejecución, los criterios de parada y la retirada de artefactos están en [Alcance y autorización del laboratorio](docs/alcance-y-autorizacion.md).

## Objetivo

- Validar BOLA/IDOR y BFLA en los endpoints de pedidos.
- Revisar la configuración de validación JWT y los claims relevantes.
- Probar *mass assignment*, validación de entrada y consumo de recursos.
- Documentar hallazgos con severidad, evidencia y estado de remediación.

## Carga de trabajo

[**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure): API .NET 10 con autenticación Entra ID, DTOs, aislamiento de pedidos por usuario y pruebas de integración.

## Metodología

Las siete fases ordenan el trabajo y cada una deja una evidencia verificable. El modelo es una herramienta de organización, no una metodología certificada.

| Fase | Qué se hace | Evidencia |
|---|---|---|
| 1. Reconocimiento | Inventario de endpoints, métodos y modelos | Matriz OWASP y cobertura de endpoints en [04](practicas/04-informe-final/README.md) |
| 2. Autenticación | Revisión de firma, emisor, audiencia y vida útil | [02 — JWT y claims](practicas/02-jwt-claims/README.md): configuración revisada; token real pendiente |
| 3. Autorización | Pruebas con dos identidades (A y B) y recursos cruzados | [01 — BOLA/BFLA](practicas/01-bola-bfla/README.md): `UserCannotReadAnotherUsersOrder` |
| 4. Entrada | Mass assignment, tipos, límites y validación | [03](practicas/03-rate-limiting-mass-assignment/README.md): `CreateProduct_IgnoresClientSuppliedId` |
| 5. Consumo | Rate limit y tamaño de petición | [03](practicas/03-rate-limiting-mass-assignment/README.md): configuración revisada; carga pendiente |
| 6. Remediación | Cambio de código y prueba de regresión | Tests de `EcommerceApi.Tests` citados en los hallazgos mitigados |
| 7. Informe | Hallazgo, severidad, impacto, evidencia y estado | [04 — Informe final](practicas/04-informe-final/README.md) |

## Prácticas

- [BOLA/BFLA: aislamiento de pedidos](practicas/01-bola-bfla/README.md) — *validado localmente* · [runbook](practicas/01-bola-bfla/runbook.md) · [evidencia](../docs/laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md)
- [Endurecimiento de JWT y claims](practicas/02-jwt-claims/README.md) — *configuración revisada; token real pendiente*
- [Rate limiting y mass assignment](practicas/03-rate-limiting-mass-assignment/README.md) — *validado localmente; rate limit manual pendiente*
- [Informe final y matriz OWASP API Top 10](practicas/04-informe-final/README.md) — *documentado*

## Relación con otros módulos

- [01 — OAuth 2.0, PKCE y JWT](../01-seguridad-azure/README.md): fundamento de autenticación.
- [07 — DevSecOps](../07-devsecops/README.md): SAST/SCA y pruebas en CI.
- [08 — Redes Azure](../08-seguridad-red-azure/README.md): exposición y Private Endpoints.
- [12 — Forense cloud](../12-forense-cloud-respuesta/README.md): evidencia y respuesta.
- [ai-agent-local-lab](https://github.com/lanuzalorenzo/ai-agent-local-lab): pruebas adversariales de LLM (inyección y robustez a perturbaciones). Fuera del alcance de este módulo: aquí el objetivo es la API, no el modelo.

## Alcance

El módulo demuestra pruebas de seguridad de API sobre un laboratorio local y deja explícito qué requiere un despliegue real (APIM, WAF, tokens de Entra, dos usuarios delegados). No es un pentest de producción y no se ha probado ningún sistema de terceros. Los detalles están en [Alcance y autorización del laboratorio](docs/alcance-y-autorizacion.md).
