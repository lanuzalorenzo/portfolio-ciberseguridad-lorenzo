# 04 | Privileged Identity Management (PIM) en Microsoft Entra ID

> **Estado:** validado en laboratorio (PASS). Tenant de prueba, sin datos reales.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Cuentas administrativas con asignaciones permanentes de altos privilegios, con riesgo de compromiso continuo y persistencia de atacantes.  
**Objetivo de seguridad:** Implementar acceso Just-in-Time (JIT) y Zero Standing Privileges mediante PIM, con activación bajo demanda, justificación y MFA.  
**Alcance:** Roles de Microsoft Entra en tenant de laboratorio y asignaciones elegibles (*Eligible*).

## Procedimiento

1. Revisar las asignaciones elegibles en Microsoft Entra roles.
2. Activar Global Reader indicando justificación, duración y MFA.
3. Comprobar el estado activo y desactivar el rol.
4. Revisar el retorno a *Eligible* y los eventos de auditoría.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluye identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra PIM** | Gobernanza de identidades privilegiadas | Asignaciones elegibles y activas. |
| **Rol Global Reader** | Rol de laboratorio | Asignación *Eligible* para el usuario de prueba. |
| **Flujo JIT** | Activación temporal | MFA, justificación y duración limitada. |
| **Resource Audit** | Trazabilidad | Registro de activaciones, desactivaciones y expiraciones. |

## Controles de seguridad

| Control | Implementación | Referencia |
|---|---|---|
| Zero Standing Access | Asignación *Eligible* en lugar de *Active* | MCSB PA-1 / PA-3 |
| Elevación protegida con MFA | MFA obligatoria en la activación | MCSB PA-2 |
| Auditoría de elevaciones | Motivo, usuario y ventana temporal | MCSB LT-1 |

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Estado inicial sin privilegios | Inspección de roles | Sin permisos administrativos activos | PASS: solo *Eligible* |
| Activación sin justificación | Flujo *My Roles* | Bloqueo | PASS: justificación y MFA obligatorias |
| Activación JIT y expiración | Activación y espera | *Active* temporal y retorno a *Eligible* | PASS: evento registrado en auditoría |

## Lecciones aprendidas

- Reducir el tiempo de exposición de privilegios mitiga el impacto de credenciales robadas.
- PIM debe complementarse con Access Reviews para retirar elegibilidades inactivas.
- Se requieren cuentas *break-glass* permanentes, excluidas de PIM y monitorizadas.

## Artefactos relacionados

- [Configuración y validación de PIM](docs/informe-tecnico.md)
- [Bitácora del módulo](../../bitacora/2026-09-07-pim-entra-id.md)
