# 14 | Simulación controlada y correlación en Defender XDR

## Descripción del escenario y objetivo de seguridad

**Escenario:** Entorno de laboratorio con una cadena de ataque controlada diseñada para validar la detección, correlación y respuesta de varios productos de Microsoft Defender.
**Objetivo de seguridad:** Ejecutar una simulación de ataque y confirmar que la suite de Microsoft Defender es capaz de correlacionar señales de identidad, endpoint, correo y cloud en un único caso de respuesta.
**Alcance:** Laboratorio con escenarios de phishing, malware, abuso de credenciales o movimiento lateral, con análisis de impacto y modelado de respuesta.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender XDR** | Correlación de señales y cronología del ataque | Caso de incidente central. |
| **Defender for Endpoint** | Evidencia de ejecución y procesos | Detección de malware y comportamiento. |
| **Defender for Identity** | Señales de autenticación anómala | Riesgo de acceso y movimiento lateral. |
| **Defender for Cloud Apps / otros** | Contexto de apps y acceso | Integración con actividad cloud. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Simulación de técnica adversaria | Ejecución controlada del escenario | Validación planificada en laboratorio | MCSB IR-2 |
| Correlación entre señales | Análisis de timeline y entidades | Caso único en XDR | MCSB IR-1 |
| Priorización y respuesta | Revisión del impacto y posible mitigación | Respuesta manual o automatizada | MCSB IR-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Simulación de ataque | Ejecución del escenario de laboratorio | Evidencia generada y detectada | Correcto |
| Correlación de señales | Revisión de timeline de XDR | Ataque completo reconstruido | Correcto |
| Respuesta operativa | Validación de acciones y mitigaciones | Caso con respuesta adecuada | Sí |

## Alcance

El escenario se plantea como una práctica controlada de laboratorio y no como actividad contra sistemas externos.
