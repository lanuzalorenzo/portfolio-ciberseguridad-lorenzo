# Evidencia — 01 / PKCE manual

> **Identificador:** `2026-11-26-01-pkce-manual`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** PASS
>
> **Runbook:** [runbook.md](../../runbook.md)

**In English.** Hand-run of OAuth 2.0 Authorization Code with PKCE against the lab tenant: a public client with no secret, code exchange, JWKS validation by the local API, one positive call and two negative ones.

## 1. Contexto

- **Fecha:** 2026-11-26.
- **Responsable:** autor del repositorio.
- **Entorno:** Ubuntu 24.04, Node.js 22.22.1, `curl` y `openssl`; API local en `http://localhost:4010`; tenant de laboratorio.
- **Alcance:** autorización con PKCE, canje del código, validación del JWT contra el JWKS y pruebas negativas.
- **Datos:** sintéticos; el catálogo de productos es de ejemplo.
- **Autorización:** tenant propio del laboratorio; el cliente público se creó para esta ejecución y queda para las siguientes.

## 2. Comandos ejecutados

Los comandos completos, con los valores sensibles sustituidos, están en [comandos.md](comandos.md).

```bash
./scripts/generate-pkce.sh
./scripts/exchange-token.sh
curl -i -H "Authorization: Bearer <access_token>" http://localhost:4010/api/products
curl -i http://localhost:4010/api/products
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Generación de PKCE | `code_verifier` de 43–128 caracteres y `code_challenge` S256 | Verifier de 128 caracteres; SHA-256 coincide con el challenge | PASS |
| Autorización | Redirección con `code` y `state` | Redirección a `http://localhost/callback` con ambos | PASS |
| Canje | `Bearer` con el scope de la API | `Bearer`, scope de la API y 5211 s | PASS |
| API con token | `200` y el catálogo | `200` con cuatro productos | PASS |
| API sin token | `401` | `401`, falta el token | PASS |
| Token manipulado | `401` por firma inválida | `401`, `invalid signature` | PASS |

## 4. Artefactos

- [generate-pkce.txt](artefactos/generate-pkce.txt): longitudes y comprobación del challenge, sin valores.
- [authorize-url.txt](artefactos/authorize-url.txt): URL con tenant y cliente redactados.
- [token-response.json](artefactos/token-response.json): tipo, scope y caducidad, sin token.
- [call-api-200.txt](artefactos/call-api-200.txt), [call-api-401.txt](artefactos/call-api-401.txt) y [call-api-tampered-401.txt](artefactos/call-api-tampered-401.txt): las tres respuestas.
- [cleanup.txt](artefactos/cleanup.txt): parada, borrado y cierre de la sesión de Azure.

## 5. Limpieza

La API se paró, se borraron `.env` y los ficheros temporales con el código y el token, se cerró la sesión de Azure y se eliminó el volumen de la CLI. El registro del cliente público queda en el tenant, sin secreto y con permiso delegado de solo lectura al scope.

## 6. Coste y tiempo

- **Coste:** 0; tenant de laboratorio y ejecución local.
- **Tiempo:** una hora, incluida la corrección del generador.

## 7. Conclusiones

- El flujo completo se ejecutó y la API rechaza lo que no lleva un token legítimo.
- El generador partía el `code_verifier` en dos líneas y el canje fallaba con `AADSTS501481`; corregido en [`scripts/generate-pkce.sh`](../../../../lab/pkce/scripts/generate-pkce.sh).
- Un cliente SPA no canjea desde `curl` (`AADSTS9002327`) y un registro en «Web» pide secreto (`AADSTS7000218`): el cliente público va en su plataforma.

## 8. Limitaciones

- Los identificadores de tenant, cliente y API se sustituyen por placeholders; el código, el verifier y los tokens no se guardan.
- La validación JWT de la API .NET queda fuera de CI y pendiente de ejecutar con este tenant.
- El laboratorio es local y HTTP; el job del laboratorio en el CI solo comprueba la carga del módulo y las dependencias, no el comportamiento del flujo.
