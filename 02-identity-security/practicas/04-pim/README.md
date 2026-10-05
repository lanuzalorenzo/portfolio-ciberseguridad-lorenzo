# PIM | Activación temporal de roles
# 04 | Privileged Identity Management (PIM) en Microsoft Entra ID

La práctica documenta el uso de Privileged Identity Management para activar un rol elegible durante un periodo limitado y revisar su trazabilidad.
## Descripción del escenario y objetivo de seguridad

## Procedimiento
**Escenario:** Cuentas de administración con asignaciones permanentes de altos privilegios (ej. Global Administrator, Security Admin), creando un riesgo severo de compromiso continuo y persistencia de atacantes.  
**Objetivo de seguridad:** Implementar el principio de acceso Just-in-Time (JIT) y Zero Standing Privileges (ZSP) mediante Microsoft Entra Privileged Identity Management (PIM), exigiendo activación bajo demanda, justificación y verificación MFA.  
**Alcance:** Roles de Microsoft Entra en tenant de laboratorio y políticas de asignación elegible (*Eligible*).

1. Revisar las asignaciones elegibles en Microsoft Entra roles.
2. Activar Global Reader indicando justificación, duración y verificación MFA.
3. Comprobar el estado activo y desactivar el rol.
4. Revisar el retorno a estado elegible y los eventos de auditoría.
> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Informe técnico
## Arquitectura y componentes de Azure utilizados

[Configuración y validación de PIM](docs/informe-tecnico.md)
| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra PIM** | Gobernanza de identidades privilegiadas | Gestión de asignaciones de roles elegibles y activas. |
| **Rol Global Reader** | Rol objeto de laboratorio | Configurado como asignación elegible (*Eligible*) para el usuario de prueba. |
| **Flujo de Activación JIT** | Puerta de enlace temporal de privilegios | Exige verificación MFA, justificación textual y duración limitada. |
| **Resource Audit de PIM** | Trazabilidad y no repudio | Registro cronológico inmutable de activaciones, desactivaciones y expiraciones. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Privilegios permanentes cero (Zero Standing Access) | Asignación en modo *Eligible* en lugar de *Active* permanente | Política de PIM en Entra ID | MCSB PA-1 / PA-3 |
| Elevación protegida con MFA | Requisito obligatorio de MFA durante el flujo de activación | Configuración de directiva de rol en PIM | MCSB PA-2 |
| Trazabilidad y auditoría de elevaciones | Registro de motivo, usuario y ventana temporal | Panel *Resource audit* de PIM | MCSB LT-1 |

**Artefactos relacionados:** [Configuración y validación de PIM](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Comprobación de estado inicial sin privilegios | Login e inspección de roles en Azure Portal | Usuario no cuenta con permisos administrativos activos | PASS: Asignación figura en modo *Eligible* únicamente |
| Intento de activación de rol sin justificación | Flujo de elevación en panel *My Roles* | El sistema bloquea el avance si falta justificación o MFA | PASS: Requisito de justificación y MFA obligatorio |
| Activación temporal JIT y verificación de expiración | Activación completada y comprobación de vigencia | El rol pasa a *Active* temporalmente y retorna a *Eligible* al finalizar | PASS: Elevación temporal correcta con evento registrado en auditoría |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **PA-1: Protección de cuentas privilegiadas** | Eliminación de administradores permanentes | Reducir el tiempo de exposición de privilegios mitiga drásticamente el impacto de credenciales robadas. |
| **PA-3: Gestión del ciclo de vida de privilegios** | Revisiones periódicas y asignaciones temporales | PIM debe complementarse con revisiones de acceso (*Access Reviews*) para retirar elegibilidades inactivas. |

- La gestión de PIM en producción requiere licenciamiento Microsoft Entra ID P2 o Microsoft Entra ID Governance.
- Es vital mantener al menos dos cuentas de emergencia de acceso interrumpido (*Break-Glass Accounts*) con asignación permanente y exclusiones explícitas de PIM y Acceso Condicional, fuertemente monitorizadas.
