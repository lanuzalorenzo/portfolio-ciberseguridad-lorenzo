# 01 | Recolección y preservación de evidencia

Un incidente se investiga con lo que se guardó antes de que ocurriera. Si los logs no están centralizados, la retención es corta o alguien toca los recursos antes de exportarlos, la reconstrucción se vuelve una hipótesis. La práctica define qué fuentes recoger, cuánto conservarlas y cómo preservarlas.

**Referencias:** NIST SP 800-86 · MCSB LT-1

| Fuente | Tabla | Retención propuesta |
|---|---|---|
| Activity Log | `AzureActivity` | 90 días |
| Signin y Audit | `SigninLogs`, `AuditLogs` | 90 días |
| App Service HTTP | `AppServiceHTTPLogs` | 30–90 días |
| Key Vault | `AzureDiagnostics` | 90 días |
| NSG flow | `AzureNetworkAnalytics_CL` | 30 días |

Preservar es un procedimiento, no una intención: identificar alcance temporal y recursos, exportar consultas y resultados a un contenedor de evidencia, calcular SHA-256 de cada exportación, registrar fecha, analista, consulta y rango, restringir el acceso y no modificar nada antes de capturar la línea temporal.

En el IaC, App Service y Key Vault ya envían diagnósticos a Log Analytics; no está desplegado. La exportación, el hash y la cadena de custodia siguen sin ejecutarse, igual que la calibración de retención y coste. La plantilla de custodia está escrita, pero no se ha usado.

Una retención corta borra la prueba antes de que la pidas; un contenedor sin hash no demuestra integridad; y tocar el recurso antes de exportar convierte la evidencia en interpretación.
