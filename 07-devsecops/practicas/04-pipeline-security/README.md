# 04 | Pipeline segura por defecto y validación de entregas

## Descripción del escenario y objetivo de seguridad

**Escenario:** Pipeline de integración continua y despliegue que ejecuta cambios sin comprobaciones suficientes, con permisos excesivos, accesos no minimizados y validaciones insuficientes antes de publicar artefactos.  
**Objetivo de seguridad:** Diseñar una pipeline segura por defecto en la que cada cambio se valora, autoriza y ejecuta con permisos mínimos y controles de seguridad predefinidos.  
**Alcance:** CI/CD del repositorio, artefactos generados, entornos de despliegue, autenticación, gestión de permisos y gates de validación.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de seguridad considerados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Pipeline CI/CD** | Orquestación de validación y entrega | Validación automática antes del despliegue. |
| **Identidad federada / OIDC** | AuthN sin secretos estáticos | Menor riesgo de credenciales persistentes. |
| **Permisos mínimos** | Control de acceso por rol y alcance | Reduce impacto de abuso de privilegios. |
| **Gates de calidad** | Validación de builds, tests y seguridad | Bloqueo de entregas no conformes. |
| **Entornos protegidos** | Control de despliegue por entorno | Aprobar solo releases con criterios claros. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Permisos mínimos | Uso de roles y alcance acotado | OIDC y políticas de acceso | MCSB DS-2 |
| Validación de releases | Gates de CI/CD para pruebas y análisis | Rechazo automático por fallos | MCSB DS-1 |
| Protección de entornos | Aprobar despliegues por etapa | Protección del entorno y revisión | MCSB GS-2 |
| Eliminar secretos estáticos | Usar credenciales efímeras y federadas | Policy-as-code y secretos gestionados | MCSB IM-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Validación de build | Ejecución de pipeline con cambios | Error si falla el proceso | Sí |
| Permisos mínimos | Revisar credenciales y roles | Permisos restringidos | Sí |
| Protección de entorno | Validación de deploy con aprobación | Despliegue sólo con control | Sí |
