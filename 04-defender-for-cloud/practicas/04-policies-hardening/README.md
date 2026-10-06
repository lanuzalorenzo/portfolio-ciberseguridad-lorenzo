# 04 | Políticas de Seguridad y Hardening Preventivo con Azure Policy

## Descripción del escenario y objetivo de seguridad

**Escenario:** Suscripción de laboratorio sin directivas de seguridad declarativas asignadas, lo que permite la creación de recursos con configuraciones inseguras por defecto (acceso público, cifrado deshabilitado, puertos abiertos) sin mecanismo de bloqueo ni auditoría sistemática.
**Objetivo de seguridad:** Implementar directivas de seguridad preventivas y de auditoría mediante Azure Policy e iniciativas regulatorias en Defender for Cloud, aplicando el modelo de hardening declarativo (*policy-as-code*) para asegurar que la postura de seguridad sea mantenible y auditada de forma continua.
**Alcance:** Suscripción de laboratorio en Azure, panel de *Security policy* en Defender for Cloud y directivas individuales y agrupadas en iniciativas.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Azure Policy** | Motor declarativo de cumplimiento y governance | Directivas individuales y agrupadas en iniciativas asignadas a la suscripción. |
| **Iniciativa Microsoft Cloud Security Benchmark** | Conjunto de controles de referencia de seguridad cloud | Asignada en Defender for Cloud como baseline de auditoría. |
| **Defender for Cloud — Security policy** | Integración de Azure Policy con CSPM | Panel unificado de iniciativas regulatorias y cumplimiento. |
| **Policy Effect: AuditIfNotExists / Deny** | Modos de aplicación de directivas | *Audit* para visibilidad sin bloqueo; *Deny* para prevención activa de configuraciones inseguras. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Asignación de iniciativa MCSB | Iniciativa *Microsoft Cloud Security Benchmark* asignada en *Security policy* | Iniciativa regulatoria en Defender for Cloud | MCSB GS-2 |
| Prevención de almacenamiento con acceso público | Directiva *Deny* para `allowBlobPublicAccess = true` | Azure Policy en modo *Deny* | MCSB DP-4 / CIS 3.7 |
| Auditoría de forzado de TLS | Directiva *AuditIfNotExists* sobre versión mínima TLS en Storage | Azure Policy en modo *Audit* | MCSB DP-3 |
| Alerta sobre recursos sin diagnósticos configurados | Directiva *AuditIfNotExists* para *Diagnostic Settings* | Azure Policy + Log Analytics | MCSB LT-1 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Asignación de iniciativa MCSB visible en Defender for Cloud | Verificación en *Environment settings* → *Security policy* | Iniciativa listada como activa con porcentaje de cumplimiento | PASS: Iniciativa presente y evaluando recursos de la suscripción |
| Intento de creación de Storage Account con acceso público (Deny) | Despliegue de recurso desde Azure Portal con `allowBlobPublicAccess = true` | Error de denegación por directiva activa | PASS: Azure Policy bloquea la operación antes de aprovisionar el recurso |
| Verificación de recursos marcados como no conformes (Audit) | Panel *Compliance* en Azure Policy | Recursos listados con estado *Non-compliant* | PASS: Recursos sin TLS 1.2 marcados para remediación |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **GS-2: Gestión de la postura de seguridad cloud** | Asignación de iniciativa MCSB como baseline | La combinación de directivas en modo *Audit* e iniciativas regulatorias proporciona visibilidad de cumplimiento sin interrumpir operaciones existentes. |
| **DP-4: Protección de datos en reposo** | Directiva *Deny* de acceso público en Storage | Las directivas en modo *Deny* son la única garantía real de prevención; el modo *Audit* solo alerta, pero no impide la configuración insegura. |

- Desplegar primero directivas en modo *Audit* y migrar a *Deny* tras validar que no bloquea flujos legítimos es la práctica estándar para minimizar interrupciones operativas durante la adopción.
