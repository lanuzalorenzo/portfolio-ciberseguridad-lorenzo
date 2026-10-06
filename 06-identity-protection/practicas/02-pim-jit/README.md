# 02 | PIM y acceso Just-In-Time

## Descripción del escenario y objetivo de seguridad

**Escenario:** Usuarios con roles administrativos o de alto impacto que conservan permisos permanentes durante largos periodos, aumentando la superficie de riesgo ante abuso de credenciales, sesiones comprometidas o errores de configuración.  
**Objetivo de seguridad:** Reducir la exposición de privilegios mediante la activación temporal y justificada de permisos altos, con validación y trazabilidad.  
**Alcance:** Microsoft Entra ID, PIM, roles asignados, activaciones JIT, revisión de accesos y evidencia de justificación.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Entra ID utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra ID PIM** | Elevación temporal de permisos | Activación bajo demanda y con requisitos. |
| **Roles privilegiados** | Permisos de administración crítica | Roles con acceso sensible a recursos. |
| **Justificación y aprobación** | Validación de necesidad temporal | Control del acceso basado en la necesidad de negocio. |
| **Revisión periódica** | Auditoría de permisos activos | Eliminar roles innecesarios. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Elevación temporal | Activación de roles solo cuando se requiere | Políticas de PIM | MCSB IA-2 |
| Revisión de justificación | Solicitud con motivo y aprobación | Workflow de aprobación | MCSB GS-2 |
| Mínimo privilegio | Roles asignados solo en el tiempo necesario | Governance de acceso | MCSB IA-3 |
| Auditoría de accesos | Registro de activaciones y duración | Compliance y evidencia | MCSB IR-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Activación temporal de rol | Solicitud y activación de acceso | El usuario obtiene permisos solo por el periodo necesario | Sí |
| Revisión de aprobaciones | Validación del proceso de activación | Solicitud con justificación y aprobación | Sí |
| Revocación del rol | Finalización del periodo de activación | Permisos revocados automáticamente | Sí |
