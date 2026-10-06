# 04 | Defender XDR

## Descripción del escenario y objetivo de seguridad

**Escenario:** Entorno con señales distribuidas entre identidad, endpoints y correo sin correlación centralizada, generando dificultad para distinguir ataques reales de alertas aisladas.
**Objetivo de seguridad:** Analizar incidentes y correlaciones en Microsoft Defender XDR para reconstruir la cronología de los ataques, prioritizar la respuesta y validar la coordinación entre productos Defender.
**Alcance:** Incidentes del laboratorio, correlación entre identidad, endpoint, correo y aplicaciones, con análisis de entidades y severidad.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender XDR** | Correlación de incidentes entre productos | Vista unificada del ataque. |
| **Defender for Identity** | Señales de anomalías de identidad | Entidades asociadas al ataque. |
| **Defender for Endpoint** | Señales de proceso y endpoint | Evidencia del comportamiento del host. |
| **Defender for Office 365** | Señales de correo y phishing | Alertas y mensajes maliciosos. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Correlación de incidentes | XDR unifica señales de varios productos | Análisis automatizado de cronología | MCSB IR-2 |
| Priorización de urgencia | Valores de severidad y riesgo | Clasificación por impacto | MCSB IR-3 |
| Respuesta operativa | Acciones recomendadas y evidencia asociada | Enriquecimiento del caso de seguridad | MCSB IR-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Revisión de incidentes | Consulta del caso de XDR | Evidencia correlacionada | Correcto |
| Cronología del ataque | Análisis de timeline | Secuencia del ataque visible | Sí |
| Impacto y severidad | Revisión de entidades y contexto | Clasificación consistente | Sí |
