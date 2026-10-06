# Informe técnico — SAST, SCA e IaC scanning

**Módulo:** 07 — DevSecOps y gobernanza del software  
**Práctica:** 03 — SAST, SCA e IaC scanning

## Contexto y objetivo

Muchos riesgos de seguridad no aparecen en tiempo de ejecución, sino durante la construcción del software o la definición de la infraestructura. Un paquete vulnerable, una dependencia puntualmente explotada o una plantilla de infraestructura con permisos excesivos pueden convertirse en un vector de ataque si no se validan antes del despliegue.

Esta práctica documenta cómo el análisis estático del código, la revisión de dependencias y la validación de IaC refuerzan la postura de seguridad de un repositorio y reducen el riesgo de entregar software inseguro.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Detección temprana** | Analizar código antes de integrarlo | Reduce exposición y coste de corrección |
| **Visibilidad de vulnerabilidades** | Conocer dependencias y riesgos del software | Permite priorizar remediación |
| **Hardening de infraestructura** | Detectar misconfiguraciones en IaC | Evita despliegues inseguros |
| **Control de calidad seguro** | Rechazar cambios con riesgos críticos | Mejora la seguridad del entregable |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **SAST** | Ejecutado en PR y CI | Detecta código vulnerable antes del merge |
| **SCA** | Activado para todas las dependencias | Reduce riesgo de paquetes conocidos |
| **IaC scanning** | Obligatorio en plantillas de infraestructura | Detección de riesgos de despliegue |
| **Gates críticos** | Rechazo de hallazgos severos | Previene cambios inseguros |

## Implementación técnica recomendada

1. Integrar SAST en la pipeline de validación.
2. Ejecutar SCA para todas las dependencias del repositorio.
3. Escanear templates de IaC con reglas de seguridad definidas.
4. Priorizar hallazgos por criticidad y alcance.
5. Rechazar cambios que introduzcan riesgos críticos sin corrección.
6. Registrar resultados para auditoría y mejora continua.

## Riesgos mitigados

- Vulnerabilidades conocidas en librerías y paquetes del software.
- Configuraciones inseguras en plantillas de infraestructura.
- Código con malas prácticas o patrones de riesgo.
- Despliegues inseguros por falta de validación previa.

## Conclusión

SAST, SCA e IaC scanning convierten la seguridad en una validación automática del código y la infraestructura, reforzando la confianza en cada entrega del software.
