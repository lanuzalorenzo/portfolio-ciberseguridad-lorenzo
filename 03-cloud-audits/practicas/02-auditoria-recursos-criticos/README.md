# 02 | Auditoría de Seguridad en Recursos Críticos (PaaS y Storage)

## Descripción del escenario y objetivo de seguridad

**Escenario:** Cargas de trabajo en Azure que utilizan servicios PaaS esenciales (Azure Storage Accounts, Azure SQL Database y Key Vault) expuestos a riesgos de fuga de información por configuraciones laxas por defecto.  
**Objetivo de seguridad:** Auditar la configuración de seguridad de recursos críticos, comprobando cifrado en tránsito/reposo, restricción de acceso público, directivas de red y autenticación moderna.  
**Alcance:** Cuentas de almacenamiento (Blob Storage), bases de datos Azure SQL y recursos Key Vault en suscripción de laboratorio.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Storage Account** | Almacenamiento de blobs y artefactos | Revisión de `allowBlobPublicAccess`, versión mínima de TLS (1.2) y acceso por claves compartidas. |
| **Azure SQL Database** | Base de datos relacional PaaS | Revisión de reglas de firewall, TLS forzado y autenticación basada en Microsoft Entra ID. |
| **Azure Key Vault** | Almacén criptográfico | Verificación de configuración de red pública, Azure RBAC activo y directiva de retención (*Soft Delete*). |
| **Network Security Groups (NSGs)** | Filtrado perimetral de red | Inspección de reglas de entrada permisivas (`0.0.0.0/0` en puertos administrativos como 22 o 3389). |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Bloqueo total de acceso anónimo a datos | `allowBlobPublicAccess = false` en Storage | Azure Policy en modo *Deny* / *Audit* | MCSB DP-4 / CIS 3.7 |
| Forzado de TLS moderno (1.2 o superior) | `minimumTlsVersion = TLS1_2` en Storage y SQL | Directiva de endurecimiento de transporte | MCSB DP-3 / NIST SP 800-52 |
| Eliminación de autenticación por claves locales | Deshabilitar *Shared Key Access* en favor de Entra ID | Azure RBAC exclusivo | MCSB DP-2 |

**Artefactos relacionados:** [Informe técnico de auditoría de recursos críticos](docs/auditoria-recursos-criticos-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Comprobación de acceso anónimo a Blob Storage | Petición HTTP anónima a contenedor de prueba | Error 409 PublicAccessNotPermitted | PASS: Acceso público deshabilitado a nivel de cuenta |
| Verificación de versión mínima de TLS | Negociación TLS con versiones obsoletas (TLS 1.0/1.1) | Rechazo del handshake TLS | PASS: El servicio exige TLS 1.2 estrictamente |
| Auditoría de reglas de firewall en Azure SQL | Inspección de rangos IP autorizados | Sin reglas permisivas abiertas a Internet (`0.0.0.0`) | PASS: Reglas acotadas a IPs de gestión autorizadas |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **DP-4: Prevención de fuga de datos en reposo** | Deshabilitación de acceso público en Storage | La opción de habilitar o deshabilitar acceso anónimo debe bloquearse a nivel de política de tenant, no dejarse al criterio del operador. |
| **DP-3: Protección de datos en tránsito** | Exigencia de TLS 1.2+ en todos los endpoints PaaS | Mitiga ataques de degradación criptográfica y descifrado pasivo de tráfico en tránsito. |

- La autenticación basada exclusivamente en Microsoft Entra ID para Azure SQL y Storage Accounts elimina la dispersión de contraseñas y claves de acceso (*Shared Keys*) imposibles de rotar ágilmente.