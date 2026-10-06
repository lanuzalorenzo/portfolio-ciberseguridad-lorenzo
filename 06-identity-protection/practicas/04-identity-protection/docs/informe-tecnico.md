# Informe técnico — Identity Protection y revisiones de acceso

**Módulo:** 06 — Privileged Access & Identity Governance  
**Práctica:** 04 — Identity Protection y revisiones de acceso

## Contexto y objetivo

Aunque la autenticación y la autorización sean elementos centrales del control de identidad, una postura robusta también requiere detectar riesgo, revisiones continuas y respuesta ante cambios inusuales. 

Esta práctica documenta cómo Microsoft Entra ID puede evaluar riesgo de autenticación, activar mitigaciones y mantener revisiones periódicas de acceso para cerrar brechas que no se perciben en un análisis inicial.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Detección de riesgo** | Evaluar actividad sospechosa o credenciales comprometidas | Mejora respuesta ante señales de ataque |
| **Governance de accesos** | Revisar roles y permisos con periodicidad | Reduce permisos obsoletos |
| **Mitigación inmediata** | Bloqueo o desafío ante riesgo alto | Limita daño potencial |
| **Evidencia y trazabilidad** | Registro de revisiones y accesos | Facilita cumplimiento y auditoría |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **Identity Protection** | Activado | Detecta riesgo y reduce amenazas de identidad |
| **Access reviews** | Periódicas | Validan la necesidad del acceso |
| **Mitigación por riesgo** | Automated | Respuesta rápida ante actividad sospechosa |
| **Revisiones de roles privilegiados** | Obligatorias | Reduce exposición por permisos obsoletos |

## Implementación técnica recomendada

1. Habilitar Identity Protection y revisar riesgo de usuario, sesión y sign-in.
2. Definir políticas de mitigación para riesgo alto y medio.
3. Establecer revisiones periódicas para roles de alto valor.
4. Revisar accesos con permisos antiguos o no utilizados.
5. Eliminar o redefinir accesos que no sigan la necesidad operativa.
6. Registrar decisiones y resultados para auditoría.

## Riesgos mitigados

- Cuentas comprometidas con riesgo no detectado.
- Acceso privilegiado persistente sin revisión.
- Uso de credenciales o sesiones sospechosas.
- Deterioro de la posture de identidad por falta de governance.

## Conclusión

La seguridad de identidad no termina con la autentificación. La protección de la identidad exige detección de riesgo, revisión del acceso y gobernanza continua de privilegios para mantener un entorno resiliente y controlado.
