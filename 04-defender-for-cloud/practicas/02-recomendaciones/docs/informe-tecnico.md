# Informe técnico — Revisión y Remediación de Recomendaciones de Seguridad

**Módulo:** 04 — Defender for Cloud
**Práctica:** 02 — Recomendaciones de Seguridad y Secure Score

## Contexto y Metodología
El panel de recomendaciones de Microsoft Defender for Cloud es el artefacto central del CSPM: agrupa los controles del Microsoft Cloud Security Benchmark evaluados contra los recursos de la suscripción y los presenta ordenados por impacto en el Secure Score.

Esta práctica documenta el análisis y la remediación selectiva de las recomendaciones de mayor deducción de puntos, distinguiendo entre remediaciones automatizables (*Quick Fix*) y aquellas que requieren decisiones de arquitectura o configuración manual.

## Categorías de Recomendaciones Analizadas

| Control de Seguridad | Recomendación | Impacto en Secure Score | Tipo de Remediación |
| :--- | :--- | :--- | :--- |
| **Protección de red perimetral** | Los puertos de administración de VMs deben estar cerrados o protegidos mediante JIT | Alto | Quick Fix: habilitar JIT en el recurso |
| **Cifrado en tránsito** | Las cuentas de almacenamiento deben exigir versión mínima TLS 1.2 | Medio | Manual: modificar propiedad del recurso |
| **Identidad y acceso** | Las suscripciones deben tener habilitada la autenticación multifactor para administradores | Alto | Manual: requiere Security Defaults o Conditional Access en Entra ID |
| **Registro y auditoría** | Los recursos de Azure deben tener configurado el diagnóstico de Activity Log | Medio | Quick Fix: configurar *Diagnostic Settings* desde el panel |

## Proceso de Priorización y Selección
Para priorizar, se aplicaron los siguientes criterios:
1. **Impacto cuantitativo:** Recomendaciones con mayor deducción de puntos del Secure Score.
2. **Facilidad de remediación:** Se priorizaron las remediaciones con *Quick Fix* disponible para maximizar el valor obtenido por el tiempo invertido.
3. **Exclusiones justificadas:** Las recomendaciones que exigen cambios de arquitectura de red (como migrar a Private Endpoints) se documentan como hallazgos pendientes sin falsear su estado.

## Remediaciones Aplicadas

| Recomendación | Acción Realizada | Resultado |
| :--- | :--- | :--- |
| Puertos de administración expuestos en VM | Habilitación de Just-in-Time VM access desde el panel de Defender for Cloud | Recomendación marcada como *Healthy* en el siguiente ciclo de evaluación |
| TLS 1.2 mínimo en Storage Account | Modificación de `minimumTlsVersion = TLS1_2` en la configuración del recurso | Propiedad actualizada y recurso conforme |
| Diagnóstico de Activity Log | Configuración de *Diagnostic Settings* apuntando a Log Analytics workspace | Log de actividad de Azure activo y centralizado |

## Conclusiones Técnicas
- La métrica del Secure Score es útil como indicador de tendencia, pero no debe interpretarse como una puntuación de seguridad absoluta: recursos con configuración conforme según las métricas de MCSB pueden seguir teniendo vectores de riesgo no cubiertos por el benchmark.
- Las recomendaciones de tipo *Quick Fix* son valiosas para correcciones rápidas, pero no sustituyen la comprensión técnica de lo que se está configurando y por qué.
