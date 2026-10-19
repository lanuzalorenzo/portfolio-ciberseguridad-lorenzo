# 08 | Seguridad de red en Azure

> **Estado:** diseño e IaC. La topología está implementada en Bicep y validada con `bicep build`; no se ha desplegado en Azure.

Este módulo aborda controles de red que reducen la superficie de exposición y limitan los flujos de tráfico hacia y entre las cargas de trabajo de Azure. Se centra en **segmentación por capas, control de tráfico perimetral y conectividad privada**.

## Escenario de referencia en la arquitectura

La topología de red documentada en este módulo está diseñada para aislar los componentes de una solución multicapa como [**EcommerceApi (lab-api-local-azure)**](https://github.com/lanuzalorenzo/lab-api-local-azure):
1. **Subred Frontend / Ingress:** Control de entrada perimetral hacia la API mediante políticas de inspección.
2. **Subred de Carga de Trabajo (Workload):** Alojamiento de la API .NET protegido mediante Network Security Groups (NSGs) que permiten únicamente tráfico HTTPS entrante autorizado y bloquean el acceso directo desde Internet.
3. **Subred de Datos y Secretos:** Aislamiento total de las bases de datos y de **Azure Key Vault**, garantizando que el acceso se realice exclusivamente a través de **Private Endpoints (Private Link)** con IPs privadas internas.

## Artefactos IaC

La plantilla [`infra/main.bicep`](https://github.com/lanuzalorenzo/lab-api-local-azure/blob/main/infra/main.bicep) implementa:

- VNet `10.20.0.0/16` con `snet-app` y `snet-pe`.
- NSG con allowlist de 443 desde la VNet y denegación por defecto.
- Key Vault con RBAC, purge protection, acceso público deshabilitado y Private Endpoint.
- Private DNS para Key Vault y App Service.
- App Service con integración VNet, HTTPS only y TLS 1.2.

La validación es estática (`bicep build` + Trivy config). No se ha ejecutado un despliegue real.

## Prácticas

- [Segmentación con VNet y Network Security Groups](practicas/01-segmentacion-vnet-nsg/README.md) — *IaC disponible; pendiente de despliegue*
- [Control centralizado de tráfico con Azure Firewall](practicas/02-control-trafico-firewall/README.md) — *diseño, no ejecutado*
- [Acceso privado a servicios con Private Link](practicas/03-acceso-privado-private-link/README.md) — *IaC disponible; pendiente de despliegue*

## Registro del trabajo

La [bitácora del módulo](bitacora/) registra las decisiones de diseño, topología y evolución de los laboratorios.

## Alcance

El módulo combina diseño, IaC y prácticas pendientes de validación. No representa una configuración desplegada en producción comercial. Cada práctica indica qué está implementado y qué falta por probar.