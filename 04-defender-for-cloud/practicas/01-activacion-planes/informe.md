# Informe técnico — Activación de Planes de Microsoft Defender for Cloud

**Módulo:** 04 — Defender for Cloud
**Práctica:** 01 — Activación de planes (CSPM y CWPP)

## Contexto y Objetivo
Microsoft Defender for Cloud opera en dos dimensiones complementarias: la gestión de la postura de seguridad cloud (*Cloud Security Posture Management* o CSPM) y la protección de cargas de trabajo (*Cloud Workload Protection Platform* o CWPP). Ambas dimensiones se habilitan y configuran mediante la selección de planes desde el panel *Environment settings*.

Esta práctica documenta la evaluación del catálogo de planes disponibles, las decisiones de activación tomadas conforme al perfil de riesgo y coste del laboratorio, y la verificación del impacto inmediato en la visibilidad de seguridad.

## Catálogo de Planes Evaluados

| Plan | Dimensión | Coste | Capacidades Clave | Decisión de Laboratorio |
| :--- | :--- | :--- | :--- | :--- |
| **Foundational CSPM** | CSPM | Gratuito | Secure Score, inventario básico, recomendaciones MCSB | Activado por defecto |
| **Defender CSPM** | CSPM | De pago (por recurso) | Attack Path Analysis, Cloud Security Explorer, gobernanza, exposición a Internet | Evaluado; no activado por coste |
| **Defender for Servers Plan 1** | CWPP (VM) | De pago (por servidor/hora) | Integración con MDE, JIT, evaluación de configuraciones OS | Activado para evaluación |
| **Defender for Servers Plan 2** | CWPP (VM) | De pago | Todo Plan 1 + MDVM, monitoreo FIM, 500 MB de ingestión gratuita | Evaluado; capacidades documentadas |
| **Defender for Storage** | CWPP (Storage) | De pago (por cuenta) | Detección de malware en blobs, alertas de acceso anómalo | Evaluado; no activado |

## Configuración y Aprovisionamiento

1. **Acceso al panel de planes:** *Microsoft Defender for Cloud* → *Environment settings* → suscripción de laboratorio.
2. **Activación del plan:** *Defender for Servers Plan 1* habilitado desde el panel de planes.
3. **Aprovisionamiento automático:** Verificación de que la extensión de Microsoft Defender for Endpoint (MDE) está configurada para instalarse automáticamente en las VMs mediante la directiva del plan.
4. **Impacto en el Secure Score:** Tras la activación, el panel de recomendaciones actualizó su catálogo incorporando controles de protección de endpoints y configuración de sistemas operativos.

## Verificación del Estado de Planes

| Plan / Componente | Estado Verificado | Método de Verificación |
| :--- | :--- | :--- |
| Foundational CSPM | Activo | Panel *Environment settings* — estado *On* |
| Defender for Servers Plan 1 | Activo | Panel *Environment settings* — estado *On* |
| Extensión MDE en VM de prueba | Instalada | Inspección de extensiones de la VM en el portal de Azure |

## Conclusiones Técnicas
- La activación de Defender for Servers Plan 1 es la forma más directa de obtener cobertura EDR sobre VMs en Azure sin requerir onboarding manual de máquinas en el portal de Microsoft 365 Defender.
- El nivel gratuito Foundational CSPM proporciona un valor significativo sin coste: Secure Score completo, recomendaciones alineadas con MCSB y visibilidad de inventario de recursos.
- Defender CSPM de pago es especialmente relevante en entornos con múltiples nubes o cuando se requiere análisis de rutas de ataque (*Attack Path Analysis*) para priorizar remediaciones de forma más sofisticada que el análisis lineal del Secure Score.
