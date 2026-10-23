# Informe técnico — Auditoría de Seguridad en Recursos Críticos (PaaS y Storage)

**Módulo:** 03 — Auditorías Cloud  
**Práctica:** 02 — Auditoría de Recursos Críticos

## Contexto y Alcance
Los servicios PaaS y de almacenamiento en Azure (como Azure Storage Accounts, Azure SQL y Key Vault) albergan habitualmente los activos de datos más valiosos de una organización. A menudo, las configuraciones por defecto facilitan el despliegue rápido pero descuidan controles de acceso perimetral, cifrado y autenticación.

Esta práctica documenta la auditoría técnica sobre los recursos críticos de la suscripción de laboratorio, evaluando el cumplimiento frente a los dominios de protección de datos (DP) y seguridad de red (NS) del Microsoft Cloud Security Benchmark.

## Metodología de Inspección
Se inspeccionaron los planos de configuración y acceso de tres tipos de recursos clave:
1. **Cuentas de Almacenamiento (Azure Storage):** Parámetros de acceso anónimo, versión mínima de TLS y métodos de autorización habilitados.
2. **Azure SQL Database:** Reglas de firewall a nivel de servidor, forzado de cifrado y autenticación con Microsoft Entra ID.
3. **Azure Key Vault:** Configuración de cortafuegos de red, modelo de autorización (RBAC vs. Access Policies) y directivas de protección contra borrado.

## Matriz de Hallazgos de Seguridad

| ID Hallazgo | Severidad | Recurso Auditado | Descripción del Hallazgo | Riesgo Asociado | Recomendación de Remediación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **SEC-RES-01** | **Crítica** | Azure Storage Account | `allowBlobPublicAccess = true` habilitado a nivel de cuenta de almacenamiento. | Exposición accidental de datos sensibles a Internet si un operador crea un contenedor en modo público. | Deshabilitar el acceso público a blobs (`allowBlobPublicAccess = false`) y forzar directiva de Azure Policy que bloquee el parámetro a nivel de suscripción. |
| **SEC-RES-02** | **Alta** | Azure Storage Account | Versión mínima de TLS establecida en TLS 1.0 por defecto (`minimumTlsVersion = TLS1_0`). | Susceptibilidad a ataques de degradación criptográfica y descifrado de tráfico sensible en tránsito. | Actualizar el parámetro a `minimumTlsVersion = TLS1_2` o TLS 1.3 de forma obligatoria. |
| **SEC-RES-03** | **Alta** | Azure SQL Server | Regla de firewall activa permitiendo acceso a todos los servicios de Azure (`0.0.0.0/0` en *Allow Azure services*). | Cualquier recurso desplegado en cualquier suscripción de Azure de terceros podría alcanzar el endpoint del servidor si compromete credenciales. | Deshabilitar la opción global de Azure services, implementar reglas de firewall por IP estrictas o desplegar Private Endpoints (Azure Private Link). |
| **SEC-RES-04** | **Media** | Azure Key Vault | Key Vault desplegado sin activación de *Purge Protection*. | Riesgo de destrucción maliciosa permanente de secretos y certificados por parte de un atacante con permisos de borrado. | Habilitar *Purge Protection* para garantizar la inmutabilidad y recuperación obligatoria mediante *Soft Delete* durante el periodo de retención (90 días). |

## Verificación de Remediación
- Se aplicó la remediación inmediata sobre el hallazgo crítico **SEC-RES-01**, desactivando el acceso anónimo a blobs y comprobando mediante una solicitud curl directa que la API de Azure devuelve el error `409 PublicAccessNotPermitted`.
- Se verificó que tras imponer `minimumTlsVersion = TLS1_2`, los clientes que no negocian al menos TLS 1.2 ven rechazado el *handshake* criptográfico.

## Conclusiones Técnicas
- Los recursos PaaS deben desplegarse siguiendo plantillas endurecidas (IaC con Bicep o Terraform) que apliquen valores seguros por defecto, evitando configuraciones iniciales débiles.
- El aislamiento de red mediante Private Endpoints debe priorizarse sobre reglas de cortafuegos IP basadas en direcciones públicas.