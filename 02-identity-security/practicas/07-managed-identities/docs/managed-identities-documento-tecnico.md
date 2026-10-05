# Informe técnico — Identidades Administradas (Managed Identities) y Acceso sin Secretos

**Módulo:** 02 — Identity Security  
**Práctica:** 07 — Azure Managed Identities

## Contexto y Objetivo
El uso de credenciales estáticas (como *Client Secrets* o certificados almacenados localmente) en aplicaciones o scripts crea una superficie de ataque propensa a filtraciones de secretos en repositorios de código o logs.

El objetivo de esta práctica es implementar y verificar el uso de **Identidades Administradas de Azure (Managed Identities)** para autenticar un servicio contra recursos seguros de Azure (como Azure Key Vault) sin custodiar ni gestionar ninguna credencial estática.

## Arquitectura y Componentes Implementados

1. **Tipo de Identidad Seleccionada:**  
   Se implementó una **Identidad Administrada Asignada por el Sistema (*System-assigned Managed Identity*)**:
   - Su ciclo de vida queda vinculado directamente al ciclo de vida del recurso informático (al eliminar el recurso, Azure borra automáticamente el Service Principal asociado en Entra ID).
   - Elimina la necesidad de rotación periódica manual de secretos.

2. **Flujo de Autenticación mediante IMDS:**  
   La aplicación no utiliza usuario ni contraseña. Se comunica localmente con el **Azure Instance Metadata Service (IMDS)** en la dirección IP no enrutable:
   `http://169.254.169.254/metadata/identity/oauth2/token`
   - El endpoint requiere la cabecera `Metadata: true` para prevenir ataques de *Server-Side Request Forgery* (SSRF).
   - Azure emite de forma transparente un token de acceso JWT firmado por Entra ID para la audiencia especificada (ej. `https://vault.azure.net`).

3. **Asignación de Mínimo Privilegio (RBAC):**  
   A la identidad administrada se le asignó exclusivamente el rol de plano de datos:
   - **Rol:** *Key Vault Secrets User*
   - **Ámbito:** Limitado al Key Vault del laboratorio (o a un secreto específico dentro del vault).

## Validaciones y Pruebas de Seguridad

| Escenario Evaluado | Método de Prueba | Comportamiento Esperado | Resultado Observado |
| :--- | :--- | :--- | :--- |
| Petición de token a IMDS sin cabecera de seguridad | `curl "http://169.254.169.254/metadata/identity/oauth2/token?resource=..."` | Error 400 Bad Request por ausencia de cabecera | PASS: Bloqueado contra SSRF simple |
| Petición con cabecera `Metadata: true` | Petición HTTP interna autorizada con flag `Metadata: true` | Retorno de JWT con audiencia `https://vault.azure.net` | PASS: Token obtenido sin usar credenciales estáticas |
| Acceso a secreto con token de Managed Identity | Lectura del secreto en Key Vault usando el token de acceso | Petición 200 OK con valor del secreto | PASS: Acceso concedido conforme al rol asignado |
| Intento de acceso a recurso fuera de ámbito | Intento de acceso a recurso sin asignación de rol | 403 Forbidden | PASS: La identidad carece de permisos sobre otros recursos |

## Lecciones Aprendidas y Buenas Prácticas
- **Zero Secrets:** Las Identidades Administradas son el estándar de oro para la comunicación entre servicios dentro de Azure, eliminando el riesgo de fuga de credenciales en código fuente o pipelines de CI/CD.
- **Protección IMDS:** La validación de cabeceras en IMDS protege el endpoint interno contra vectores de inyección SSRF no autenticados.
- **Ciclo de vida automático:** Al destruir el recurso en el laboratorio, se previene la existencia de identidades o Service Principals huérfanos con permisos residuales en el tenant.
