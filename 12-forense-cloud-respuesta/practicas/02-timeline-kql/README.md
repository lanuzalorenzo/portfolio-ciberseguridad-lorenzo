# 02 | Línea temporal y consultas KQL

> **Estado:** KQL revisado sintácticamente. No ejecutado contra un workspace con datos.

## Descripción del escenario y objetivo de seguridad

**Escenario:** Durante un incidente se dispone de eventos dispersos en Activity Log, Entra ID, App Service y Key Vault. Sin una línea temporal correlacionada es difícil distinguir causa, impacto y alcance.  
**Objetivo de seguridad:** Construir consultas que permitan reconstruir el incidente y producir evidencia reproducible.  
**Alcance:** `AzureActivity`, `SigninLogs`, `AuditLogs`, `AppServiceHTTPLogs`, `AzureDiagnostics` y alertas de Defender.

## Consultas

### 1. Inicios de sesión fallidos

```kusto
SigninLogs
| where TimeGenerated between (datetime(2026-10-01) .. datetime(2026-10-02))
| where ResultType != "0"
| summarize attempts = count(), users = dcount(UserPrincipalName), ips = dcount(IPAddress)
    by bin(TimeGenerated, 15m), AppDisplayName, ResultType
| order by TimeGenerated asc
```

**Uso:** detectar fuerza bruta, password spraying o errores de configuración.

### 2. Inicio exitoso después de fallos

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

**Uso:** identificar un acceso exitoso tras varios fallos (posible credencial comprometida).

### 3. Cambios de roles y aplicaciones

```kusto
AuditLogs
| where TimeGenerated > ago(7d)
| where OperationName has_any ("Add member to role", "Remove member from role", "Update application", "Add service principal")
| project TimeGenerated, OperationName, InitiatedBy, TargetResources
| order by TimeGenerated asc
```

**Uso:** detectar elevación de privilegios o persistencia.

### 4. Cambios de infraestructura

```kusto
AzureActivity
| where TimeGenerated > ago(7d)
| where OperationNameValue has_any ("NETWORKSECURITYGROUPS", "VIRTUALNETWORKS", "KEYVAULTS", "SITES")
| where ActivityStatusValue in ("Success", "Succeeded")
| project TimeGenerated, Caller, OperationNameValue, ResourceGroup, ResourceId, ActivityStatusValue
| order by TimeGenerated asc
```

**Uso:** reconstruir cambios de red, Key Vault o App Service.

### 5. Accesos a Key Vault

```kusto
AzureDiagnostics
| where ResourceType == "VAULTS"
| where TimeGenerated > ago(7d)
| where OperationName in ("SecretGet", "SecretList", "SecretSet", "SecretDelete", "VaultGet")
| project TimeGenerated, Resource, OperationName, ResultType, identity_claim_oid_g, CallerIPAddress
| order by TimeGenerated asc
```

**Uso:** detectar lectura masiva o acceso anómalo a secretos.

### 6. Errores 401/403 en App Service

```kusto
AppServiceHTTPLogs
| where TimeGenerated > ago(24h)
| where ScStatus in (401, 403)
| summarize count() by bin(TimeGenerated, 5m), CsMethod, CsUriStem, ScStatus, UserAgent
| order by TimeGenerated asc
```

**Uso:** identificar enumeración, fuerza bruta o fallos de autorización.

### 7. Línea temporal unificada

```kusto
union
    (AzureActivity | project TimeGenerated, Source = "AzureActivity", Actor = Caller, Action = OperationNameValue, Detail = ResourceId),
    (AuditLogs | project TimeGenerated, Source = "AuditLogs", Actor = tostring(InitiatedBy), Action = OperationName, Detail = tostring(TargetResources)),
    (SigninLogs | where ResultType != "0" | project TimeGenerated, Source = "SigninLogs", Actor = UserPrincipalName, Action = "FailedSignin", Detail = ResultType),
    (AppServiceHTTPLogs | where ScStatus in (401, 403) | project TimeGenerated, Source = "AppService", Actor = CsUsername, Action = strcat(CsMethod, " ", CsUriStem), Detail = tostring(ScStatus))
| where TimeGenerated between (datetime(2026-10-01) .. datetime(2026-10-02))
| order by TimeGenerated asc
```

**Uso:** vista única para el informe y la cadena de custodia. Ajustar tablas y campos al esquema real del workspace.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Sintaxis KQL | Revisión y ejecución en un workspace de prueba | Consultas válidas | Pendiente: no hay workspace |
| Cobertura de fuentes | Revisión de la matriz | Activity, Entra, App Service, Key Vault | Documentado |
| Línea temporal | Incidente simulado | Eventos ordenados y atribuibles | Pendiente |
| Falsos positivos | Revisión de resultados | Ruido identificado | Pendiente |

## Limitaciones

- Los nombres de tabla y campos pueden variar según el conector y el esquema.
- Las consultas no se han ejecutado; no se presentan resultados.
- La correlación entre fuentes requiere normalización y un identificador común (IP, usuario, recurso).

## Artefactos relacionados

- [Informe técnico con consultas](../../docs/informe-tecnico.md)
- [Módulo 09 — Sentinel](../../../09-microsoft-sentinel/README.md)
