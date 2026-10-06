# 03 | RBAC y minimización de privilegios

## Descripción del escenario y objetivo de seguridad

**Escenario:** Entorno con varios grupos y roles de acceso asignados sin un análisis claro del principio de mínimo privilegio, generando permisos innecesarios y superficie de ataque excesiva.  
**Objetivo de seguridad:** Diseñar un modelo de acceso basado en roles con permisos mínimos y justificados, reduciendo el impacto de errores, abuso o acceso no autorizado.  
**Alcance:** Azure RBAC, Microsoft Entra ID, roles de aplicación y recursos gestionados en entorno de laboratorio.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Entra ID y Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure RBAC** | Modelo de permisos para recursos Azure | Asignación por rol y ámbito. |
| **Microsoft Entra ID** | Identidad de usuarios y grupos | Gestión de grupos y permisos. |
| **Grupos de seguridad** | Agregación de permisos | Agrupar usuarios según necesidad operativa. |
| **Ámbitos de alcance** | Definición del nivel de acceso | Subscrición, grupo de recursos o recurso. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Mínimo privilegio | Permisos limitados al alcance necesario | RBAC y documentación de roles | MCSB IA-3 |
| Separación de responsabilidades | Diferentes roles para distintas funciones | Governance de acceso | MCSB GS-2 |
| Revisión de asignaciones | Validación periódica de usuarios y roles | Auditoría operativa | MCSB IR-1 |
| Principio de necesidad | Solo accesos requeridos para la tarea | Control de acceso basado en necesidad | MCSB IA-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Revisar permisos de un usuario | Inspección del rol asignado | Solo permisos mínimos | Sí |
| Validar alcance de acceso | Comprobación de ámbito del rol | Sin acceso excesivo | Sí |
| Auditoría de roles | Revisión de acceso no utilizado | Eliminación de permisos redundantes | Sí |
