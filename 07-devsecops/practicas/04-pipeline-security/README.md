# 04 | Pipeline segura y validación de entregas

> **Estado:** **Parcial**. Permisos mínimos y gates validados en CI; OIDC y despliegue no están activos.
>
> **Referencias:** MCSB DS-1, DS-2, GS-2, IM-1.

Una pipeline con permisos de escritura sobre todo el repositorio es una credencial más que robar, y una que no bloquea no es un control: es un informe. El diseño es el contrario: cada job recibe lo mínimo, cada análisis puede tumbar la entrega y ninguna credencial dura más que la ejecución.

## Qué se aplicó

| Pieza | Configuración |
|---|---|
| Permisos | `contents: read`; `security-events: write` solo donde se publica SARIF |
| Gates | Build, 10 pruebas xUnit, Gitleaks, CodeQL, Trivy, contenedor e IaC |
| Contenedor | Multi-stage, usuario no-root, Trivy image |
| Concurrencia | Un run por rama, cancelando el anterior |
| OIDC | Diseñado, no activo |

## Validación

| Prueba | Resultado observado |
|---|---|
| Build y pruebas | Compila y pasan las 10 pruebas en local y en CI |
| Permisos del workflow | Revisados y acotados por job |
| Gates de seguridad | Todos los jobs en verde el 2026-10-19 |
| Contenedor no-root | UID distinto de 0 dentro del contenedor |

## Lecciones

- Un gate que no bloquea el merge es un aviso, no un control.
- El permiso de escritura se concede al job que lo necesita, no al workflow entero.
- Quedan fuera la firma de artefactos y el SBOM; sin ellos, la cadena de suministro está a medias.

## Más detalle

- [Módulo 07](../../README.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Diseño OIDC](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/README.md)
