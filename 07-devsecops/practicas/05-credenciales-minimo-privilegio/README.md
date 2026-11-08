# 05 | Credenciales de mínimo privilegio para feeds privados

> **Estado:** **Validado** en local y CI ([run 42470483409](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/42470483409), 2026-11-08) para la separación de credenciales; el ciclo de Dependabot sigue **Parcial** (falta una PR real de `LL.*`).
>
> **Referencias:** MCSB IM-1, IM-2, DS-2.

Un build que descarga paquetes de un feed privado necesita una credencial. Si es la misma que abre PRs y edita workflows, cualquier script hereda permisos que no necesita. Separarlas no evita el robo; limita el daño.

## Qué se comprobó

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Restore limpio | Caché NuGet vacía con `GH_PACKAGES_TOKEN` | Descargar `LL.*` del feed | `exit 0`; solución restaurada (2026-11-08) |
| Prueba negativa | Sin la variable y caché vacía | `401` del feed | `NU1301` y `401` en `LL.*` |
| Aislamiento de `gh` | Shell nuevo | `GITHUB_TOKEN` libre; llavero intacto | `GH_PACKAGES_TOKEN` definido; `gh auth status` con `repo` |
| CI | `secrets.GITHUB_TOKEN` mapeado a `GH_PACKAGES_TOKEN` | Restore y build en verde | [Run 42470483409](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/42470483409) |
| Dependabot | Secreto `LL_PACKAGES_TOKEN` | Sin `Secret Not Found` | Run 42410124439, sin error de credenciales |

El PAT tiene solo `read:packages` y 90 días; `gh` conserva `repo` y `workflow`. La imagen lo recibe como secreto de BuildKit.

## Lecciones

- `GITHUB_TOKEN` es la credencial de sesión que `gh` y Git prefieren; un PAT de solo lectura ahí deja los `push` en `403` y parece un problema de permisos del repositorio.
- Dependabot no acepta el `GITHUB_TOKEN` de Actions en `registries`: necesita un secreto propio con el mismo PAT.
- El PAT vive en el llavero y se desbloquea con la sesión: cualquier proceso del usuario puede leerlo. Acota el daño; no sustituye al antimalware.

## Más detalle

- [Módulo 07](../../README.md)
- [Credenciales del feed](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/docs/credenciales.md)
- [`NuGet.config`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/NuGet.config)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
