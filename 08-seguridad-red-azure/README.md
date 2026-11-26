# 08 | Seguridad de red en Azure

Una API expuesta a Internet necesita más que un cortafuegos de aplicación: las subredes, las reglas de tráfico y la resolución de nombres deciden qué puede alcanzar a qué. Este módulo documenta esa capa para la API del laboratorio: separar por función, cerrar la entrada y llevar los servicios a conectividad privada. El diseño está escrito en Bicep. La capa sin coste —VNet, NSG y subredes— se desplegó y validó el 2026-11-26; los Private Endpoints, el DNS privado y el firewall siguen sin desplegarse.

## Topología

La red parte de una VNet `10.20.0.0/16` con dos subredes. `snet-app` aloja la integración de App Service y lleva el NSG que solo permite 443 desde la propia VNet y deniega el resto de la entrada. `snet-pe` aloja los Private Endpoints de Key Vault y App Service, con sus zonas de DNS privado enlazadas a la VNet. La API sale a Internet con HTTPS y TLS 1.2, y los dos servicios dejan de aceptar tráfico público.

## Qué está validado y qué no

- **Validado estáticamente:** el job de Bicep del CI compila la plantilla (runs `39243360276` y `39920448092`) y Trivy config la revisa con cuatro supresiones justificadas en `.trivyignore`.
- **Validado en Azure (2026-11-26):** la VNet `10.20.0.0/16`, la subred de aplicación `10.20.1.0/24` con delegación a `Microsoft.Web/serverFarms` y NSG, y la subred de Private Endpoint `10.20.2.0/24` con las políticas de endpoint privado desactivadas ([evidencia](../laboratorio-final/evidencias/2026-11-26-08-red-y-api/README.md)).
- **No ejecutado:** Private Endpoints, DNS privado, firewall y prueba de conectividad privada. La red existe, pero el tráfico privado que importa sigue sin probarse.

## Prácticas

- [Segmentación con VNet y Network Security Groups](practicas/01-segmentacion-vnet-nsg/README.md) — *red desplegada; flujos privados pendientes*
- [Control centralizado de tráfico con Azure Firewall](practicas/02-control-trafico-firewall/README.md) — *diseño, sin IaC ni despliegue*
- [Acceso privado a servicios con Private Link](practicas/03-acceso-privado-private-link/README.md) — *IaC validada estáticamente; resolución y acceso pendientes*

## Límites

El NSG filtra solo la entrada: la salida sigue con las reglas predeterminadas de Azure hasta que exista un control de egreso, que es lo que plantea la práctica 02. El firewall no está en la plantilla porque su coste y su disponibilidad regional no se han confirmado. La red está desplegada, pero las pruebas que importan —conectividad permitida, conectividad denegada, nombre que resuelve a una IP privada— siguen sin ejecutarse: necesitan los Private Endpoints y el DNS privado, que son de pago y están en Diseño.
