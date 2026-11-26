# Evidencias — 01 PKCE manual

> **Estado:** Validado (2026-11-26). La evidencia está en [2026-11-26-01-pkce-manual](2026-11-26-01-pkce-manual/README.md); la ejecución histórica sigue en la [bitácora](../../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md).
>
> **Runbook:** [../runbook.md](../runbook.md).

## La evidencia

La carpeta de la reejecución guarda la fecha, el entorno, el resultado y los comandos con las salidas redactadas. El registro de aplicación del cliente público queda en el tenant para futuras ejecuciones, sin secreto y con permiso delegado de solo lectura al scope.

## Qué contiene la evidencia

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
