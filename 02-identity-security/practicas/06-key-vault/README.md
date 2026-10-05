# 06 | Gestión y Protección de Secretos en Azure Key Vault

## Descripción del escenario y objetivo de seguridad

**Escenario:** Aplicaciones y servicios almacenando contraseñas, tokens y cadenas de conexión en texto plano o variables de entorno no auditables, vulnerables a exfiltración.  
**Objetivo de seguridad:** Centralizar la custodia de secretos en Azure Key Vault aplicando el modelo de autorización Azure RBAC, control de ciclo de vida con Soft Delete y protección inmutable contra purgado.  
**Alcance:** Recurso Azure Key Vault en suscripción de laboratorio, secretos de prueba y roles de plano de datos.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Key Vault** | Almacén criptográfico y de secretos | Habilitado con modelo de permisos *Azure role-based access control*. |
| **Soft Delete** | Retención de elementos eliminados | Retención configurada en 90 días para recuperación ante incidentes. |
| **Purge Protection** | Inmutabilidad de borrado | Forzado activo; impide la destrucción definitiva antes de expirar el periodo de retención. |
| **Rol Key Vault Secrets User** | Acceso de lectura a secretos en runtime | Permite acción `get` sobre el secreto requerido sin permisos de listado general. |
| **Rol Key Vault Secrets Officer** | Gestión del ciclo de vida de secretos | Permite operaciones de creación, edición y rotación asignado a SecOps. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Control de acceso en plano de datos vía RBAC | Modelo Azure RBAC habilitado en Key Vault | Asignación en Azure Resource Manager | MCSB DP-1 / DP-2 |
| Protección contra ransomware / borrado | Soft Delete y Purge Protection activos | Configuración inmutable del recurso | MCSB BR-1 |
| Principio de menor privilegio en secretos | Roles granulares de lectura sin permiso de listado (`list`) | Matriz de permisos RBAC | NIST SP 800-53 SC-28 |

**Artefactos relacionados:** [Configuración y controles de Key Vault](docs/key-vault-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Lectura de secreto con rol *Secrets User* | Petición autorizada con identidad asignada | Valor del secreto recuperado exitosamente | PASS: Acceso concedido al secreto objetivo |
| Listado de secretos sin rol de descubrimiento | Intento de listar catálogo de secretos en el vault | Error 403 Forbidden | PASS: Bloqueado; se mitiga el reconocimiento interno |
| Purgado forzado de secreto borrado | Intento de eliminación definitiva antes de retención | Error de operación rechazada | PASS: Purge Protection bloquea la eliminación permanente |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **DP-1: Descubrimiento y protección de datos sensibles** | Centralización en Key Vault con Azure RBAC | Migrar del modelo clásico de Access Policies a Azure RBAC permite una gobernanza unificada e integrada con PIM. |
| **BR-1: Recuperación ante desastres y copias de seguridad** | Aplicación de Purge Protection | Impide que un actor malicioso o un administrador comprometido borre permanentemente credenciales críticas para causar denegación de servicio. |

- Tratar el permiso de listado (`list`) con la misma criticidad que el de lectura (`get`) previene el descubrimiento y mapeo de secretos por parte de identidades comprometidas.
