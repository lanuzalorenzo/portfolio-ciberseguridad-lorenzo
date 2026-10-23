# 01 | Protección de ramas y revisión de cambios

> **Estado:** **Validado** en GitHub para los repositorios de código. `enforce_admins` está desactivado: el propietario puede saltarse la regla, y se documenta como limitación.
>
> **Referencias:** MCSB DS-1, GS-2, IR-1, DS-2.

Sin regla, cualquier cambio entra en `main` sin que nadie lo mire y el historial se puede reescribir con un `force-push`. La protección de rama convierte la revisión en un requisito del repositorio y no en una costumbre del equipo.

## Qué hay configurado

Reglas consultadas por API el 2026-10-23:

| Regla | Valor |
|---|---|
| Pull request | Obligatorio, con una aprobación |
| Checks exigidos | Siete jobs del pipeline, con la rama al día |
| Historial | Lineal: sin commits de merge |
| Force-push y borrado | Bloqueados |
| Administradores | Exentos: `enforce_admins` desactivado |

## Validación

| Prueba | Resultado observado |
|---|---|
| Escritura directa a `main` | Rechazada para cuentas sin permiso de administrador |
| PR sin aprobación | No se puede fusionar |
| Pipeline en rojo | El merge queda bloqueado: los checks son obligatorios |
| Force-push | Rechazado por la regla |

## Lecciones

- La regla no protege de una cuenta administradora comprometida: activar `enforce_admins` y usar una cuenta de servicio para automatizaciones cerraría el hueco.
- Una aprobación sin criterio se convierte en un clic; el valor está en que el revisor mire el cambio.
- Siete checks obligatorios con la rama al día encarecen el merge, y ese coste es justo el que evita integrar algo roto.

## Más detalle

- [Módulo 07](../../README.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
