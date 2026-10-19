# 01 | Recolección y preservación de evidencia

> **Estado:** diseño. La plantilla Bicep define diagnóstico a Log Analytics; no se ha desplegado ni exportado evidencia real.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Un incidente en Azure requiere reconstruir qué ocurrió, pero los logs no están centralizados, la retención es corta o la evidencia se altera durante la investigación.  
**Objetivo de seguridad:** Centralizar las fuentes relevantes, definir retención y preservar la evidencia con integridad y cadena de custodia.  
**Alcance:** Activity Log, Entra ID, Defender, App Service, Key Vault y NSG flow logs.

## Arquitectura y componentes

| Componente | Función | Configuración relevante |
|---|---|---|
| **Log Analytics** | Repositorio central | Retención de 30–90 días según coste. |
| **Diagnostic settings** | Envío de logs | App Service, Key Vault y NSG. |
| **Storage inmutable** | Evidencia a largo plazo | Blob inmutable/WORM si está disponible. |
| **Defender for Cloud** | Alertas | Exportación a Sentinel/Log Analytics. |
| **Entra ID** | Sign-in y audit logs | Exportación y retención. |

## Fuentes y retención propuestas

| Fuente | Tabla | Retención | Prioridad |
|---|---|---|---|
| Activity Log | `AzureActivity` | 90 días | Alta |
| Sign-in logs | `SigninLogs` | 90 días | Alta |
| Audit logs | `AuditLogs` | 90 días | Alta |
| App Service HTTP | `AppServiceHTTPLogs` | 30–90 días | Media |
| Key Vault | `AzureDiagnostics` | 90 días | Alta |
| NSG flow logs | `AzureNetworkAnalytics_CL` | 30 días | Media |

## Procedimiento de preservación

1. Identificar el alcance temporal y los recursos implicados.
2. Exportar las consultas y los resultados a un contenedor de evidencia.
3. Calcular hash SHA-256 de cada exportación.
4. Registrar en la cadena de custodia: fecha, analista, consulta, rango, hash.
5. Restringir el acceso al contenedor de evidencia.
6. No modificar los recursos antes de capturar la línea temporal.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Diagnóstico definido | Revisión de `infra/main.bicep` | App Service y Key Vault con diagnóstico | Implementado en IaC |
| Exportación de evidencia | Exportar consulta a Storage | Archivo con hash | Pendiente: requiere despliegue |
| Cadena de custodia | Revisión de la plantilla de registro | Campos completos | Pendiente: plantilla documentada, no usada |
| Retención | Revisión de Log Analytics | Retención configurada | Pendiente: no desplegado |

## Limitaciones

- No hay workspace desplegado ni datos reales.
- La retención y el coste no están calibrados.
- La inmutabilidad del almacenamiento depende del nivel de Storage.

## Artefactos relacionados

- [Plantilla Bicep](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/main.bicep)
- [Diseño de red](../../../08-seguridad-red-azure/README.md)
- [Informe técnico de KQL](../../docs/informe-tecnico.md)
