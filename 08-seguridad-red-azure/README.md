# 08 | Seguridad de red en Azure

Este módulo aborda controles de red que reducen la superficie de exposición y limitan los flujos de tráfico hacia y entre las cargas de trabajo de Azure. Se centra en **segmentación por capas, control de tráfico perimetral y conectividad privada**.

## Escenario de referencia en la arquitectura

La topología de red documentada en este módulo está diseñada para aislar los componentes de una solución multicapa como [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure):
1. **Subred Frontend / Ingress:** Control de entrada perimetral hacia la API mediante políticas de inspección.
2. **Subred de Carga de Trabajo (Workload):** Alojamiento de la API .NET protegido mediante Network Security Groups (NSGs) que permiten únicamente tráfico HTTPS entrante autorizado y bloquean el acceso directo desde Internet.
3. **Subred de Datos y Secretos:** Aislamiento total de las bases de datos y de **Azure Key Vault**, garantizando que el acceso se realice exclusivamente a través de **Private Endpoints (Private Link)** con IPs privadas internas.

## Prácticas

- [Segmentación con VNet y Network Security Groups](practicas/01-segmentacion-vnet-nsg/README.md)
- [Control centralizado de tráfico con Azure Firewall](practicas/02-control-trafico-firewall/README.md)
- [Acceso privado a servicios con Private Link](practicas/03-acceso-privado-private-link/README.md)

## Registro del trabajo

La [bitácora del módulo](bitacora/) registra las decisiones de diseño, topología y evolución de los laboratorios.

## Alcance

El módulo se plantea como una serie de laboratorios y diseños arquitectónicos, no como una configuración desplegada en producción comercial. Cada práctica define su objetivo y validaciones pendientes; los resultados se documentan conforme a lo realmente probado.