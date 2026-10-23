# 12 | Forense cloud y respuesta a incidentes

> **Estado:** **Parcial**. Playbook, runbook y KQL documentados, y **tabletop ejecutado el 2026-10-22** con [acta](../laboratorio-final/evidencias/2026-10-22-12-tabletop/README.md). Pendiente: variante de laboratorio, recolección técnica y ejecución de las consultas en un workspace de Sentinel con datos.

Este módulo cubre la investigación de incidentes en Azure desde la recolección de evidencia hasta la respuesta. Se apoya en la telemetría que ya define la arquitectura de referencia: Activity Log, Entra ID, Defender, App Service, Key Vault y flujos de red.

## Objetivo

- Definir fuentes de evidencia y su retención.
- Construir una línea temporal con KQL.
- Documentar un playbook de respuesta con contención, erradicación y recuperación.
- Distinguir claramente entre consultas revisadas y consultas ejecutadas.

## Alcance

| Fuente | Uso forense |
|---|---|
| **Azure Activity Log** | Cambios de recursos, asignaciones de roles, eliminaciones. |
| **Entra ID SigninLogs** | Intentos de acceso, MFA, riesgo, ubicaciones. |
| **Entra ID AuditLogs** | Cambios de identidad, roles, aplicaciones. |
| **Defender for Cloud** | Alertas y recomendaciones. |
| **App Service logs** | Peticiones HTTP, errores, consola. |
| **Key Vault audit** | Accesos y operaciones sobre secretos. |
| **NSG flow logs** | Conexiones permitidas/denegadas. |

## Prácticas

- [Recolección y preservación de evidencia](practicas/01-recoleccion-logs-azure/README.md) — *diseño; Bicep con diagnóstico, no desplegado*
- [Línea temporal y consultas KQL](practicas/02-timeline-kql/README.md) — *KQL revisado, no ejecutado*
- [Playbook de respuesta y tabletop](practicas/03-playbook-respuesta/README.md) — *tabletop ejecutado el 2026-10-22; variante con roles pendiente*

## Principios

1. **Preservar antes de tocar:** exportar y hashear la evidencia antes de contener.
2. **Cadena de custodia:** registrar quién accedió, cuándo y con qué herramienta.
3. **Mínimo privilegio:** el investigador no debe poder alterar la evidencia.
4. **Separar hechos de hipótesis:** cada conclusión debe apuntar a una consulta o artefacto.
5. **Documentar lo que no se pudo probar:** la ausencia de evidencia no es evidencia de ausencia.

## Relación con otros módulos

- [08 — Redes Azure](../08-seguridad-red-azure/README.md): NSG, Private Endpoints y flujos.
- [09 — Microsoft Sentinel](../09-microsoft-sentinel/README.md): detección y analítica.
- [11 — Hacking ético de APIs](../11-hacking-etico-api/README.md): escenarios que generan evidencia.

## Limitaciones

- No hay workspace de Sentinel ni tenant con datos de laboratorio en esta iteración.
- Las consultas KQL están revisadas sintácticamente, pero no ejecutadas.
- El tabletop se ejecutó sobre documentación; falta la variante con reparto de roles y entorno real.
- La retención y el coste de Log Analytics no se han calibrado.

## Aviso

Todo el contenido es defensivo y se limita a un laboratorio propio. No incluye datos personales, secretos ni procedimientos para atacar sistemas de terceros.
