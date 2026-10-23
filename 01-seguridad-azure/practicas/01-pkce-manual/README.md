# 01 | PKCE manual con cliente público

Pedimos un pase a Entra ID a mano, con `curl`, sin librerías que escondan los pasos, y comprobamos que la API solo abre la puerta con un pase legítimo.

> **Estado:** Parcial. La ejecución histórica está documentada en la bitácora del módulo; la evidencia estandarizada queda pendiente de reejecución con un tenant de laboratorio.
>
> Esta práctica cubre **solo el laboratorio Node.js**. La validación JWT de la API .NET es otra pieza del módulo y sí está validada en CI: ver [estado real del módulo](../../README.md#estado).
>
> **Runbook:** [runbook.md](runbook.md).
>
> **Código:** [01-seguridad-azure/lab/pkce](../../lab/pkce/).
>
> **Evidencia:** [evidencias/](evidencias/).

## Contexto y alcance

**Escenario:** una aplicación pública (CLI, SPA o móvil) no puede custodiar un secreto de cliente. Para obtener un token de acceso debe usar OAuth2 Authorization Code con PKCE: genera un `code_verifier`, deriva un `code_challenge`, inicia la autorización contra Microsoft Entra ID, canjea el `authorization_code` y presenta el token a una API que lo valida criptográficamente.

**Objetivo de seguridad:** demostrar de forma manual y reproducible que el flujo PKCE protege el código de autorización y que la API no confía en el cliente: valida firma, `iss`, `aud`, `exp` y `nbf` contra el JWKS del tenant.

> [!NOTE]
> La práctica se documenta como ejercicio técnico de laboratorio. No representa un despliegue de producción ni un sistema certificado.

## Relación con el módulo

- [Conceptos y contexto](../../docs/01-conceptos.md).
- [Flujo OAuth 2.0 con PKCE](../../docs/02-flujo-oauth2-pkce.md).
- [Validación de JWT y JWKS](../../docs/03-validacion-jwt-jwks.md).
- [Bitácora histórica de la ejecución](../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md).
- [Nota de fusión del tutorial](docs/laboratorio-pkce-azure.md): el antiguo documento de laboratorio se integró en 02, 03 y el runbook.
- API de referencia del workload: [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure).

## Qué aporta

- Flujo Authorization Code + PKCE ejecutado a mano con `bash` y `curl`, sin librerías que oculten los pasos.
- Validación JWT/JWKS en una API local Node.js/Express, independiente del workload .NET.
- Prueba negativa explícita: sin token y con token manipulado la API responde `401`.
- Errores frecuentes de Entra ID documentados: `AADSTS501481` y `AADSTS90013`.

## Prerrequisitos

- Node.js 18 o superior, npm, `curl`, `openssl` y `bash`.
- Un tenant de Microsoft Entra ID con permisos para registrar aplicaciones.
- Dos registros de aplicación: cliente público y API protegida con el scope `access_as_user`.
- No se necesitan recursos de Azure desplegados; los registros de aplicación viven en el tenant.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Generación de PKCE | `./scripts/generate-pkce.sh` | `code_verifier` de 43–128 caracteres y `code_challenge` S256 | Documentado en la bitácora histórica; pendiente de reejecución |
| Autorización | URL de `/authorize` con `code_challenge` | Redirección con `authorization_code` | Documentado en la bitácora histórica; pendiente de reejecución |
| Canje de token | `./scripts/exchange-token.sh` | `access_token` JWT con `exp`, `aud` e `iss` | Documentado en la bitácora histórica; pendiente de reejecución |
| Validación JWKS | `GET /api/products` con token | `200` con datos protegidos | Documentado en la bitácora histórica; pendiente de reejecución |
| Prueba negativa sin token | `GET /api/products` | `401 Unauthorized` | Pendiente de reejecución |
| Prueba negativa con token manipulado | Cambiar un carácter de la firma | `401 Unauthorized` | Documentado en la bitácora histórica; pendiente de reejecución |

## Limitaciones

- No hay tenant de laboratorio disponible en el momento de consolidar la práctica; por eso el estado es **Parcial**.
- La evidencia estandarizada (salidas redactadas, fecha, entorno y resultado) no se conservó en la ejecución histórica.
- El laboratorio no tiene tests automatizados ni CI.
- La API es local y HTTP; no incluye TLS ni configuración de producción.
- Los identificadores de tenant, aplicación y usuario deben redactarse siempre.

## Coste

- **Estimado:** 0. Todo ocurre en local y en el tenant de laboratorio.
- **Real:** 0 en la consolidación actual; la reejecución tampoco genera coste directo.
