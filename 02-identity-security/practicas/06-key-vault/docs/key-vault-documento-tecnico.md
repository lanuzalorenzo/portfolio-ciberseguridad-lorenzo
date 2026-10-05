# Informe técnico — Seguridad y Control de Acceso en Azure Key Vault

**Módulo:** 02 — Identity Security  
**Práctica:** 06 — Azure Key Vault & Secrets Management

## Contexto y Objetivo
El almacenamiento de credenciales, cadenas de conexión y certificados directamente en código o variables de entorno desprotegidas constituye una de las principales causas de brechas de seguridad. 

Esta práctica documenta la configuración segura de un **Azure Key Vault** de laboratorio, la comparativa entre los modelos de autorización (*Azure RBAC* vs. *Vault Access Policies*), y la implementación de controles de seguridad en reposo y tránsito.

## Configuración y Decisiones de Arquitectura

Para este laboratorio se aplicaron las recomendaciones del Microsoft Cloud Security Benchmark (MCSB):

1. **Modelo de Autorización: Azure RBAC (Recomendado):**  
   Se seleccionó el modelo de permisos **Azure role-based access control (Azure RBAC)** frente al modelo heredado de *Access Policies*. Esto permite:
   - Integración nativa con Privileged Identity Management (PIM).
   - Asignación de permisos a nivel de secreto individual o a nivel de vault.
   - Auditoría unificada bajo el mismo registro de actividad de Azure.

2. **Roles de Plano de Datos Utilizados:**  
   Se definieron asignaciones estrictas con roles predefinidos:
   - **Key Vault Secrets Officer:** Asignado únicamente al equipo de administración/SecOps para crear, rotar y gestionar el ciclo de vida de los secretos.
   - **Key Vault Secrets User:** Asignado al servicio consumidor únicamente para lectura (`get`) del valor del secreto en tiempo de ejecución, sin permisos de listado (`list`) indiscriminado.
   - **Key Vault Reader:** Para auditoría (inspección de metadatos y configuración sin acceso al contenido de los secretos).

3. **Protección contra Eliminación Accidental:**
   - **Soft Delete:** Habilitado por defecto con retención de 90 días para proteger contra borrados accidentales o maliciosos.
   - **Purge Protection:** Activado para garantizar que un secreto no pueda ser eliminado definitivamente antes de que expire el periodo de retención.

## Validaciones y Pruebas de Seguridad

| Control / Prueba | Método | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Lectura de secreto con rol *Secrets User* | Petición con identidad autorizada | Lectura exitosa del valor del secreto | PASS: Valor recuperado correctamente |
| Listado de secretos sin rol de listado | Intento de listar catálogo de secretos | Error 403 Forbidden | PASS: Acceso denegado (requiere `Microsoft.KeyVault/vaults/secrets/readMetadata/action`) |
| Intento de lectura con rol de plano de control (*Reader*) | Usuario con rol *Reader* de Azure en el RG | Acceso denegado al contenido del secreto | PASS: El rol de plano de control no otorga acceso al plano de datos |
| Prueba de Purge con Purge Protection activo | Intento de purgado forzado de secreto borrado | Error de operación no permitida | PASS: Bloqueado por directiva de retención inmutable |

## Lecciones Aprendidas
- Migrar del modelo de *Access Policies* a *Azure RBAC* simplifica la gobernanza y reduce drásticamente el riesgo de asignaciones de permisos globales accidentales.
- El permiso de listado (`list`) en Key Vault debe tratarse con el mismo celo que el de lectura (`get`), ya que permite el descubrimiento de nombres y estructura de secretos sensibles.
