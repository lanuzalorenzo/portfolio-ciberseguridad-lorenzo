# Bitácora — 2026-09-14: Inicio de Auditorías Cloud y Revisión de Suscripción

**Módulo:** 03 — Auditorías Cloud  
**Práctica:** 01 — Auditoría de Suscripciones

Hoy he comenzado los trabajos del Módulo 03, orientando el enfoque del portfolio hacia el rol de auditor cloud y evaluador de postura de seguridad.

La primera tarea consistió en inspeccionar la gobernanza global a nivel de suscripción. Entré en Microsoft Defender for Cloud para evaluar el *Secure Score* de la suscripción de laboratorio frente a la iniciativa base del Microsoft Cloud Security Benchmark.

Identifiqué varias áreas de mejora críticas en la gestión del plano de control:
1. Había asignaciones directas del rol *Owner* a usuarios individuales en lugar de grupos de seguridad administrados. Esto rompe la trazabilidad y la gobernanza centralizada.
2. Descubrí que la suscripción carecía de directivas obligatorias de Azure Policy para asegurar que todos los recursos desvíen sus logs de diagnóstico hacia un workspace de Log Analytics.

Documenté ambos hallazgos con severidad Alta y Media respectivamente en la matriz del informe técnico, detallando los pasos de remediación mediante la migración a PIM y el despliegue de políticas de Azure Policy. Mañana profundizaré en la inspección a nivel de servicios PaaS y almacenamiento.
