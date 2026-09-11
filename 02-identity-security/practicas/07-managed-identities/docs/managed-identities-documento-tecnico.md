# ?? Ejercicio 07 — Managed Identities  
## Documento técnico  
## Módulo 2 — Identity Security

## ?? Contexto (atemporal)
Este ejercicio aborda el uso de Managed Identities en Azure para eliminar secretos y credenciales en aplicaciones y automatizaciones.  
El objetivo es comprender cómo funcionan, cómo se asignan permisos y cómo interactúan con servicios como Key Vault.

## ?? Objetivo
Implementar Managed Identities y aplicar buenas prácticas:
- Crear una Managed Identity.
- Asignar permisos mediante RBAC.
- Validar accesos a Key Vault u otros recursos.
- Revisar implicaciones de seguridad.

## ?? Trabajo realizado (cronológico y técnico)
1. Revisión del GUION del módulo para identificar requisitos del ejercicio.
2. Creación de una Managed Identity (System-assigned).
3. Asignación de roles RBAC sobre recursos específicos.
4. Validación de accesos desde scripts o servicios.
5. Revisión de auditoría y logs de acceso.
6. Eliminación de permisos innecesarios.

## ?? Validaciones realizadas
- La Managed Identity está correctamente creada.
- Los permisos cumplen mínimo privilegio.
- No existen roles excesivos ni permisos huérfanos.
- Accesos validados correctamente.
- Auditoría funcional.

## ?? Problemas encontrados
- Un rol permitía acceso de escritura sin necesidad operativa.
- Un recurso tenía permisos heredados no deseados.

## ??? Soluciones aplicadas
- Ajuste de roles para cumplir mínimo privilegio.
- Eliminación de permisos heredados innecesarios.
- Revisión completa de asignaciones RBAC.

## ?? Implicaciones de seguridad
- Las Managed Identities eliminan la necesidad de secretos.
- Un rol mal asignado puede exponer recursos críticos.
- Los accesos deben revisarse periódicamente.
- Las identidades deben limitarse a recursos específicos.

## ?? Recursos útiles (opcionales)
- Microsoft Learn — Managed Identities Overview
- Azure RBAC Documentation

## ?? Comandos utilizados (opcionales)
_No aplica._

## ?? Comandos pendientes (opcionales)
_No aplica._
