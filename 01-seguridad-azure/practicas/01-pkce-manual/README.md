# 01 | PKCE manual con cliente público

Pedimos un pase a Entra ID a mano, con `curl`, sin librerías que escondan los pasos, y comprobamos que la API solo abre la puerta con un pase legítimo.

> **Estado:** Parcial. La ejecución histórica está en la [bitácora](../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md); la evidencia estandarizada queda pendiente de reejecución con un tenant de laboratorio.
>
> Esta práctica cubre solo el laboratorio Node.js. La validación JWT de la API .NET está validada en CI: [estado real](../../README.md#estado).

**Enlaces:** [runbook](runbook.md) · [código](../../lab/pkce/) · [evidencias](evidencias/) · [nota de trazabilidad](docs/laboratorio-pkce-azure.md).

Una aplicación pública —CLI, SPA o móvil— no puede custodiar un secreto de cliente. Para obtener un token debe usar Authorization Code con PKCE: genera un `code_verifier`, deriva un `code_challenge`, autoriza contra Entra ID, canjea el código y presenta el token a una API que lo valida contra el JWKS del tenant. Sin PKCE, quien intercepte el código puede canjearlo.

## Qué se comprobó

| Prueba | Resultado histórico |
|---|---|
| Generación y autorización | `code_verifier` de 43–128 caracteres, `code_challenge` S256 y redirección con código |
| Canje y validación JWKS | JWT con `exp`, `aud` e `iss`; `GET /api/products` responde 200 |
| Pruebas negativas | Sin token y con la firma manipulada, la API responde 401 |

Las tres pruebas están documentadas en la bitácora, pero sin el formato actual: falta repetirlas con fecha, entorno y salidas redactadas.

## Limitaciones

- No hay tenant de laboratorio disponible: de ahí el estado **Parcial**.
- El laboratorio es local y HTTP, sin tests ni CI.
- Los identificadores de tenant, aplicación y usuario se redactan.
- Los ejemplos antiguos con `Bearer $TOKEN` son marcadores cubiertos por la allowlist de `.gitleaks.toml`; el historial no se reescribió. Si alguna vez se usó un token real, hay que rotarlo.

**Coste:** 0; todo ocurre en local y en el tenant de laboratorio.
