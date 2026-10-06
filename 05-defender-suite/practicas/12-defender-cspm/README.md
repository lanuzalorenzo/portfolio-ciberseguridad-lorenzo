# 12 | Defender CSPM (Cloud Security Posture Management)

## Descripción del escenario y objetivo de seguridad

**Escenario:** Suscripción de laboratorio con recursos cloud expuestos sin evaluación continua de postura, generando riesgos de configuración, cumplimiento y visibilidad de seguridad.
**Objetivo de seguridad:** Revisar la postura de seguridad cloud mediante Defender CSPM para identificar recomendaciones, evaluación de riesgo y desviaciones de configuración.
**Alcance:** Recursos de Azure del laboratorio, cumplimiento frente al benchmark, recomendaciones priorizadas y validación de las principales desviaciones de seguridad.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender CSPM** | Evaluación continua de postura cloud | Analítica de configuración y riesgos. |
| **Secure Score / recomendaciones** | Priorización del esfuerzo de remediación | Recomendaciones con impacto calculado. |
| **Benchmark de seguridad** | Comparación con estándares de referencia | MCSB y mejores prácticas. |
| **Exposición y cumplimiento** | Riesgos y desviaciones de políticas | Integración con continuidad de seguridad. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Evaluación de Postura | Análisis de riesgos y configuraciones | Sensores de CSPM continuos | MCSB GS-2 |
| Priorización de recomendaciones | Ordenación por impacto y esfuerzo | Secure Score y remediación guiada | MCSB GS-1 |
| Cumplimiento y hardening | Revisión de desviaciones regulatorias | Políticas y mejores prácticas | MCSB DP-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Revisión de posture | Análisis del panel de Defender CSPM | Riesgos y configuraciones visibles | Correcto |
| Secure Score | Evaluación del score actual | Valor con contexto de mejora | Correcto |
| Prioridad de remediación | Comparación de recomendaciones | Impacto y esfuerzo bien definidos | Sí |
