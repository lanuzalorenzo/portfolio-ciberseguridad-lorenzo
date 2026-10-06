# Protección de la rama principal y control de cambios

Este documento describe el control base de seguridad del flujo de desarrollo: las modificaciones a la rama principal deben pasar por revisión, validación y trazabilidad antes de integrarse.

## Objetivo

Reducir el riesgo de cambios no auditados, sobreescrituras accidentales, conflictos de integración y modificaciones directas a la rama de producción o de referencia.

## Política documentada

- Requerir Pull Request para cualquier cambio hacia `main`.
- Exigir al menos una aprobación antes de fusionar.
- Bloquear `force-push` y el borrado de la rama protegida.
- Evitar escritura directa a la rama principal.
- Mantener un historial limpio y auditable del código.
- Vincular verificaciones automáticas (status checks) cuando exista CI/CD asociado.

## Buenas prácticas recomendadas

| Práctica | Propósito | Impacto de seguridad |
|---|---|---|
| **PR obligatorio** | Canaliza cada cambio a revisión humana y técnica | Reduce cambios no validados |
| **Aprobación mínima** | Requiere una segunda mirada antes de integrar | Detecta errores y malas prácticas |
| **Sin fuerza de escritura** | Evita sobrescritura accidental del historial | Preserva integridad del código |
| **Validación automática** | Rechaza cambios con errores de compilación o análisis | Mejora calidad y seguridad |
| **Historial trazable** | Permite reconstruir eventos y decisiones | Facilita auditoría y compliance |

## Alcance y validación

La regla describe el baseline mínimo de una estrategia DevSecOps para repositorios de software. La configuración concreta debe validarse en la plataforma del repositorio (GitHub, Azure DevOps, GitLab u otro). Este documento establece el criterio técnico y el enfoque de seguridad, pero no sustituye la configuración real del entorno.

**Artefactos relacionados:** [README del módulo](README.md) y [práctica de protección de ramas](practicas/01-proteccion-ramas/README.md).
