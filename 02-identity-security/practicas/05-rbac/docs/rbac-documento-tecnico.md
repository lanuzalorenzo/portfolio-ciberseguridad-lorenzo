# ?? Ejercicio 05 — RBAC  
## Documento técnico  
## Módulo 2 — Identity Security

## ?? Contexto (atemporal)
Este ejercicio forma parte del Módulo 2 de Identity Security y se centra en el diseño y aplicación del modelo RBAC (Role-Based Access Control).  
El objetivo es comprender cómo se definen roles, permisos y asignaciones dentro de un sistema de identidad, aplicando buenas prácticas de seguridad y evitando configuraciones inseguras.

## ?? Objetivo
Implementar un modelo RBAC básico que permita:
- Definir roles funcionales.  
- Asociar permisos a cada rol.  
- Asignar roles a usuarios.  
- Validar que los permisos se aplican correctamente.  
- Detectar configuraciones inseguras o inconsistentes.

## ?? Trabajo realizado (cronológico y técnico)
1. Revisión del GUION del módulo.  
2. Diseño del modelo RBAC.  
3. Validación del modelo.  
4. Revisión de implicaciones de seguridad.

## ?? Validaciones realizadas
- Verificación de roles y permisos.  
- Validación de mínimo privilegio.  
- Comprobación de permisos no asignados directamente a usuarios.

## ?? Problemas encontrados
- Permisos excesivos en roles operativos.  
- Falta de separación de funciones.

## ??? Soluciones aplicadas
- Ajuste de permisos del rol operador.  
- Corrección del rol auditor.  
- Revisión completa de asignaciones.

## ?? Implicaciones de seguridad
- Riesgo de escalada de privilegios.  
- Necesidad de separación de funciones.  
- Revisión periódica de roles.

## ?? Recursos útiles (opcionales)
- NIST RBAC Standard  
- OWASP ASVS  
- Microsoft Entra ID RBAC

## ?? Comandos utilizados (opcionales)
_No aplica._

## ?? Comandos pendientes (opcionales)
_No aplica._
