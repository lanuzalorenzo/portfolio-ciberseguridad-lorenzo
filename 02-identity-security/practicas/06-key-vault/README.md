# 06 | Gestión y protección de secretos en Azure Key Vault

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB DP-1, DP-2, BR-1 · NIST SP 800-53 SC-28.

Una contraseña de base de datos en un fichero de configuración es una credencial que acaba en un repositorio, en una copia de seguridad o en una captura de pantalla. Key Vault la guarda en un solo sitio, con permisos por rol, registro de accesos y protección contra el borrado definitivo.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Leer un secreto con *Secrets User* | Petición autorizada | Secreto devuelto | PASS: acceso concedido |
| Listar el catálogo sin rol de descubrimiento | Intento de enumerar secretos | Denegado | PASS: 403, sin reconocimiento |
| Purgar un secreto borrado | Borrado definitivo antes de la retención | Operación rechazada | PASS: Purge Protection lo impide |

## Lecciones

- Pasar de Access Policies a Azure RBAC unifica la gobernanza con el resto del tenant y con PIM.
- El permiso de listado (`list`) es tan sensible como el de lectura (`get`): permite mapear qué hay dentro.
- Soft Delete y Purge Protection convierten un borrado malicioso en un incidente recuperable.

## Más detalle

- [Configuración y controles](informe.md)
- [Bitácora del módulo](../../bitacora/2026-09-11-ejercicio-06-key-vault.md)
