# 10 | Defender App Governance

## Descripción del escenario y objetivo de seguridad

**Escenario:** Aplicaciones OAuth y conectores del entorno de Microsoft 365 con permisos amplios y poca visibilidad de comportamiento, incrementando el riesgo de abuso de accesos y fuga de datos.
**Objetivo de seguridad:** Evaluar permisos, comportamientos y riesgos de aplicaciones mediante Defender App Governance para reforzar la gobernanza y detectar actividades sospechosas.
**Alcance:** Aplicaciones conectadas a Microsoft 365, permisos consentidos, análisis de riesgos y validación de alertas sobre actividades anómalas.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender App Governance** | Gobernanza de aplicaciones y permisos | Visibilidad de aplicaciones conectadas. |
| **OAuth / permisos** | Evaluación de accesos y consentimiento | Determinación de privilegios excesivos. |
| **Alertas de riesgo** | Señales de actividad sospechosa | Detección de uso anómalo. |
| **Conectores y datos** | Revisión del acceso a información sensible | Análisis de riesgo y comportamiento. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Gobernanza de permisos | Identificación de aplicaciones con accesos excesivos | Revisión continua de consentimientos | MCSB AM-2 |
| Detección de anomalías | Monitorización de utilización inusual de apps | Alertas por riesgo | MCSB IR-2 |
| Reducción de superficie | Revocación o ajuste de permisos | Respuesta operativa | MCSB IA-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Revisar permisos | Inspección de apps registradas | Riesgos de exceso de privilegios visibles | Correcto |
| Verificar alertas | Revisión del panel de seguridad | Incidentes o señales identificadas | Sí |
| Validar comportamiento | Análisis de actividad anómala | Evidencia de riesgo documentada | Sí |
