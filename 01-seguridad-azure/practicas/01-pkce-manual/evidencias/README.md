# Evidencias — 01 PKCE manual

> **Estado:** Pendiente. La ejecución histórica está documentada en la [bitácora del módulo](../../../bitacora/2026-09-02-lab-azuread-oauth2-pkce-api.md), pero no se conservó como evidencia estandarizada.
>
> **Runbook:** [../runbook.md](../runbook.md).

## Por qué está pendiente

La ejecución estandarizada requiere un tenant de Microsoft Entra ID con dos registros de aplicación. En el momento de consolidar la práctica no hay tenant de laboratorio disponible. Por eso el estado de la práctica es **Parcial**: hay una ejecución histórica narrada, pero falta la evidencia redactada con fecha, entorno y resultado.

## Estructura prevista

Cuando se reejecute, la evidencia debe vivir en:

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

## Redacción obligatoria

- Sin `access_token`, `refresh_token`, `id_token`, `authorization_code` ni `code_verifier`.
- Sin tenant ID, client ID, object ID ni UPN.
- Sin nombre de usuario, correo ni datos personales.
- Sin capturas con la barra de direcciones que muestre el código de autorización.

## Criterio de cierre

- La API responde `200` con un token válido.
- La API responde `401` sin token y con token manipulado.
- Todos los artefactos están redactados.
- El estado de la práctica se actualiza a **Validado** o **Parcial** según el resultado real.
