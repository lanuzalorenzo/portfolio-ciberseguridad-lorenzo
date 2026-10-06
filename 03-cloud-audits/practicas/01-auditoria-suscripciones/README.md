# 01 | Auditoría de Seguridad en Suscripciones Azure

## Descripción del escenario y objetivo de seguridad

**Escenario:** Suscripción cloud de laboratorio que aloja múltiples cargas de trabajo, con configuraciones heredadas, políticas dispersas y asignaciones de permisos en el ámbito de suscripción sin inventario formal.  
**Objetivo de seguridad:** Evaluar el estado de seguridad y gobernanza de la suscripción, identificando brechas en la postura global (Secure Score), asignaciones de privilegios amplios y políticas ausentes conforme al Microsoft Cloud Security Benchmark (MCSB).  
**Alcance:** Ámbito de suscripción en Azure Resource Manager (ARM), evaluaciones de Microsoft Defender for Cloud y directivas base de Azure Policy.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Resource Manager (ARM)** | Plano de control y gobernanza | Alcance `/subscriptions/<subscription-id>` para evaluación de permisos y recursos. |
| **Microsoft Defender for Cloud** | Gestión de postura de seguridad (CSPM) | Secure Score habilitado con la iniciativa Microsoft Cloud Security Benchmark. |
| **Azure Policy** | Cumplimiento normativo y directivas | Asignación de iniciativas de seguridad estándar para detección de desviaciones. |
| **Azure Resource Graph** | Inventario y consultas analíticas KQL | Consultas de auditoría rápida sobre recursos desprotegidos y configuraciones globales. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Evaluación continua de postura (CSPM) | Secure Score en Defender for Cloud | Iniciativa regulatoria MCSB | MCSB GS-1 / CIS Azure 2.0 |
| Auditoría de asignaciones RBAC a nivel root | Revisión de roles *Owner* y *Contributor* en suscripción | Consultas de inventario en IAM | MCSB PA-1 / PA-3 |
| Detección de recursos no conformes | Auditoría declarativa de configuraciones básicas | Azure Policy (`Audit` mode) | MCSB GS-2 |

**Artefactos relacionados:** [Informe de auditoría](docs/auditoria-suscripciones-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Revisión de asignaciones *Owner* permanentes | Inspección de IAM en suscripción | Máximo 2-3 identidades con justificación formal | PASS: Se detectaron asignaciones directas a usuarios; se propuso migración a PIM/grupos |
| Estado de cumplimiento de Secure Score | Panel de Defender for Cloud | Identificación de recomendaciones críticas de seguridad | PASS: Score evaluado con foco en remediación de red y cifrado |
| Comprobación de políticas obligatorias activas | Evaluación de cumplimiento en Azure Policy | Iniciativa MCSB en estado de auditoría asignada | PASS: Detección de recursos sin diagnósticos habilitados |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **GS-1: Asignar responsabilidades de seguridad** | Auditoría y seguimiento del Secure Score | La postura no es estática; las recomendaciones de Defender for Cloud deben integrarse en rutinas periódicas de revisión. |
| **PA-1: Minimizar privilegios a nivel de suscripción** | Restricción de ámbito a Resource Groups | Asignar roles a nivel de suscripción amplía excesivamente el radio de explosión ante cualquier identidad vulnerada. |

- Azure Resource Graph es el mecanismo más rápido y escalable para auditar el cumplimiento de propiedades de recursos sin depender de la navegación manual por el portal.
