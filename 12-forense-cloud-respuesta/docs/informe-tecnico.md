# Informe técnico — Forense cloud y KQL

Documento de apoyo del módulo 12. Recoge las consultas, el modelo de evidencia y las limitaciones. **No contiene resultados de ejecución** porque no se ha dispuesto de un workspace con datos.

## 1. Modelo de evidencia

| Fuente | Tabla | Retención propuesta | Valor forense |
|---|---|---|---|
| Azure Activity | `AzureActivity` | 90 días | Cambios de recursos y roles. |
| Entra Sign-in | `SigninLogs` | 90 días | Accesos, MFA, riesgo. |
| Entra Audit | `AuditLogs` | 90 días | Cambios de identidad y aplicaciones. |
| App Service | `AppServiceHTTPLogs` | 30–90 días | Peticiones y errores. |
| Key Vault | `AzureDiagnostics` | 90 días | Acceso a secretos. |
| NSG flow | `AzureNetworkAnalytics_CL` | 30 días | Flujos de red. |

## 2. Consultas

Las consultas completas están en [la práctica 02](../practicas/02-timeline-kql/README.md). Resumen:

1. Fallos de inicio de sesión por usuario/IP.
2. Éxito tras fallos en 30 minutos.
3. Cambios de roles y aplicaciones.
4. Cambios de NSG, VNet, Key Vault y App Service.
5. Operaciones sobre Key Vault.
6. Errores 401/403 en App Service.
7. `union` para línea temporal.

## 3. Cadena de custodia

Plantilla mínima:

```text
Incidente: INC-YYYY-MM-DD-001
Analista:
Fecha/hora UTC:
Fuente:
Consulta:
Rango temporal:
Destino de exportación:
SHA-256:
Acceso restringido a:
Observaciones:
```

## 4. Correlación

- **Identidad:** `UserPrincipalName`, `oid`, `appid`.
- **Red:** `IPAddress`, `CallerIPAddress`, `SourceIP`.
- **Recurso:** `ResourceId`, `Resource`, `CsUriStem`.
- **Tiempo:** normalizar a UTC y usar ventanas de 5–15 minutos.

## 5. Limitaciones

- Las tablas y campos deben validarse contra el workspace real.
- No se han ejecutado las consultas.
- No se ha medido el coste de retención.
- No se ha realizado un tabletop.

## 6. Próximos pasos

- Desplegar un workspace de laboratorio con diagnóstico.
- Ejecutar un incidente simulado y capturar evidencia.
- Validar las consultas y ajustar el ruido.
- Documentar tiempos de detección y contención.
