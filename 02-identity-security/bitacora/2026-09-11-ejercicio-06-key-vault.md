# Bitácora — 2026-09-11: Despliegue y Securización de Azure Key Vault

**Módulo:** 02 — Identity Security  
**Práctica:** 06 — Key Vault & Secrets Management

Continuando con la jornada, desplegué un Azure Key Vault de laboratorio para almacenar cadenas de conexión y secretos sensibles.

La decisión técnica clave fue optar por el modelo de autorización **Azure RBAC** en lugar de las directivas de acceso clásicas (*Access Policies*). La ventaja es clara: permite integrar el acceso a secretos con PIM y asignar permisos finos a nivel de secreto individual. Asigné el rol *Key Vault Secrets Officer* únicamente al perfil de administración y *Key Vault Secrets User* a la identidad que necesita consumir el secreto.

Habilité expresamente **Soft Delete** y **Purge Protection**. Para comprobarlo en caliente, eliminé un secreto de prueba e intenté purgarlo forzosamente; Azure rechazó la operación inmediatamente respetando el periodo de retención inmutable. Además, verifiqué que los roles de lectura de ARM no permiten inspeccionar el valor de los secretos sin contar con un rol explícito en el plano de datos.
