# 03 | SAST, SCA e IaC scanning

## Descripción del escenario y objetivo de seguridad

**Escenario:** Proyecto software con dependencias de terceros, infraestructura declarativa y lógica de aplicación que no se validan de forma automatizada antes de integrarse. Esto incrementa el riesgo de introducir vulnerabilidades conocidas, defectos de seguridad y configuraciones inseguras.  
**Objetivo de seguridad:** Automatizar la validación del código, dependencias y plantillas de infraestructura mediante análisis estático antes de la entrega.  
**Alcance:** Código fuente, dependencias, plantillas de infraestructura (Terraform, Bicep, ARM o similares) y validación previa a la integración.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de seguridad considerados

| Componente | Función | Configuración relevante |
|---|---|---|
| **SAST** | Análisis estático del código fuente | Detección de vulnerabilidades en lógica y flujo. |
| **SCA** | Revisión de dependencias y paquetes | Identificación de librerías vulnerables. |
| **IaC scanning** | Validación de plantillas de infraestructura | Detección de configuración insegura. |
| **Pipeline de validación** | Ejecución automatizada de análisis | Gating previo al merge o despliegue. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Análisis estático del código | Identificación de patrones inseguros | Ejecución en PR y CI | MCSB PV-2 |
| Escaneo de dependencias | Revisión de librerías o paquetes vulnerables | SCA en pipeline | MCSB PV-3 |
| Validación de infraestructura | Revisión de IaC con referencia normativa | Escaneo en PRs y despliegues | MCSB DS-1 |
| Bloqueo por hallazgos críticos | Rechazo del cambio en CI si supera umbral | Gates de seguridad | MCSB IR-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| SAST en cambio crítico | Análisis de código con riesgo latente | Hallazgos identificados | Sí |
| SCA de dependencias | Revisar paquetes vulnerables | Alertas priorizadas por severidad | Sí |
| IaC scanning | Validación de plantillas | Configuraciones inseguras detectadas | Sí |
