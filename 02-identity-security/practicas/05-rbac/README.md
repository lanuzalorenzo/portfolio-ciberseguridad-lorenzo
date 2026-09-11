# ?? Ejercicio 05 — RBAC  
## Módulo 2 — Identity Security

## ?? Descripción del ejercicio
Este ejercicio consiste en diseñar y validar un modelo RBAC aplicando buenas prácticas de seguridad.

## ??? Arquitectura del caso práctico
05-rbac/
    README.md
    docs/
        rbac-documento-tecnico.md

## ?? Trabajo realizado
- Diseño del modelo RBAC.
- Validación del principio de mínimo privilegio.
- Revisión de separación de funciones.
- Corrección de permisos excesivos en roles operativos.
- Ajuste del rol auditor.

## ?? Validaciones
- Roles con permisos definidos.
- Sin permisos directos a usuarios.
- Sin permisos huérfanos.
- Sin roles contradictorios.
- Cumplimiento de mínimo privilegio.

## ?? Caso práctico final
- admin: read, write, delete  
- auditor: read, audit  
- operador: read, write  

## ?? Documentación completa
docs/rbac-documento-tecnico.md

## ?? Implicaciones de seguridad
- Evitar escalada de privilegios.
- Mantener separación de funciones.
- Revisar roles periódicamente.
- Asignar permisos solo vía roles.
