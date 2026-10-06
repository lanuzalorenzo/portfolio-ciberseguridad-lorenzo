# 08 | Defender External Attack Surface Management (EASM)

## Descripción del escenario y objetivo de seguridad

**Escenario:** Organización con activos externos no gestionados o parcialmente conocidos, incluyendo dominios, subdominios, servicios públicos y tecnologías expuestas sin visibilidad centralizada.
**Objetivo de seguridad:** Descubrir, mapear y priorizar la superficie de ataque externa para detectar exposiciones, configuraciones inseguras y riesgos asociados a activos públicos.
**Alcance:** Dominios del laboratorio, servicios web y entidades públicas visibles en Internet, así como riesgos de exposición y oportunidades de remediación.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender EASM** | Descubrimiento de activos expuestos | Mapado de dominios, subdominios e IPs. |
| **Superficie de ataque externa** | Inventario de activos públicos | Evaluación continua del entorno visible. |
| **Tecnologías detectadas** | Identificación de stacks y versiones | Riesgo asociado a mantenimiento. |
| **Exposición y vulnerabilidades** | Riesgo y hallazgos asociados | Priorización de remediación. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Descubrimiento de activos externos | Escaneo inicial de superficie y dominios | Recolección continua de activos | MCSB GS-1 |
| Priorización de exposiciones | Clasificación por riesgo y exposición | Base de urgencia para remediación | MCSB RM-1 |
| Evaluación de configuración | Detección de servicios y tecnologías públicas | Riesgos derivados de versiones y servicios | MCSB PV-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Descubrimiento de activos | Escaneo inicial de EASM | Lista de dominios y servicios visibles | Correcto |
| Análisis de riesgos | Revisión de tecnologías y vulnerabilidades | Riesgos identificados por prioridad | Correcto |
| Validación de exposición | Comprobación de activos externos | Mayor visibilidad del perímetro | Sí |
