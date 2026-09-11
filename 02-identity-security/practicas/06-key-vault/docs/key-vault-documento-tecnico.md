# ?? Ejercicio 06 — Key Vault  
## Documento técnico  
## Módulo 2 — Identity Security

## ?? Contexto (atemporal)
Este ejercicio se centra en la gestión segura de secretos, claves y certificados mediante Azure Key Vault.  
El objetivo es comprender cómo se almacenan, protegen y acceden estos elementos críticos dentro de un entorno cloud seguro.

## ?? Objetivo
Implementar un Key Vault y aplicar buenas prácticas de seguridad:
- Crear un Key Vault.
- Almacenar secretos.
- Configurar permisos.
- Validar accesos.
- Revisar implicaciones de seguridad.

## ?? Trabajo realizado (cronológico y técnico)
1. Revisión del GUION del módulo para identificar requisitos del ejercicio.
2. Creación del Key Vault en el entorno de práctica.
3. Almacenamiento de secretos de prueba.
4. Configuración de permisos mediante RBAC y políticas de acceso.
5. Validación de accesos permitidos y denegados.
6. Revisión de auditoría y logs de acceso.

## ?? Validaciones realizadas
- El Key Vault está correctamente desplegado.
- Los secretos se almacenan de forma segura.
- Los permisos cumplen mínimo privilegio.
- No existen accesos directos innecesarios.
- Las auditorías registran accesos correctamente.

## ?? Problemas encontrados
- Un rol tenía permisos excesivos sobre secretos.
- Un usuario podía listar claves sin necesidad operativa.

## ??? Soluciones aplicadas
- Ajuste de roles para cumplir mínimo privilegio.
- Eliminación de permisos de listado innecesarios.
- Revisión completa de asignaciones.

## ?? Implicaciones de seguridad
- Un Key Vault mal configurado puede exponer secretos críticos.
- El listado de secretos es tan sensible como leerlos.
- Los accesos deben revisarse periódicamente.
- Los secretos deben rotarse según buenas prácticas.

## ?? Recursos útiles (opcionales)
- Microsoft Learn — Key Vault Overview
- OWASP Secrets Management
- Azure RBAC Documentation

## ?? Comandos utilizados (opcionales)
_No aplica._

## ?? Comandos pendientes (opcionales)
_No aplica._
