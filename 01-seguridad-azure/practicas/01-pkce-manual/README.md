# 01 | PKCE manual con cliente público

> **Estado:** Validado (2026-11-26). Ejecutada contra el tenant del laboratorio y la API local; [evidencia](evidencias/2026-11-26-01-pkce-manual/README.md).
>
> **Referencias:** MCSB IM-1, IM-6 · CIS 6.3, 6.5 · NIST IA-2, IA-5.

**In English.** A public application —CLI, SPA or mobile— cannot keep a client secret. It obtains a token with Authorization Code and PKCE, and the API validates it against the tenant's JWKS; without PKCE, whoever intercepts the code can redeem it.

Una aplicación pública —CLI, SPA o móvil— no puede custodiar un secreto. Usa Authorization Code con PKCE: genera un `code_verifier`, deriva un `code_challenge`, autoriza contra Entra ID, canjea el código y presenta el token a una API que lo valida contra el JWKS del tenant. Sin PKCE, quien intercepte el código puede canjearlo.

## Qué se comprobó

Solo el laboratorio Node.js; la validación JWT de la API .NET sigue fuera de CI.

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Generación y autorización | `generate-pkce.sh` y navegador | Challenge S256 y redirección con código | Verifier de 128 caracteres y código recibido |
| Canje y validación JWKS | `exchange-token.sh` y API local | `Bearer` con `exp`, `aud` e `iss`; `200` | `Bearer`, scope de la API y cuatro productos |
| Pruebas negativas | `curl` sin token y con firma manipulada | `401` en los dos casos | `401` en los dos casos |

## Lecciones

- El generador partía el `code_verifier` en dos líneas: el canje falla con `AADSTS501481` si el salto viaja dentro del valor.
- Un cliente SPA no canjea desde `curl` (`AADSTS9002327`) y un registro en «Web» pide secreto (`AADSTS7000218`): el cliente público va en su plataforma.
- La API valida firma, emisor y audiencia; el scope no se comprueba.

## Más detalle

- [Runbook](runbook.md) · [Evidencia](evidencias/2026-11-26-01-pkce-manual/README.md) · [Código](../../lab/pkce/) · [Bitácora histórica](../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md)
