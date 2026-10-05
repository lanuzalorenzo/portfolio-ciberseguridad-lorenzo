# 07 | Identidades Administradas (Managed Identities) en Azure

## Descripción del escenario y objetivo de seguridad

**Escenario:** Servicios y aplicaciones desplegadas en Azure que requieren conectarse a Azure Key Vault u otros recursos, recurriendo habitualmente a secretos de aplicación embebidos en código o archivos de configuración.  
**Objetivo de seguridad:** Eliminar por completo el uso de secretos estáticos en código mediante la implementación de Identidades Administradas (Managed Identities) autenticadas vía Azure Instance Metadata Service (IMDS).  
**Alcance:** Recurso de cómputo en Azure con System-assigned Managed Identity y acceso a secretos en Azure Key Vault.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **System-assigned Managed Identity** | Identidad sin contraseña vinculada al recurso | Ciclo de vida atado al recurso de cómputo; Service Principal gestionado por Azure. |
| **Endpoint IMDS (`169.254.169.254`)** | Emisión local de tokens OAuth2 de plataforma | Accesible solo internamente desde el recurso; exige cabecera `Metadata: true`. |
| **Azure Key Vault** | Recurso destino de acceso seguro | Asignación de rol *Key Vault Secrets User* a la Managed Identity en el plano de datos. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Eliminación total de credenciales en código | Identidad administrada asignada por el sistema | Configuración nativa del recurso | MCSB IA-1 / DevSecOps |
| Protección contra SSRF en obtención de token | Exigencia obligatoria de cabecera HTTP `Metadata: true` | Implementación nativa de Azure IMDS | OWASP Top 10 A10:2021 |
| Mínimo privilegio en el consumo de secretos | Asignación exclusiva del rol *Key Vault Secrets User* | Asignación RBAC en Key Vault | MCSB PA-1 |

**Artefactos relacionados:** [Configuración y validación de Managed Identities](docs/managed-identities-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Petición a IMDS sin cabecera `Metadata: true` | `curl` directo al endpoint de metadatos local | Error 400 Bad Request | PASS: Azure rechaza la petición; mitigación SSRF efectiva |
| Solicitud de token con cabecera de seguridad | `curl -H "Metadata: true"` solicitando recurso de Key Vault | Emisión exitosa de JWT firmado por Entra ID | PASS: Token obtenido sin credenciales estáticas |
| Consumo de secreto en Key Vault usando el JWT | Petición a la API de Key Vault con Bearer token | Retorno del secreto almacenado | PASS: Acceso concedido conforme al rol RBAC |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **IA-1: Uso de identidades gestionadas por el proveedor** | Reemplazo de Client Secrets por Managed Identities | Elimina el riesgo operativo de expiración de secretos y el riesgo de seguridad por fuga en repositorios de código. |

- Al destruir o recrear el recurso de cómputo, Azure borra automáticamente el Service Principal en Entra ID, previniendo identidades huérfanas con permisos residuales en el entorno.
