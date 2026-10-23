# Evidencias — 01 PKCE manual

> **Estado:** Pendiente. Hay una [ejecución histórica](../../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md) narrada en la bitácora, pero no se conservó con el formato de evidencia actual.
>
> **Runbook:** [../runbook.md](../runbook.md).

## Por qué falta

La evidencia estandarizada necesita un tenant de Microsoft Entra ID con dos registros de aplicación. No hay tenant de laboratorio disponible desde que se consolidó la práctica, así que el estado es **Parcial**: existe el procedimiento y existe la ejecución histórica; falta la prueba redactada con fecha y entorno.

## Qué se capturará al reejecutar

```text
evidencias/YYYY-MM-DD-01-pkce-manual/
  README.md          # fecha, entorno, resultado y limitaciones
  comandos.md        # comandos ejecutados y salida redactada
  artefactos/
    generate-pkce.txt
    authorize-url.txt
    token-response.json
    call-api-200.txt
    call-api-401.txt
    call-api-tampered-401.txt
    cleanup.txt
```

| Artefacto | Qué debe demostrar |
|---|---|
| `generate-pkce.txt` | Que se generaron verifier y challenge (longitudes, no valores) |
| `authorize-url.txt` | URL con tenant y client ID redactados |
| `token-response.json` | `token_type`, `scope` y `expires_in`, sin tokens |
| `call-api-200.txt` | `200` y número de productos, sin datos personales |
| `call-api-401.txt` | `401` sin cabecera |
| `call-api-tampered-401.txt` | `401` con token manipulado |
| `cleanup.txt` | Parada de la API y borrado de `.env` |

## Redacción obligatoria

- Sin `access_token`, `refresh_token`, `id_token`, `authorization_code` ni `code_verifier`.
- Sin tenant ID, client ID, object ID ni UPN.
- Sin nombre de usuario, correo ni datos personales.
- Sin capturas que muestren la barra de direcciones con el código de autorización.

## Criterio de cierre

- La API responde `200` con un token válido.
- La API responde `401` sin token y con token manipulado.
- Todos los artefactos están redactados.
- El estado pasa a **Validado**, o se mantiene en **Parcial**, según el resultado real.
