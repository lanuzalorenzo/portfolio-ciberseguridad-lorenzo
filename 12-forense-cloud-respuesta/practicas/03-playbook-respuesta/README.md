# 03 | Playbook de respuesta y tabletop

> **Estado:** diseño. Playbook documentado; tabletop no ejecutado.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Se detecta un acceso anómalo a Key Vault desde una identidad de aplicación, con cambios recientes en NSG y un pico de errores 401 en la API.  
**Objetivo de seguridad:** Definir una respuesta ordenada que preserve evidencia, contenga el incidente y restablezca el servicio sin destruir la trazabilidad.  
**Alcance:** Incidente cloud en Azure con identidad, red y plano de datos implicados.

## Fases (NIST SP 800-61)

| Fase | Acciones | Evidencia |
|---|---|---|
| **Preparación** | Contactos, accesos de emergencia, retención, runbook. | Directorio y roles revisados. |
| **Detección y análisis** | Alertas de Defender, KQL, alcance temporal. | Consultas y timelines. |
| **Contención** | Revocar sesiones, deshabilitar identidad, restringir red. | Tickets y cambios. |
| **Erradicación** | Rotar secretos, corregir configuración, parchear. | Registro de rotación. |
| **Recuperación** | Restaurar servicio, monitorizar, validar. | Métricas y logs. |
| **Lecciones** | Post-incidente, acciones y responsables. | Informe final. |

## Playbook

### 1. Triaje

- Confirmar la alerta y el recurso afectado.
- Identificar identidad, IP, user agent y ventana temporal.
- Clasificar severidad e impacto.
- Abrir incidente y canal de comunicación.

### 2. Preservación

- Exportar `SigninLogs`, `AuditLogs`, `AzureActivity`, `AzureDiagnostics` y `AppServiceHTTPLogs`.
- Calcular hash y registrar cadena de custodia.
- No borrar recursos ni rotar secretos antes de capturar la línea temporal.

### 3. Contención

- Revocar sesiones y refresh tokens de la identidad comprometida.
- Deshabilitar la identidad o retirar roles.
- Restringir NSG/Private Endpoint si hay movimiento lateral.
- Aislar la aplicación si hay ejecución maliciosa.

### 4. Erradicación

- Rotar secretos y claves expuestas.
- Corregir la configuración que permitió el acceso.
- Revisar persistencia: nuevas aplicaciones, roles, credenciales.
- Aplicar parches y validar controles.

### 5. Recuperación

- Restaurar el servicio de forma controlada.
- Monitorizar 401/403, accesos a Key Vault y cambios de red.
- Confirmar que no hay reingreso.

### 6. Post-incidente

- Documentar causa raíz, impacto y cronología.
- Añadir detecciones y pruebas de regresión.
- Actualizar el playbook y la matriz de controles.

## Tabletop propuesto

| Escenario | Participantes | Duración | Artefactos |
|---|---|---|---|
| Acceso anómalo a Key Vault + cambio de NSG | SecOps, AppSec, Cloud | 90 min | Timeline, decisiones, evidencias |

**Estado:** no ejecutado. No hay resultados que presentar.

## Mapeo MITRE ATT&CK (orientativo)

| Táctica | Técnica | Evidencia a buscar |
|---|---|---|
| Credential Access | T1552 Unsecured Credentials | Accesos a Key Vault, secretos en logs. |
| Persistence | T1098 Account Manipulation | Cambios de roles/aplicaciones. |
| Defense Evasion | T1562 Impair Defenses | Cambios de NSG, diagnóstico o políticas. |
| Collection | T1530 Data from Cloud Storage | Lectura masiva de blobs. |

## Limitaciones

- No se ha ejecutado el tabletop.
- No hay datos reales ni un workspace de Sentinel.
- Los tiempos de contención no están medidos.
- La rotación de secretos y la revocación de sesiones deben probarse en un tenant de laboratorio.

## Artefactos relacionados

- [Recolección de evidencia](../01-recoleccion-logs-azure/README.md)
- [Consultas KQL](../02-timeline-kql/README.md)
- [Informe técnico](../../docs/informe-tecnico.md)
