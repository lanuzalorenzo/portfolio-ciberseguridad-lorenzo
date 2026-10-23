# Informe técnico — RBAC y minimización de privilegios

**Módulo:** 06 — Privileged Access & Identity Governance  
**Práctica:** 03 — RBAC y minimización de privilegios

## Contexto y objetivo

Los permisos excesivos son una de las principales causas de impacto en incidentes de seguridad. Cuando un usuario o servicio tiene acceso más amplio del necesario, cualquier error o credencial comprometida puede ampliarse a múltiples recursos y servicios.

Esta práctica reforza la seguridad de acceso mediante un modelo basado en roles, con alcance preciso y revisiones periódicas del acceso concedido.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Mínimo privilegio** | Conceder solo lo estrictamente necesario | Reduce impacto de incidentes |
| **Ámbito acotado** | Limitar permisos a un grupo de recursos concreto | Mejora control y gestión |
| **Revisión periódica** | Revisar accesos no utilizados | Elimina privilegios innecesarios |
| **Separación de funciones** | Evitar que una persona tenga todo el control | Mejora resiliencia y governance |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **RBAC por rol** | Sí | Control claro y auditable |
| **Grupos de acceso** | Recomendado | Simplifica administración |
| **Ámbito mínimo** | Sí | Limita superficie de acceso |
| **Revisiones periódicas** | Obbligatorias | Mantiene permiso alineado con la necesidad |

## Implementación técnica recomendada

1. Mapear los roles operativos necesarios.
2. Agrupar usuarios por perfiles de acceso.
3. Asignar roles con el ámbito más pequeño posible.
4. Evitar permisos globales cuando no sean estrictamente necesarios.
5. Revisar periódicamente los accesos activos.
6. Eliminar permisos no utilizados o duplicados.

## Riesgos mitigados

- Over-privileging de usuarios y servicios.
- Impacto ampliado en incidentes de seguridad.
- Acceso no justificado a recursos críticos.
- Falta de trazabilidad y control de acceso.

## Conclusión

El control de permisos mediante RBAC no es solo una buena práctica administrativa; es un eje central de la protección del entorno y de la reducción del riesgo operativo.
