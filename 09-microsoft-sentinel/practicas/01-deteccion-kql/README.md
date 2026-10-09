# 01 | Detección con KQL y análisis de alertas

## Descripción del escenario y objetivo de seguridad

**Escenario:** Un entorno con actividad de identidad, accesos y eventos de recursos donde se necesita distinguir comportamientos normales de actividades con riesgo. El escenario es un diseño orientativo para un laboratorio y no representa una operación real en producción.
**Objetivo de seguridad:** Identificar anomalías, eventos sospechosos y patrones de riesgo mediante consultas KQL y correlación de señales.
**Alcance:** Microsoft Sentinel, conectores, consulta de registros y análisis de incidentes sobre eventos relevantes del entorno.

> [!NOTE]
> Práctica propuesta para un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| Microsoft Sentinel | Plataforma SIEM/SOAR de detección y respuesta | Supervisión de eventos, alertas e incidentes. |
| Log Analytics / workspace | Almacenamiento central de eventos | Fuente de la consulta KQL. |
| Conectores | Integración de datos de origen | Azure, Entra ID, Defender y recursos relevantes. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Detección de actividades sospechosas | Consultas KQL enfocadas a anomalías y patrones de riesgo | Consulta y detección de eventos | Microsoft Sentinel analytics |
| Correlación de eventos | Vincular señales con identidad, acceso y recursos | Incidentes en Sentinel | Seguridad operativa |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Consulta de acceso anómalo | Ejecución de consulta KQL sobre eventos seleccionados | Resultado útil y trazable | Pendiente: no ejecutado en laboratorio. |
| Alertas relevantes | Validación de detección y filtrado | Alertas con contexto suficiente | Pendiente: no ejecutado en laboratorio. |

> [!WARNING]
> No declarar una prueba superada si no se ejecutó. Redactar datos sensibles.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| Pendiente de verificar contra la versión vigente | Correlación de datos y detección de riesgo | El valor real de Sentinel requiere contextos de identidad, red y endpoint. |

- Asegurar que cada query tenga un propósito claro y un uso de investigación o detección bien definido.
- Documentar el mecanismo de alertado antes de generalizar la detección.
