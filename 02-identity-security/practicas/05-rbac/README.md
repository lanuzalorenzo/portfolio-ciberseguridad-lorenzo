# 05 | Control de Acceso Basado en Roles (RBAC) en Azure

## Descripción del escenario y objetivo de seguridad

**Escenario:** Asignaciones de privilegios amplios y descontrolados a nivel de suscripción que permiten a operadores y auditores modificar configuraciones críticas o redes sin necesidad funcional.  
**Objetivo de seguridad:** Diseñar e implementar una matriz de control de acceso basada en roles (RBAC) que aplique separación de funciones (SoD) y mínimo privilegio sobre recursos de Azure.  
**Alcance:** Ámbito de Resource Group en Azure Resource Manager (ARM), roles integrados de Azure y grupos de seguridad de Entra ID.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Resource Manager (ARM)** | Plano de control de Azure | Gestión declarativa de autorizaciones y asignaciones de roles. |
| **Rol Security Admin** | Perfil SecOps | Permisos de lectura de configuraciones de seguridad y gestión de directivas. |
| **Rol Virtual Machine Contributor** | Perfil de Operaciones | Capacidad de gestión sobre el ciclo de vida de VMs sin permisos sobre la red o seguridad. |
| **Rol Security Reader** | Perfil de Auditoría | Visibilidad de estado de cumplimiento y alertas sin permisos de alteración ni borrado. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Principio de mínimo privilegio | Restricción de permisos al Resource Group del proyecto | Asignaciones RBAC en ARM | MCSB PA-1 |
| Separación de funciones (SoD) | Roles diferenciados para operaciones, seguridad y auditoría | Matriz RBAC definida | MCSB PA-7 |
| Aislamiento de plano de control y datos | Asignación de roles sin permisos implícitos sobre datos | RBAC granular en Azure | NIST SP 800-53 AC-6 |

**Artefactos relacionados:** [Diseño y validación del modelo RBAC](docs/rbac-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Modificación de NSG con rol *VM Contributor* | Intento de cambio en reglas de red | Error 403 Forbidden por falta de permisos en `Microsoft.Network` | PASS: Operación denegada por control RBAC |
| Reinicio de servicio con rol *Security Reader* | Petición de reinicio o parada de recurso | Acceso denegado (solo lectura habilitada) | PASS: Acción no autorizada para el auditor |
| Intento de delegación de permisos a terceros | Ejecución de asignación de roles con cuenta operador | Bloqueo por falta de permiso `roleAssignments/write` | PASS: Elevación de privilegios no autorizada impedida |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **PA-1: Mínimo privilegio en el plano de control** | Delimitación estricta a Resource Group | Asignar roles a nivel de Resource Group en lugar de Suscripción reduce el radio de impacto ante cuentas comprometidas. |
| **PA-7: Separación de funciones** | Desacoplar administración de infraestructura de seguridad | Evita conflictos de interés y asegura que quien despliega infraestructura no audite sus propias configuraciones. |

- Asignar roles a grupos de seguridad de Entra ID en lugar de a usuarios individuales facilita la gobernanza y previene permisos residuales tras la salida de personal.
