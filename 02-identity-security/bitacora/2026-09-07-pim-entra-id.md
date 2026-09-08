# 🗒️ Bitácora — 2026-09-07 — Privileged Identity Management (PIM)

## Actividades realizadas
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

## Observaciones
- PIM estructura claramente los flujos de activación temporal, reduciendo la exposición a permisos permanentes.
- La auditoría de recursos ofrece trazabilidad completa de activaciones, desactivaciones y cambios.
- La interfaz moderna oculta parte de la navegación clásica, pero mantiene la lógica de roles y auditoría.
- Sin licencia P2 no se pueden activar roles, pero sí estudiar la estructura y los flujos.

## Conocimientos adquiridos
- Diferencias entre **Eligible** y **Active**.
- Funcionamiento de la activación temporal de roles privilegiados.
- Integración de MFA y justificación dentro del flujo de activación.
- Revisión de auditoría y eventos registrados por PIM.
- Configuraciones avanzadas: alertas, revisiones de acceso, caducidad, etc.

## Próximos pasos
- Documentar la práctica completa en el portfolio.
- Integrar PIM dentro del módulo 02 de Identity Security.
- Preparar validaciones reales cuando se disponga de licencia P2.
