# Informe técnico — Protección de Workloads (CWPP) con Defender for Cloud

**Módulo:** 04 — Defender for Cloud
**Práctica:** 03 — Protección de Workloads

## Contexto y Objetivo
La protección de cargas de trabajo (*Cloud Workload Protection Platform* o CWPP) en Defender for Cloud extiende la seguridad más allá de la postura estática: proporciona detección de amenazas en tiempo real, integración con tecnologías EDR maduras (Microsoft Defender for Endpoint) y escaneo continuo de vulnerabilidades.

Esta práctica documenta la revisión de las capacidades de CWPP disponibles para los workloads del laboratorio (principalmente VMs), el aprovisionamiento del agente de seguridad y la comprobación del estado de cobertura.

## Componentes y Flujo de Protección

### Defender for Servers + Microsoft Defender for Endpoint (MDE)
La protección de VMs en Azure mediante Defender for Servers funciona en dos capas complementarias:

1. **Capa de plano de control (Defender for Cloud):** Evalúa la configuración del sistema operativo, aplica recomendaciones de hardening y gestiona el aprovisionamiento del agente.
2. **Capa de detección en runtime (MDE):** Recibe la telemetría del endpoint (procesos, conexiones de red, archivos ejecutados) para detectar comportamientos maliciosos, realizar análisis forense y generar alertas de seguridad.

La integración es automática: al activar Defender for Servers Plan 1, Defender for Cloud instala la extensión MDE en las VMs de la suscripción sin necesidad de configuración adicional en el portal de Microsoft 365 Defender.

## Verificación de Cobertura de Workloads

| Tipo de Workload | Plan Cubriendo | Estado de Aprovisionamiento | Capacidad Verificada |
| :--- | :--- | :--- | :--- |
| Máquinas virtuales (VMs) | Defender for Servers Plan 1 | Extensión MDE instalada automáticamente | Telemetría de endpoint activa |
| Azure Storage Accounts | Defender for Storage | No activado (evaluado) | Detección de malware y accesos anómalos — pendiente de activación |

## Revisión de Capacidades por Plan

**Defender for Servers Plan 1 (activado):**
- Integración completa con Microsoft Defender for Endpoint.
- Acceso Just-in-Time (JIT) a puertos de administración.
- Evaluación de configuraciones del sistema operativo contra líneas base de seguridad.

**Defender for Servers Plan 2 (evaluado, no activado):**
- Todo lo de Plan 1 más Microsoft Defender Vulnerability Management (MDVM): escaneo de CVEs en tiempo real, priorización por exploitabilidad y riesgo.
- File Integrity Monitoring (FIM): alertas sobre modificaciones en archivos críticos del sistema operativo.
- 500 MB de datos de Log Analytics incluidos por nodo al día.

## Conclusiones Técnicas
- La decisión de Plan 1 vs. Plan 2 debe basarse en si se requiere la gestión de vulnerabilidades integrada (MDVM): en laboratorios de aprendizaje, Plan 1 proporciona la cobertura EDR fundamental sin el sobrecoste de MDVM.
- La extensión MDE instalada automáticamente puede causar reinicios en algunas VMs con configuraciones específicas; en entornos de producción conviene validar esto en una ventana de mantenimiento antes de habilitar el aprovisionamiento automático masivo.
