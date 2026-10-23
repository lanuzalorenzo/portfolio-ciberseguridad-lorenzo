# 02 | Detección de secretos y credenciales expuestas

> **Estado:** **Validado** localmente y en CI (run 39243360276, 2026-10-19).
>
> **Referencias:** MCSB IM-1, IM-2, DS-2.

Un token pegado en un commit sigue ahí aunque se borre en el siguiente: el historial guarda el objeto. Gitleaks recorre el historial completo en cada push a `main` y en cada pull request, y un hallazgo tumba el job. Si el secreto ya se empujó, el escaneo no lo borra del historial: obliga a rotarlo y a decidir si se reescribe.

## Qué se aplicó

| Pieza | Configuración |
|---|---|
| Gitleaks 8.30.1 | Historial completo con `fetch-depth: 0` |
| Bloqueo | `--exit-code 2`: un hallazgo tumba el job |
| Allowlist | Solo rutas de documentación y patrones `$TOKEN` o JWT truncados |
| Respuesta | Rotar la credencial y valorar la reescritura del historial |

## Validación

| Prueba | Resultado observado |
|---|---|
| Escaneo del historial completo | 0 secretos reales en local y en CI |
| Falsos positivos de documentación | La allowlist los cubre; el resto del repositorio se escanea igual |
| Bloqueo ante hallazgo | Configurado con `--exit-code 2`; no se probó con un secreto real |

## Lecciones

- La allowlist es el punto débil: una regla por ruta puede tapar un secreto real escondido en un `.md`.
- Primero se rota la credencial; reescribir el historial viene después, y solo si el secreto llegó a publicarse.
- Escanear el historial completo, y no solo el diff del commit, es lo que encuentra lo que ya estaba dentro.

## Más detalle

- [Módulo 07](../../README.md)
- [`.gitleaks.toml`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.gitleaks.toml)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
