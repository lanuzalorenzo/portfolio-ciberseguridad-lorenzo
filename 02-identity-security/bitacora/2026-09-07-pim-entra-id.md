# Bitácora — 2026-09-07 — Privileged Identity Management (PIM)
# Bitácora — 2026-09-07: Análisis y Simulación de PIM en Entra ID

## Trabajo realizado
- Acceso al portal de Microsoft Entra ID.
- Revisión de la sección **Identity Governance**.
- Entrada en **Privileged Identity Management (PIM)**.
- Exploración de los paneles principales:
  - **Assignments** (asignaciones activas y elegibles)
  - **My roles** (roles disponibles para activación)
  - **Resource audit** (registro de eventos y trazabilidad)
  - **Alerts** (recomendaciones y avisos del sistema)
  - **Settings** (configuración del comportamiento de PIM)
- Revisión de los tipos de asignación:
  - **Eligible** (requiere activación temporal)
  - **Active** (rol actualmente en uso)
- Identificación de los requisitos de activación:
  - MFA obligatorio
  - Motivo de activación
  - Duración limitada
  - Justificación para roles sensibles
**Módulo:** 02 — Identity Security  
**Práctica:** 04 — Privileged Identity Management (PIM)

## Resultados y validaciones
- PIM estructura claramente los flujos de activación temporal, reduciendo la exposición a permisos permanentes.
- La auditoría de recursos ofrece trazabilidad completa de activaciones, desactivaciones y cambios.
- La interfaz moderna oculta parte de la navegación clásica, pero mantiene la lógica de roles y auditoría.
- Sin licencia P2 no se pueden activar roles, pero sí estudiar la estructura y los flujos.
Jornada dedicada a explorar y documentar el funcionamiento de **Privileged Identity Management (PIM)** en la sección de *Identity Governance* de Microsoft Entra ID.

## Aprendizaje clave
- Diferencias entre **Eligible** y **Active**.
- Funcionamiento de la activación temporal de roles privilegiados.
- Integración de MFA y justificación dentro del flujo de activación.
- Revisión de auditoría y eventos registrados por PIM.
- Configuraciones avanzadas: alertas, revisiones de acceso, caducidad, etc.
El objetivo fue analizar cómo eliminar los privilegios permanentes (*Standing Access*) y estructurar la concesión de permisos bajo demanda (*Just-in-Time*). Inspeccioné los paneles clave de PIM: *Assignments*, *My roles*, *Alerts* y *Resource audit*.

## Siguiente paso
- Documentar la práctica completa en el portfolio.
- Integrar PIM dentro del módulo 02 de Identity Security.
- Preparar validaciones reales cuando se disponga de licencia P2.
Configuré una asignación en modo **Eligible** para el rol *Global Reader*. Al simular el flujo de activación desde el punto de vista del operador, comprobé los controles que impone la directiva:
1. Requisito ineludible de verificar un factor MFA antes de elevar privilegios.
2. Obligación de indicar un motivo o justificación técnica por escrito.
3. Ventana temporal limitada (2 horas en mi configuración).

Comprobé además el panel de trazabilidad (*Resource audit*), donde queda constancia exacta de la identidad, hora de elevación y justificación aportada. Como apunte técnico importante: para la activación efectiva en producción se requiere licencia Entra ID P2; sin embargo, simular y mapear el flujo de gobierno permite comprender la arquitectura de mínimo privilegio temporal recomendada por Microsoft.
