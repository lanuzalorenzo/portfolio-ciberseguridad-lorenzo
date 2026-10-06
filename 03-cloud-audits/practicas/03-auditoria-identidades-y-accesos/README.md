# 03 | Auditoría de Identidades, Roles y Accesos en Microsoft Entra ID

## Descripción del escenario y objetivo de seguridad

**Escenario:** Tenant de Microsoft Entra ID y suscripciones de Azure donde convergen cuentas de usuario internas, colaboradores externos (B2B/Guest) y registros de aplicaciones (Service Principals) con asignaciones de roles acumuladas en el tiempo.  
**Objetivo de seguridad:** Ejecutar una auditoría exhaustiva sobre el plano de identidad para identificar identidades inactivas o huérfanas, excesos de privilegios administrativos, credenciales de aplicaciones de larga duración y ausencia de factores de autenticación fuerte.  
**Alcance:** Directorio Microsoft Entra ID de laboratorio, usuarios miembros, invitados, roles de directorio y Service Principals.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra ID** | Proveedor de Identidad central | Gestión de usuarios, grupos, roles de directorio y aplicaciones registradas. |
| **Entra ID Roles** | Asignaciones de privilegios globales | Revisión de roles como *Global Administrator*, *Privileged Role Administrator* y *User Administrator*. |
| **Cuentas de Invitado (B2B)** | Identidades externas colaboradoras | Auditoría de cuentas `@external.com` inactivas o con privilegios asignados. |
| **App Registrations / Service Principals** | Identidades de aplicaciones y automatizaciones | Inspección de certificados y *client secrets* asociados, vigencia y permisos delegados o de aplicación. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Mapeo y reducción de Global Administrators | Limitar cuentas con administración total a un máximo de 2-4 | Revisión periódica de IAM en Entra ID | MCSB PA-1 / CIS 1.2 |
| Ciclo de vida y caducidad de secretos de apps | Prohibir secretos con duración mayor a 6-12 meses | Auditoría de *App Registrations* | MCSB PA-6 / CIS 1.14 |
| Detección de cuentas huérfanas o inactivas | Identificación de usuarios sin inicio de sesión en >90 días | Logs de inicio de sesión (*Sign-in logs*) | MCSB IA-1 / NIST AC-2 |

**Artefactos relacionados:** [Informe técnico de auditoría de identidades y accesos](docs/auditoria-identidades-y-accesos-documento-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Conteo y revisión de Global Administrators | Filtro en *Microsoft Entra roles* | Sin asignaciones permanentes descontroladas | PASS: Identificadas cuentas asignadas; se recomendó conversión a elegibles vía PIM |
| Auditoría de caducidad en secretos de Service Principals | Inspección de *Certificates & Secrets* en apps | Secretos vigentes y con caducidad no superior a 1 año | PASS: Detectado secreto sin caducidad; se recomendó rotación y uso de Managed Identities |
| Revisión de cuentas Guest con roles privilegiados | Filtro por `userType == 'Guest'` en asignaciones de roles | Ningún usuario invitado con roles administrativos | PASS: Cero asignaciones privilegiadas a cuentas externas |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **PA-1: Protección de cuentas privilegiadas** | Eliminación de asignaciones permanentes | Ningún usuario humano debe operar como Administrador Global permanente para tareas diarias. |
| **PA-6: Gestión de credenciales de aplicaciones** | Reemplazo de secretos estáticos por identidades administradas | Los secretos de aplicaciones representan un vector silencioso de persistencia si no se audita su fecha de expiración y alcance de permisos. |

- Complementar las auditorías manuales con revisiones de acceso automatizadas (*Access Reviews*) en Entra ID Governance es esencial para revocar privilegios a usuarios o invitados que abandonan proyectos.