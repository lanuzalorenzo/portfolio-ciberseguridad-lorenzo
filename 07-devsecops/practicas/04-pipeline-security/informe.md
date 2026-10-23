# Informe técnico — Pipeline segura por defecto y validación de entregas

**Módulo:** 07 — DevSecOps y gobernanza del software  
**Práctica:** 04 — Pipeline segura por defecto y validación de entregas

## Contexto y objetivo

Una pipeline mal diseñada puede convertir un cambio de software en una puerta de entrada para despliegues inseguros, ejecuciones no autorizadas o exposición de secretos. La seguridad del pipeline no se limita a ejecutar pruebas, sino a controlar permisos, autenticación, validación por entorno y condiciones de aprobación.

Esta práctica busca establecer un modelo seguro por defecto para la entrega continua, en el que cada release solo pueda producirse si cumple las condiciones mínimas de calidad, trazabilidad y control de acceso.

## Principios de la práctica

| Principio | Descripción | Beneficio |
| :--- | :--- | :--- |
| **Permisos mínimos** | No conceder más privilegios de los necesarios | Reduce impacto de abuso o errores |
| **Autenticación sin secretos fijos** | OIDC o identidades federadas | Evita credenciales persistentes |
| **Validación por gates** | Bloquear entregas con fallos o riesgo | Mejora la calidad de la entrega |
| **Entornos protegidos** | Asegurar aprobación por entorno | Reduce riesgo de despliegues no controlados |
| **Trazabilidad** | Registrar ejecuciones y decisiones | Facilita auditoría y response |

## Configuración recomendada

| Política | Valor recomendado | Rationale |
| :--- | :--- | :--- |
| **OIDC / federación** | Recomendado | Evita secretos de larga duración |
| **Permisos mínimos** | Sí | Menor superficie de ataque |
| **Validación de artefactos** | Obligatoria | Rechaza entregas defectuosas |
| **Aprobación por entorno** | Sí | Control de despliegue por etapa |
| **Status checks** | Obligatorios | Garantiza que no se publican cambios no validados |

## Implementación técnica recomendada

1. Usar identidades federadas para la autenticación del pipeline.
2. Reducir permisos al mínimo necesario por entorno y tarea.
3. Ejecutar validaciones de compilación, pruebas y análisis antes del despliegue.
4. Rechazar artefactos con fallos o riesgos críticos.
5. Definir entornos protegidos y requerir aprobación manual si aplica.
6. Registrar cada ejecución para evidenciar la trazabilidad del proceso.

## Riesgos mitigados

- Uso excesivo de privilegios y lateral movement dentro del pipeline.
- Despliegues no controlados o con artefactos defectuosos.
- Exposición de credenciales persistentes.
- Falta de trazabilidad frente a incidentes de seguridad.

## Conclusión

Una pipeline segura por defecto no solo acelera la entrega; también reduce el riesgo de ejecutar software comprometido, con permisos excesivos o sin validación adecuada. Es un componente clave de la estrategia DevSecOps.
