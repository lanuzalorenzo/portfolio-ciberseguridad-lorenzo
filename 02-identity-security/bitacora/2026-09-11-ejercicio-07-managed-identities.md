# Bitácora — 2026-09-11: Autenticación sin Secretos con Managed Identities

**Módulo:** 02 — Identity Security  
**Práctica:** 07 — Managed Identities

Para cerrar las sesiones de hoy, configuré una **System-assigned Managed Identity** en un recurso de cómputo para resolver el problema recurrente de almacenar secretos y credenciales en scripts o repositorios.

La prueba de fuego consistió en verificar el flujo de autenticación contra el endpoint de metadatos de instancia (IMDS) en `169.254.169.254`. Comprobé que cualquier intento de solicitar un token sin la cabecera `Metadata: true` es rechazado de inmediato por el hipervisor (protección efectiva frente a SSRF básico).

Una vez inyectada la cabecera y solicitada la audiencia de Key Vault (`https://vault.azure.net`), obtuve un token JWT sin haber gestionado ningún password ni secreto estático. Con dicho token y el rol de *Key Vault Secrets User* asignado a la Managed Identity, pude recuperar el secreto del laboratorio de forma limpia. 

Eliminar credenciales fijas y delegar la rotación y autenticación completamente en la plataforma de Azure cierra de forma impecable este bloque de prácticas de identidad.
