# 03 | Acceso privado a servicios con Private Link

Key Vault y App Service no necesitan una IP pública para funcionar. El diseño los mete en la VNet mediante Private Endpoints y resuelve sus nombres con DNS privado, de modo que la API hable con ellos por la red interna y no por Internet.

**Referencias:** MCSB NS-2 · CIS Azure 6.x

| Qué se definió | Valor | Estado |
|---|---|---|
| Private Endpoint de Key Vault | `snet-pe`, grupo `vault`, zona `privatelink.vaultcore.azure.net` | En IaC |
| Private Endpoint de App Service | `snet-pe`, grupo `sites`, zona `privatelink.azurewebsites.net` | En IaC |
| Acceso público | Key Vault y App Service con `publicNetworkAccess: Disabled` | En IaC |
| Enlaces DNS | Ambas zonas enlazadas a la VNet, sin registro automático | En IaC |
| Resolución y conectividad privadas | Consulta y conexión desde la subred de aplicación | Pendiente: sin desplegar |

La plantilla compila en CI. Lo que no se ha hecho es desplegarla y comprobar que el nombre de Key Vault resuelve a la IP privada del endpoint, que la API obtiene el secreto y que el acceso público no responde. Esa es la diferencia entre declarar una red privada y tenerla.

El endpoint no basta sin la zona DNS y su enlace; deshabilitar el acceso público antes de probar la ruta privada puede romper la aplicación; y el grupo del endpoint (`vault` o `sites`) tiene que coincidir con el servicio.
