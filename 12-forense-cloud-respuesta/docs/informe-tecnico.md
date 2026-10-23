# Informe técnico — Forense cloud y KQL

Documento de apoyo del módulo 12. Recoge el modelo de evidencia, las consultas, la cadena de custodia y las limitaciones. **No contiene resultados de ejecución**: las consultas no se han lanzado contra un workspace con datos.

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

### 2.1. Inicios de sesión fallidos

```kusto
SigninLogs
| where TimeGenerated between (datetime(2026-10-01) .. datetime(2026-10-02))
| where ResultType != "0"
| summarize attempts = count(), users = dcount(UserPrincipalName), ips = dcount(IPAddress)
    by bin(TimeGenerated, 15m), AppDisplayName, ResultType
| order by TimeGenerated asc
```

### 2.2. Inicio exitoso después de fallos

```kusto
let failures = SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType != "0"
| project UserPrincipalName, IPAddress, FailureTime = TimeGenerated;
SigninLogs
| where TimeGenerated > ago(24h)
| where ResultType == "0"
| join kind=inner failures on UserPrincipalName
| where TimeGenerated between (FailureTime .. FailureTime + 30m)
| project TimeGenerated, UserPrincipalName, IPAddress, AppDisplayName, ResultType
| order by TimeGenerated asc
```

### 2.3. Cambios de roles y aplicaciones

```kusto
AuditLogs
| where TimeGenerated > ago(7d)
| where OperationName has_any ("Add member to role", "Remove member from role", "Update application", "Add service principal")
| project TimeGenerated, OperationName, InitiatedBy, TargetResources
| order by TimeGenerated asc
```

### 2.4. Cambios de infraestructura

```kusto
AzureActivity
| where TimeGenerated > ago(7d)
| where OperationNameValue has_any ("NETWORKSECURITYGROUPS", "VIRTUALNETWORKS", "KEYVAULTS", "SITES")
| where ActivityStatusValue in ("Success", "Succeeded")
| project TimeGenerated, Caller, OperationNameValue, ResourceGroup, ResourceId, ActivityStatusValue
| order by TimeGenerated asc
```

### 2.5. Accesos a Key Vault

```kusto
AzureDiagnostics
| where ResourceType == "VAULTS"
| where TimeGenerated > ago(7d)
| where OperationName in ("SecretGet", "SecretList", "SecretSet", "SecretDelete", "VaultGet")
| project TimeGenerated, Resource, OperationName, ResultType, identity_claim_oid_g, CallerIPAddress
| order by TimeGenerated asc
```

### 2.6. Errores 401/403 en App Service

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(24h)
| where ScStatus in (401, 403)
| summarize count() by bin(TimeGenerated, 5m), CsMethod, CsUriStem, ScStatus, UserAgent
| order by TimeGenerated asc
```

### 2.7. Línea temporal unificada

```kusto
union
    (AzureActivity | project TimeGenerated, Source = "AzureActivity", Actor = Caller, Action = OperationNameValue, Detail = ResourceId),
    (AuditLogs | project TimeGenerated, Source = "AuditLogs", Actor = tostring(InitiatedBy), Action = OperationName, Detail = tostring(TargetResources)),
    (SigninLogs | where ResultType != "0" | project TimeGenerated, Source = "SigninLogs", Actor = UserPrincipalName, Action = "FailedSignin", Detail = ResultType),
    (AppServiceHTTPLogs | where ScStatus in (401, 403) | project TimeGenerated, Source = "AppService", Actor = CsUsername, Action = strcat(CsMethod, " ", CsUriStem), Detail = tostring(ScStatus))
| where TimeGenerated between (datetime(2026-10-01) .. datetime(2026-10-02))
| order by TimeGenerated asc
```

## 3. Cadena de custodia

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

- Las tablas y campos deben validarse contra el workspace real; los nombres cambian según el conector.
- No se han ejecutado las consultas y no se presentan resultados.
- No se ha medido el coste de retención.
- El tabletop del 2026-10-22 se hizo sobre documentación, sin entorno real ni reparto de roles.
- La correlación entre fuentes exige un identificador común y un rango temporal explícito.

## 6. Próximos pasos

- Desplegar un workspace de laboratorio con diagnóstico.
- Ejecutar un incidente simulado y capturar evidencia.
- Validar las consultas y ajustar el ruido.
- Documentar tiempos de detección y contención.
