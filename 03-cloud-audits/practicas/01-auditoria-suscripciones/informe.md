# Informe técnico — Auditoría de Seguridad en Suscripciones Azure

**Módulo:** 03 — Auditorías Cloud  
**Práctica:** 01 — Auditoría de Suscripciones

## Contexto y Alcance de la Auditoría
La gobernanza a nivel de suscripción es el pilar central del modelo de seguridad en Azure. Un plano de control descuidado o con asignaciones excesivas a nivel de raíz debilita cualquier control defensivo implementado en los recursos individuales.

Esta práctica documenta la evaluación de seguridad de una suscripción de laboratorio en Azure, analizando la postura global (Secure Score), la coherencia de directivas de Azure Policy y las asignaciones de control de acceso (RBAC) en el ámbito de suscripción.

## Metodología y Herramientas Utilizadas
Para realizar la auditoría se combinaron tres mecanismos complementarios:
1. **Microsoft Defender for Cloud (CSPM):** Análisis de recomendaciones y puntuación de postura (*Secure Score*) mapeada con la iniciativa Microsoft Cloud Security Benchmark (MCSB).
2. **Azure Policy:** Verificación del estado de cumplimiento de directivas de auditoría y denegación asignadas en la suscripción.
3. **Azure Resource Graph (KQL):** Consultas directas sobre el inventario para identificar recursos huérfanos o fuera de estándar.

## Matriz de Hallazgos de Seguridad

| ID Hallazgo | Severidad | Control / Área | Descripción del Hallazgo | Riesgo Asociado | Recomendación de Remediación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SEC-SUB-01** | **Alta** | IAM / RBAC | Asignaciones del rol *Owner* realizadas directamente a identidades de usuario individuales en el ámbito de suscripción. | Escalada de privilegios y dificultad de revocación ante rotación de personal; falta de gobernanza centralizada. | Reemplazar asignaciones directas por asignaciones a grupos de seguridad y configurar el rol como elegible a través de Privileged Identity Management (PIM). |
| **SEC-SUB-02** | **Media** | Azure Policy | Ausencia de directiva de auditoría obligatoria para el registro de actividad de diagnóstico (*Diagnostic Settings*) hacia Log Analytics. | Pérdida de visibilidad forense ante incidentes de seguridad y falta de centralización de logs en SIEM. | Asignar la iniciativa integrada de Azure Policy para forzar el streaming de logs de diagnóstico a un workspace de Log Analytics central. |
| **SEC-SUB-03** | **Baja** | Tags / Gobernanza | Recursos desplegados en la suscripción sin etiquetas obligatorias de propiedad, entorno (*Environment*) y criticidad. | Dificultad para priorizar incidentes de seguridad y determinar responsables de activos en el inventario. | Desplegar directiva de Azure Policy que exija etiquetas mínimas en la creación de recursos (*Require a tag on resources*). |

## Evaluación de Postura y Secure Score
- Se evaluó el panel de recomendaciones de **Microsoft Defender for Cloud**.
- Las principales deducciones de puntos en el Secure Score provinieron de recursos con puertos de administración abiertos sin protección Just-in-Time (JIT) y almacenamiento sin forzado de TLS 1.2.
- Se trazó un plan de remediación priorizando los controles con mayor impacto cuantitativo en la reducción del riesgo.

## Lecciones Aprendidas y Conclusiones
- Las auditorías a nivel de suscripción deben ejecutarse periódicamente, ya que el despliegue dinámico de nuevos recursos suele degradar la postura si no existen directivas de prevención automáticas.
- Adoptar Azure Policy en modo *Deny* para configuraciones críticas es más eficiente que depender exclusivamente de auditorías reactivas.
