# 13 | Defender CNAPP (Cloud-Native Application Protection Platform)

## Descripción del escenario y objetivo de seguridad

**Escenario:** Aplicaciones cloud-native con riesgo de exposición en el ciclo de desarrollo y ejecución, incluyendo arquitectura basada en contenedores, IaC e infraestructura temporal.
**Objetivo de seguridad:** Evaluar la protección de workloads cloud-native mediante Defender CNAPP, analizando IaC, contenedores, exposiciones y riesgo asociado en la plataforma.
**Alcance:** Infraestructura cloud-native del laboratorio, análisis de seguridad en IaC, contenedores, workloads y recomendaciones priorizadas.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender CNAPP** | Protección de workloads cloud-native | Visibilidad en IaC y runtime. |
| **Seguridad de contenedores** | Revisión de imágenes y vulnerabilidades | Detección de riesgos de ejecución. |
| **Protección de workloads** | Evaluación del riesgo por aplicación | Exposición y configuración. |
| **Correlación con XDR** | Relación con incidentes y alertas | Contexto extremo para respuesta. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Seguridad de IaC | Análisis de configuración con plantillas | Análisis en pipeline y despliegue | MCSB DS-1 |
| Seguridad de contenedores | Revisión de imágenes, capas y vulnerabilidades | Escaneo y alertas | MCSB PV-2 |
| Protección de workloads | Evaluación de exposición y riesgo | Directrices de hardening | MCSB EP-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escaneo de IaC | Revisión del panel de CNAPP | Riesgos detectados y priorizados | Correcto |
| Evaluación de contenedores | Análisis de imágenes y capas | Vulnerabilidades o riesgos visibles | Correcto |
| Protección de workloads | Verificación de riesgos y exposición | Evidencia con impacto identificado | Sí |
