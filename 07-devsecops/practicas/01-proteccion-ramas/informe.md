# Informe técnico — Protección de ramas y revisión de cambios

**Módulo:** 07 — DevSecOps y gobernanza del software  
**Práctica:** 01 — Protección de ramas y revisión de cambios

## Contexto y objetivo

La protección de la rama principal es un control básico de seguridad en cualquier flujo de desarrollo. Su objetivo no es solo impedir errores accidentales, sino también reforzar la trazabilidad, la revisión por pares y la integridad del historial de cambios antes de que el código llegue a un entorno de ejecución o producción.

En un entorno de desarrollo seguro, cada cambio debe pasar por validación técnica y revisión humana, lo que reduce el riesgo de introducir vulnerabilidades, errores de integración o alteraciones no autorizadas en la base de código.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Revisión previa** | Todo cambio hacia `main` debe abrir un Pull Request | Mejora la calidad y la trazabilidad |
| **Aprobación obligatoria** | La integración requiere validación del código por parte de otro miembro | Reduce errores de configuración y malas decisiones |
| **Bloqueo de sobrescritura** | Se evita el `force-push` y el borrado de la rama protegida | Preserva integridad del repositorio |
| **Validación automática** | Conexión con status checks y pipelines | Asegura que no se fusionan cambios rotos |
| **Trazabilidad** | El historial refleja quién, cuándo y por qué se integra cada cambio | Facilita auditoría y response |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **Pull Request obligatorio** | Sí | Evita fusión directa sin revisión |
| **Aprobación mínima** | 1 o más revisores | Requiere validación humana |
| **Sin force push** | Sí | Preserva integridad del historial |
| **Borrado de rama bloqueado** | Sí | Evita pérdida de trazabilidad |
| **Required status checks** | Sí, cuando existen pipelines | No se fusiona código no validado |

## Implementación técnica recomendada

1. Proteger la rama principal en la plataforma de repositorio.
2. Exigir Pull Requests para cualquier integración.
3. Requerir al menos una aprobación de revisión.
4. Desactivar la escritura directa a la rama base.
5. Evitar el borrado de la rama protegida.
6. Vincular validaciones automáticas de CI/CD (lint, tests, scans o compilación).
7. Mantener trazabilidad de cambios y evidencias de aprobación.

## Riesgos mitigados

- Cambios no revisados o defectuosos.
- Sobrescrituras accidentales del historial Git.
- Integración de código sin validación técnica.
- Falta de evidencia para auditoría operativa o regulatoria.
- Incremento del riesgo de introducir vulnerabilidades por cambios rápidos y no supervisados.

## Conclusión

La política de protección de ramas no es una medida aislada ni burocrática; es un control fundamental de seguridad del desarrollo. Cuando se combina con validaciones automáticas y revisión humana, convierte el repositorio en un punto más seguro de la cadena de valor del software.
