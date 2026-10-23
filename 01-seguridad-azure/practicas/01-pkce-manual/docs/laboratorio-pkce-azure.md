# Laboratorio — OAuth 2.0 Authorization Code con PKCE (documento fusionado)

> **Este documento se fusionó el 2026-10-23.** Su contenido vive ahora en las fuentes únicas del módulo. Se conserva este puntero para no romper enlaces externos y para dejar rastro del cambio.

## Por qué se retiró

Repetía el flujo de [02](../../../docs/02-flujo-oauth2-pkce.md), la validación de [03](../../../docs/03-validacion-jwt-jwks.md) y los pasos del [runbook](../runbook.md). Además usaba rutas antiguas (`api-local/...`) que ya no existen: el código vive en [`lab/pkce/`](../../../lab/pkce/).

Tener un `docs/` dentro de `practicas/` rompía la separación del módulo: `docs/` explica, `practicas/` demuestra y `lab/` ejecuta.

## Dónde está ahora cada cosa

| Antes en este documento | Ahora en |
|---|---|
| Explicación del flujo y por qué PKCE | [02 — Flujo OAuth 2.0 con PKCE](../../../docs/02-flujo-oauth2-pkce.md) |
| Cómo se valida el JWT con JWKS | [03 — Validación JWT y JWKS](../../../docs/03-validacion-jwt-jwks.md) |
| Registro de aplicaciones, URL de autorización y canje | [runbook.md](../runbook.md) |
| Errores `AADSTS501481` y `AADSTS90013` | [02 — Lecciones de troubleshooting](../../../docs/02-flujo-oauth2-pkce.md#lecciones-de-troubleshooting) |
| Buenas prácticas | [02 — Reglas prácticas](../../../docs/02-flujo-oauth2-pkce.md#reglas-prácticas) |
| Código ejecutable | [lab/pkce](../../../lab/pkce/README.md) |
| Ejecución histórica del 2026-09-02 | [bitácora](../../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md) |

## Nota de trazabilidad

El contenido completo sigue disponible en el historial de Git. No se borró ninguna evidencia ni bitácora: solo se retiró la copia duplicada de la explicación.
