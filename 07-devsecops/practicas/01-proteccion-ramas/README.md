# 01 | Protección de ramas y revisión de cambios

> **Estado:** **Validado** sobre `lab-api-local-azure`: push directo y forzado rechazados. El merge con checks en rojo no se reprobó.
>
> **Referencias:** MCSB DS-1, GS-2, IR-1, DS-2.

Sin regla, cualquier cambio entra en `main` sin que nadie lo mire y un `force-push` reescribe el historial. Un ruleset exige pull request y checks: es requisito del repositorio, no costumbre.

## Qué hay configurado

Reglas del ruleset `main`, consultadas por API el 2026-11-04:

| Regla | Valor |
|---|---|
| Pull request | Obligatorio, sin aprobaciones exigidas |
| Checks exigidos | Siete jobs del pipeline, con la rama al día |
| Fusión | Solo squash, con historial lineal |
| Force-push y borrado | Bloqueados |
| Exenciones | Ninguna: tampoco el propietario |

## Validación

| Prueba | Resultado observado |
|---|---|
| Escritura directa a `main` | Rechazada con `GH013`: «7 of 7 required status checks are expected» |
| Push forzado a `main` | Rechazado: el historial no se reescribe |
| PR con los checks en verde | Se fusiona sin aprobación; la revisión es proceso, no puerta |
| Checks en rojo | No reprobado desde el ruleset actual |

La prueba se ejecutó como propietario: el rechazo no depende del rol. Exigir aprobación bloquearía a quien trabaja solo, porque GitHub no deja aprobar el propio pull request.

## Lecciones

- La protección cubre al propietario: la automatización usa el mismo camino, un PR de Dependabot con los checks en verde.
- Sin aprobación obligatoria, la revisión es práctica previa; la puerta real son los checks y la rama al día.
- Siete checks con la rama al día encarecen el merge; ese coste evita integrar algo roto.

## Más detalle

- [Módulo 07](../../README.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
