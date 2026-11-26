# Comandos ejecutados

Los valores entre `<...>` sustituyen identificadores reales. La región es `spaincentral` y la fecha, 2026-11-26.

## 1. `what-if` de la capa gratuita

```bash
az deployment group what-if \
  --resource-group rg-ecomlab-f1 \
  --template-file infra/main.bicep \
  --parameters workload=ecomlab environmentName=dev location=spaincentral \
               tenantId=<tenant-id> apiClientId=<app-id> apiAudience=api://<app-id> \
               desplegarServiciosDePago=false \
  --result-format ResourceIdOnly
```

Salida:

```text
+ Create
+ Microsoft.Network/networkSecurityGroups/nsg-ecomlab-dev-esc-cmmt
+ Microsoft.Network/virtualNetworks/vnet-ecomlab-dev-esc-cmmt
```

## 2. Despliegue de la red

```bash
az deployment group create \
  --resource-group rg-ecomlab-f1 --name fase1-red-20261126 \
  --template-file infra/main.bicep \
  --parameters workload=ecomlab environmentName=dev location=spaincentral \
               tenantId=<tenant-id> apiClientId=<app-id> apiAudience=api://<app-id> \
               desplegarServiciosDePago=false
```

Salida: `provisioningState: Succeeded`.

## 3. Validación de la red

```bash
az resource list --resource-group rg-ecomlab-f1 \
  --query '[].{tipo:type,nombre:name,region:location}' --output table
```

```text
Microsoft.Network/networkSecurityGroups  nsg-ecomlab-dev-esc-cmmt   spaincentral
Microsoft.Network/virtualNetworks        vnet-ecomlab-dev-esc-cmmt  spaincentral
```

```bash
az network vnet subnet show \
  --resource-group rg-ecomlab-f1 --vnet-name vnet-ecomlab-dev-esc-cmmt \
  --name snet-ecomlab-dev-esc-app \
  --query '{prefijo:addressPrefix,delegaciones:delegations[].serviceName}'
```

```json
{
  "delegaciones": ["Microsoft.Web/serverFarms"],
  "prefijo": "10.20.1.0/24"
}
```

```bash
az network vnet subnet show \
  --resource-group rg-ecomlab-f1 --vnet-name vnet-ecomlab-dev-esc-cmmt \
  --name snet-ecomlab-dev-esc-pe \
  --query '{prefijo:addressPrefix,politicas:privateEndpointNetworkPolicies}'
```

```json
{ "politicas": "Disabled", "prefijo": "10.20.2.0/24" }
```

Reglas del NSG: `AllowHttpsFromVirtualNetwork` (443 desde la VNet), `AllowAzureLoadBalancer` y `DenyAllInbound`.

## 4. API en Container Apps

```bash
az containerapp env create \
  --name cae-ecomlab-dev --resource-group rg-ecomlab-f1 --location spaincentral \
  --logs-destination none
```

```bash
az containerapp create \
  --name ca-ecomlab-api --resource-group rg-ecomlab-f1 \
  --environment cae-ecomlab-dev \
  --image ghcr.io/lanuzalorenzo/ecommerceapi@sha256:6702689de66df0916d165d7ee52cf7f208c2186028810acd7b2996d86e70f712 \
  --target-port 8080 --ingress external \
  --min-replicas 0 --max-replicas 1 \
  --env-vars ASPNETCORE_ENVIRONMENT=Production \
             AzureAd__TenantId=<tenant-id> \
             AzureAd__ClientId=<app-id> \
             AzureAd__Audience=api://<app-id> \
             AzureAd__Authority=https://login.microsoftonline.com/<tenant-id>/v2.0 \
             'Storage__ConnectionString=Data Source=/tmp/ecommerce.db'
```

Estado observado: entorno `Succeeded` con `appLogsConfiguration.destination` nulo; aplicación `Succeeded` con la imagen fijada por digest, `minReplicas: 0` y `maxReplicas: 1`.

## 5. Pruebas contra la API

```bash
curl -sS --max-time 90 -D headers-health -o body-health "https://<fqdn>/health"
```

```text
HTTP/2 200
sin cabecera Server
Healthy
```

```bash
curl -sS --max-time 90 -D headers-products -o body-products "https://<fqdn>/api/products"
```

```text
HTTP/2 401
content-length: 0
www-authenticate: Bearer
x-content-type-options: nosniff
x-frame-options: DENY
referrer-policy: no-referrer
permissions-policy: geolocation=(), microphone=(), camera=()
content-security-policy: default-src 'none'; frame-ancestors 'none'; base-uri 'none'; form-action 'none'
```

El cuerpo del 401 tiene 0 bytes: es el hallazgo de esta evidencia.

## 6. Etiquetas y ventana

```bash
az group show --name rg-ecomlab-f1 --query 'tags'
```

```json
{ "expires": "2026-12-03", "lab": "ecomlab", "owner": "<owner>" }
```

## 7. Limpieza (pendiente el 2026-12-03)

```bash
az group delete --name rg-ecomlab-f1 --yes
az group exists --name rg-ecomlab-f1
```

El segundo comando debe devolver `false`. La salida se añade aquí cuando se ejecute.
