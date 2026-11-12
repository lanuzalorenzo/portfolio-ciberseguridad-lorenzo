# 04 | Pipeline segura y validación de entregas

> **Estado:** **Parcial**. Permisos mínimos y gates validados en CI; OIDC con Azure y despliegue no están activos.
>
> **Referencias:** MCSB DS-1, DS-2, GS-2, IM-1.

Una pipeline con permisos de escritura sobre todo el repositorio es una credencial más que robar, y una que no bloquea no es un control: es un informe. El diseño es el contrario: cada job recibe lo mínimo, cada análisis puede tumbar la entrega y ninguna credencial dura más que la ejecución.

## Qué se aplicó

| Pieza | Configuración |
|---|---|
| Permisos | `contents: read`; `security-events: write` solo donde se publica SARIF |
| Gates | Build, pruebas xUnit, Gitleaks, CodeQL, Trivy, contenedor e IaC |
| Contenedor | Multi-stage, usuario no-root, Trivy image |
| SBOM | Inventario CycloneDX de lo que contiene la imagen, adjunto a la ejecución; el job que lo genera solo lee |
| Firma | cosign keyless sobre el digest publicado; `cosign verify` con la identidad del workflow |
| Atestación | SBOM atestado con `cosign attest --type cyclonedx` y verificado con `cosign verify-attestation` |
| Concurrencia | Un run por rama, cancelando el anterior |
| OIDC con Azure | Diseñado, no activo |

## Validación

| Prueba | Resultado observado |
|---|---|
| Build y pruebas | Compila y pasan las pruebas de la solución en local y en CI |
| Permisos del workflow | Revisados y acotados por job |
| Gates de seguridad | Todos los jobs en verde el 2026-10-19 |
| Contenedor no-root | UID distinto de 0 dentro del contenedor |
| SBOM CycloneDX | `.cdx.json` de 3 842 componentes adjunto a la ejecución del 2026-11-12, con el digest de la imagen y el del fichero |
| Firma y atestación | Run [43314295991](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/43314295991): firma y atestación publicadas y verificadas |

## Lecciones

- Un gate que no bloquea el merge es un aviso, no un control.
- El permiso de escritura se concede al job que lo necesita, no al workflow entero.
- La firma y la atestación se validaron el 2026-11-12: el SBOM queda ligado al digest y al workflow que lo construyó. OIDC con Azure y despliegue siguen fuera.

## Más detalle

- [Módulo 07](../../README.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
- [Workflow de publicación de la imagen](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/container-publish.yml)
- [Diseño OIDC con Azure](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/README.md)
