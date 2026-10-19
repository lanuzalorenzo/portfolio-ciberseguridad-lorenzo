# 01 | Protección de ramas y revisión de cambios

> **Estado:** validado en GitHub para los repositorios de código. El propietario administrador conserva bypass; se documenta como limitación.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Repositorio con flujo de cambios directo hacia `main`, sin validación ni control de integridad del historial.  
**Objetivo de seguridad:** Garantizar que cualquier integración pase por revisión, validación automática y restricciones de integridad.  
**Alcance:** Rama principal, pull requests, revisión y reglas de protección.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Repositorio Git** | Código y trazabilidad | `main` protegida. |
| **Pull Request** | Revisión y validación | Todos los cambios pasan por PR. |
| **Required reviewers** | Revisión humana | Al menos un aprobador. |
| **Status checks** | Validación automática | Build, tests y seguridad. |
| **Historial** | Integridad | Sin force-push ni borrado de la rama. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Protección de la rama principal | PR obligatorio | MCSB DS-1 |
| Revisión obligatoria | Aprobación antes del merge | MCSB GS-2 |
| Bloqueo de sobreescritura | Force-push y borrado bloqueados | MCSB IR-1 |
| Validación automática | Checks de CI/CD | MCSB DS-2 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escritura directa a `main` | Revisión de la regla | Bloqueada para no administradores | PASS: regla activa; admin puede omitir |
| Fusión vía PR | Apertura de PR | Revisión requerida | PASS |
| Protección de historial | Intento de force-push | Rechazado | PASS (regla) |
| Checks automáticos | Ejecución del pipeline | Requisitos antes del merge | Implementado; pendiente de ejecución verde |

## Limitación

La protección de rama no protege frente a una cuenta administradora comprometida. Para reducir ese riesgo se recomienda aplicar la regla también a administradores (`enforce_admins`) y usar una cuenta de servicio para automatizaciones.

## Artefactos relacionados

- [Política de protección de ramas](../../branch-protection.md)
- [Workflow de la API](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/.github/workflows/devsecops-ci.yml)
