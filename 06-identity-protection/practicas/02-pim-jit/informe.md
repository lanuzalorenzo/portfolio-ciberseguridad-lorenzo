# Informe técnico — PIM y acceso Just-In-Time

**Módulo:** 06 — Privileged Access & Identity Governance  
**Práctica:** 02 — PIM y acceso Just-In-Time

## Contexto y objetivo

Los permisos de administración son una de las áreas más sensibles dentro de la identidad. Cuando un rol privilegiado está activo de manera permanente, la superficie de riesgo aumenta considerablemente ante abuso, errores o sesiones comprometidas.

Esta práctica documenta cómo Microsoft Entra ID PIM permite asignar permisos en un modelo temporal, con justificación, aprobación y revisión periódica, reduciendo la exposición sin impedir la operatividad del entorno.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Mínimo privilegio dinámico** | Los permisos se activan solo cuando se necesitan | Reduce exposición continua |
| **Aprobación de activación** | Toda acción de elevación requiere validación | Mejora control y trazabilidad |
| **Tiempo acotado** | Los permisos existen durante un periodo concreto | Limita daño potencial |
| **Auditoría continua** | El acceso activado queda registrado | Facilita revisión y cumplimiento |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **PIM para roles críticos** | Activado | Reduce exposición permanente |
| **Justificación obligatoria** | Sí | Mejora trazabilidad de la elevación |
| **Aprobación por rol** | Requerida | Detecta usos no justificados |
| **Revisión periódica** | Sí | Elimina permisos innecesarios |

## Implementación técnica recomendada

1. Identificar roles con alto impacto y sensibilidad.
2. Habilitar PIM para esos roles y permisos.
3. Definir tiempos de activación y requisitos opcionales de aprobación.
4. Exigir justificación al activar un rol crítico.
5. Revisar periódicamente las asignaciones y los accesos activos.
6. Revocar permisos que ya no se necesiten.

## Riesgos mitigados

- Uso persistente de permisos administrators.
- Abuso de credenciales de alto valor.
- Duración prolongada de accesos no necesarios.
- Falta de trazabilidad en cambios de privilegio.

## Conclusión

PIM convierte los permisos privilegiados en un acceso temporal y controlado, reduciendo el riesgo sin comprometer la operatividad de la organización.
