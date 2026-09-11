# ?? Ejercicio 07 — Managed Identities  
## Módulo 2 — Identity Security

## ?? Descripción del ejercicio
Este ejercicio consiste en implementar y validar Managed Identities en Azure para eliminar secretos y credenciales en aplicaciones y automatizaciones.

## ??? Arquitectura del caso práctico
07-managed-identities/
    README.md
    docs/
        managed-identities-documento-tecnico.md

## ?? Trabajo realizado
- Creación de una Managed Identity.
- Asignación de roles RBAC sobre recursos específicos.
- Validación de accesos desde scripts o servicios.
- Revisión de auditoría y logs.
- Ajuste de permisos para cumplir mínimo privilegio.

## ?? Validaciones
- Managed Identity creada correctamente.
- Permisos ajustados a mínimo privilegio.
- Sin roles excesivos ni permisos huérfanos.
- Accesos validados con éxito.
- Auditoría funcional.

## ?? Caso práctico final
- Identidad gestionada operativa.
- Accesos seguros sin secretos.
- Roles ajustados y validados.

## ?? Documentación completa
docs/managed-identities-documento-tecnico.md

## ?? Implicaciones de seguridad
- Las Managed Identities eliminan la necesidad de secretos.
- Un rol mal asignado puede exponer recursos críticos.
- Los accesos deben revisarse periódicamente.
