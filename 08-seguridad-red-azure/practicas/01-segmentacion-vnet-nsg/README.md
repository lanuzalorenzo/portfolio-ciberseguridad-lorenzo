# 01 | Segmentación con VNet y Network Security Groups

La red del laboratorio separa la API de sus dependencias para que un fallo en una capa no abra las demás. El diseño está en [`infra/main.bicep`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/main.bicep) y no se ha desplegado: lo comprobado es que la plantilla compila y que las reglas declaradas son las que se quieren probar.

**Referencias:** MCSB NS-1 · CIS Azure 6.x

| Qué se definió | Valor | Estado |
|---|---|---|
| VNet | `10.20.0.0/16` | En IaC |
| Subred de aplicación | `snet-app`, `10.20.1.0/24`, delegada a `Microsoft.Web/serverFarms` | En IaC |
| Subred de endpoints | `snet-pe`, `10.20.2.0/24`, con políticas de Private Endpoint desactivadas | En IaC |
| NSG | 443/TCP desde `VirtualNetwork` (prioridad 100), `AzureLoadBalancer` (110) y denegación total de entrada (4096) | En IaC |
| Flujo permitido y flujo denegado | Conectividad real entre subredes | Pendiente: sin desplegar |

La validación es estática: el job de Bicep del CI compila la plantilla y Trivy revisa la configuración con cuatro supresiones justificadas en `.trivyignore`. No hay prueba de conectividad.

El NSG solo filtra la entrada. La salida sigue con las reglas predeterminadas de Azure hasta que se añada un control de egreso, que es lo que propone la práctica 02.

Una subred por función evita reglas que se solapan; la delegación de `snet-app` la exige la integración de App Service; y una plantilla que compila no demuestra que el tráfico correcto pase, solo que la intención está escrita.
