# 02 | Defender for Endpoint

## Descripción del escenario y objetivo de seguridad

**Escenario:** Dispositivos del laboratorio sin onboarding activo en Microsoft Defender for Endpoint, con telemetría incompleta y riesgo de exposición no detectada ante malware, ejecución remota y movimiento lateral.
**Objetivo de seguridad:** Habilitar el onboarding de endpoints, validar la ingestión de telemetría y confirmar la detección temprana de comportamiento sospechoso mediante EDR.
**Alcance:** Equipos Windows/Linux del laboratorio, registros de actividad del endpoint y validación de alertas de seguridad generadas por el motor de detección.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for Endpoint** | EDR y protección de endpoints | Onboarding del dispositivo y validación del estado activo. |
| **Agente de seguridad** | Recolección de eventos y procesos | Instalado en el endpoint del laboratorio. |
| **Threat analytics / alertas** | Detección y respuesta ante comportamientos anómalos | Revisado desde el portal de Microsoft Defender. |
| **Attack surface reduction** | Reducción de superficie de ataque | Evaluación de controles de seguridad del endpoint. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Onboarding de endpoints | Instalación del agente y validación del estado "Active" | Script de incorporación del portal | MCSB EP-1 |
| Telemetría y visibilidad | Supervisión de procesos, conexiones y actividad | Monitorización continua del motor EDR | MCSB EP-2 |
| Detección de comportamiento | Alertas de actividad sospechosa y técnicas ATT&CK | Motores de análisis del EDR | MCSB IR-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Estado del dispositivo | Consulta del portal de Defender for Endpoint | Dispositivo visible y operativo | Correcto |
| Ingestión de telemetría | Revisar actividad y eventos del endpoint | Datos actualizados y consistentes | Correcto |
| Análisis de alertas | Revisión de incidentes activos | Incidentes con contexto y severidad | Sí |
