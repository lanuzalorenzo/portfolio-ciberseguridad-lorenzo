# 11 | Defender for DevOps

## Descripción del escenario y objetivo de seguridad

**Escenario:** Ciclo de vida de software con repositorios y pipelines conectados sin análisis continuo de IaC, secretos o dependencias, incrementando el riesgo de fuga de credenciales y componentes vulnerables.
**Objetivo de seguridad:** Integrar repositorios y pipelines en Defender for DevOps para evaluar IaC, secretos expuestos y vulnerabilidades del software antes de la entrega continua.
**Alcance:** Repositorios de laboratorio, pipelines, plantillas de infraestructura y análisis de seguridad sobre componentes y artefactos generados.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Defender utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for DevOps** | Seguridad en repositorios y pipelines | Integración con GitHub/Azure DevOps. |
| **Análisis de IaC** | Escaneo de Terraform, Bicep o ARM | Detección de configuración insegura. |
| **Detección de secretos** | Identificación de tokens y credenciales | Escaneo del repositorio. |
| **Dependencias y artefactos** | Revisión de vulnerabilidades y librerías | Análisis de cadena de suministro. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Análisis de IaC | Revisar plantillas de infraestructura | Escaneo de seguridad en CI/CD | MCSB DS-1 |
| Detección de secretos | Búsqueda de credenciales expuestas | Validación previa a commit o despliegue | MCSB IM-1 |
| Seguridad de dependencias | Revisión de paquetes vulnerables | Alertas de riesgo y remediación | MCSB PV-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Escaneo de IaC | Revisión de plantillas de infraestructura | Hallazgos de riesgo visibles | Correcto |
| Secret scanning | Validación de credenciales en repositorio | Alertas de riesgo si existen secretos | Sí |
| Evaluación de dependencias | Análisis de paquetes y librerías | Vulnerabilidades priorizadas | Sí |
