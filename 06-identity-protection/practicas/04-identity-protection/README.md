# 04 | Identity Protection y revisiones de acceso

## Descripción del escenario y objetivo de seguridad

**Escenario:** Entorno con riesgo de identidad asociado a accesos sospechosos, credenciales comprometidas y usuarios con permisos antiguos o no revisados.  
**Objetivo de seguridad:** Detectar riesgos de identidad, revisar permisos y activar políticas de mitigación para proteger la operación y la postura de seguridad del tenant.  
**Alcance:** Microsoft Entra ID, Identity Protection, revisiones de acceso, riesgo de sesión y gobernanza del acceso privilegiado.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Entra ID utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Identity Protection** | Evaluación continua del riesgo de identidad | Detección de acceso sospechoso o credenciales comprometidas. |
| **Access reviews** | Revisión periódica de accesos | Validación de roles y permisos activos. |
| **Riesgo de usuario y sesión** | Clasificación de riesgo | Diagnóstico de señales maliciosas o anómalas. |
| **Políticas de mitigación** | Respuesta automática ante riesgo | Rechazo, MFA o bloqueo según el riesgo. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Evaluación de riesgo | Identity Protection analizando sign-ins y actividades | Revisión automática del riesgo | MCSB IA-1 |
| Revisión de acceso | Access reviews sobre permisos críticos | Periodicidad definida | MCSB GS-2 |
| Mitigación automática | MFA, bloqueo o desafío ante riesgo alto | Políticas de respuesta | MCSB IR-2 |
| Gobernanza de privilegios | Eliminación de roles no necesarios | Revisión técnica y operativa | MCSB IA-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Sign-in con riesgo | Simulación del escenario de riesgo | Se detecta y activa mitigación | Sí |
| Review de accesos | Análisis de roles activos | Permisos no necesarios visibles | Sí |
| Mitigación automática | Política de riesgo | MFA o bloqueo aplicados | Sí |
