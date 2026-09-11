# ?? Ejercicio 06 — Key Vault  
## Módulo 2 — Identity Security

## ?? Descripción del ejercicio
Este ejercicio consiste en desplegar y validar un Key Vault aplicando buenas prácticas de seguridad en la gestión de secretos, claves y certificados.

## ??? Arquitectura del caso práctico
06-key-vault/
    README.md
    docs/
        key-vault-documento-tecnico.md

## ?? Trabajo realizado
- Creación del Key Vault.
- Almacenamiento de secretos de prueba.
- Configuración de permisos mediante RBAC y políticas de acceso.
- Validación de accesos permitidos y denegados.
- Revisión de auditoría y logs.

## ?? Validaciones
- Key Vault desplegado correctamente.
- Secretos almacenados de forma segura.
- Permisos ajustados a mínimo privilegio.
- Sin accesos directos innecesarios.
- Auditoría funcional.

## ?? Caso práctico final
- Secretos creados y protegidos.
- Roles ajustados para evitar exposición.
- Accesos validados con éxito.

## ?? Documentación completa
docs/key-vault-documento-tecnico.md

## ?? Implicaciones de seguridad
- Un Key Vault mal configurado puede exponer secretos críticos.
- El listado de secretos es tan sensible como leerlos.
- Los accesos deben revisarse periódicamente.
- Los secretos deben rotarse según buenas prácticas.
