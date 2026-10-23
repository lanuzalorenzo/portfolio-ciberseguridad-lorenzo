# Informe técnico — Conditional Access y MFA adaptativo

**Módulo:** 06 — Privileged Access & Identity Governance  
**Práctica:** 01 — Conditional Access y MFA adaptativo

## Contexto y objetivo

El acceso a recursos críticos no debe estar basado únicamente en una contraseña. En un entorno moderno, la identidad debe evaluarse según contexto: ubicación, dispositivo, riesgo de sesión y tipo de aplicación. 

Esta práctica documenta la activación de políticas de acceso condicional y MFA adaptativo para reforzar la autenticación, especialmente en escenarios con riesgo medio o alto.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Contexto de acceso** | Evaluar comportamiento, ubicación y dispositivo | Reduce decisiones homogéneas |
| **MFA adaptativo** | Reforzar la validación según riesgo | Mejora resistencia a credenciales comprometidas |
| **Postura de seguridad** | Restringir accesos sensibles por condiciones | Aumenta control y minimización de riesgo |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **MFA para usuarios privilegiados** | Obligatorio | Reduce riesgo de acceso comprometido |
| **Acceso condicional por dispositivo** | Requerido para recursos críticos | Mejora control del endpoint |
| **Bloqueo por ubicación no confiable** | Sí | Limita acceso desde ubicaciones sospechosas |
| **Sign-in risk** | Habilitado | Detecta accesos de riesgo |

## Implementación técnica recomendada

1. Revisar usuarios y grupos sensibles.
2. Crear políticas de Conditional Access para aplicaciones críticas.
3. Exigir MFA para usuarios con acceso privilegiado.
4. Bloquear acceso desde ubicaciones o dispositivos no conformes.
5. Revisar sign-ins con riesgo y reforzar medidas de acceso.

## Riesgos mitigados

- Uso de credenciales robadas.
- Acceso desde redes o dispositivos no fiables.
- Sesiones sospechosas o compromisos de identidad.
- Exposición de datos sensibles por accesos excesivos.

## Conclusión

Conditional Access y MFA adaptativo convierten la identidad en una decisión de contexto, no en un simple requisito de inicio de sesión. Es una capa esencial de la seguridad moderna.
