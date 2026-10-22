# Matriz de cumplimiento y controles

> **Estado:** documentado. No es una certificación ni una auditoría. Mapea controles técnicos del portfolio a marcos de referencia para facilitar la conversación con equipos de seguridad, arquitectura y compliance.

> **En fácil:** la matriz cruza lo que se ha practicado con los controles que piden los marcos de seguridad. Sirve para ver qué está probado, qué a medias y qué falta, y para recordar que esto no es una certificación.

## Objetivo

Traducir el trabajo técnico del portfolio a un lenguaje de control: qué marco cubre cada práctica, qué evidencia existe y qué queda pendiente. La matriz evita dos errores frecuentes: afirmar cumplimiento sin evidencia y tratar un laboratorio como un sistema certificado.

## Cómo leer la matriz

- **Cubierto:** existe una práctica, código o configuración que aborda el control.
- **Parcial:** hay un control parcial o falta evidencia de ejecución.
- **Pendiente:** no hay implementación ni evidencia.
- **No aplica:** el control no corresponde al alcance del laboratorio.

La evidencia enlaza al módulo o al repositorio de la API. Cuando la columna indica **IA local**, la evidencia vive en `ai-agent-local-lab`; cuando indica **API**, en `lab-api-local-azure`.

## Matriz principal

| Marco / control | Descripción | Módulo | Evidencia | Estado |
|---|---|---|---|---|
| **MCSB IM-1** | Protección de credenciales y secretos | 02, 07 | Key Vault, Managed Identity, Gitleaks | Cubierto |
| **MCSB IM-2** | Gestión de identidades privilegiadas | 02, 06 | PIM, RBAC, Access Reviews | Cubierto |
| **MCSB IA-2** | MFA | 02, 06 | MFA, Passwordless, Conditional Access | Cubierto |
| **MCSB PA-1** | Mínimo privilegio | 02, 06, 08 | RBAC, PIM, NSG | Cubierto |
| **MCSB PA-7** | Separación de funciones | 02 | Matriz RBAC | Cubierto |
| **MCSB DP-1** | Protección de datos sensibles | 02 | Key Vault, RBAC | Cubierto |
| **MCSB DP-3** | Cifrado en tránsito | 01, 08 | HTTPS/TLS, JWT | Cubierto |
| **MCSB NS-1** | Segmentación de red | 08 | VNet/NSG/Private Endpoint (IaC) | Parcial: no desplegado |
| **MCSB NS-2** | Acceso privado a servicios | 08 | Private Endpoints (IaC) | Parcial: no desplegado |
| **MCSB PV-2** | Análisis de vulnerabilidades | 07 | CodeQL | Parcial: ejecución remota pendiente |
| **MCSB PV-3** | Gestión de dependencias | 07 | Trivy SCA | Cubierto |
| **MCSB DS-1** | Seguridad del desarrollo | 07 | Protección de ramas, IaC | Cubierto |
| **MCSB DS-2** | DevSecOps / pipelines | 07 | Workflow con gates | Cubierto |
| **MCSB IR-1** | Integridad del historial | 07 | Branch protection | Cubierto con bypass de admin |
| **MCSB IR-2** | Detección y respuesta | 09, 12 | KQL, playbook | Parcial: no ejecutado |
| **MCSB LT-1** | Registro y auditoría | 09, 12 | Diagnóstico, Log Analytics | Parcial: no desplegado |
| **NIS2 art. 21** | Gestión de riesgos y controles técnicos | 02, 07, 08, 09, 12 | Módulos y matriz | Parcial: laboratorio, no sistema real |
| **NIS2 art. 23** | Notificación de incidentes | 12 | Playbook | Diseño |
| **ENS mp.info.1** | Protección de la información | 02, 08 | Key Vault, Private Endpoint | Parcial |
| **ENS op.exp.2** | Gestión de incidentes | 12 | Playbook | Diseño |
| **ENS op.mon.1** | Monitorización | 09, 12 | KQL, diagnóstico | Parcial |
| **CIS Azure 1.x** | Identidad y acceso | 02, 06 | MFA, PIM, RBAC | Cubierto |
| **CIS Azure 6.x** | Redes | 08 | NSG, Private Endpoint | Parcial |
| **CIS Azure 8.x** | Key Vault | 02 | RBAC, purge protection | Cubierto |
| **OWASP API1** | BOLA | 11 | Pruebas y remediación | Cubierto localmente |
| **OWASP API2** | Broken Authentication | 01, 11 | JWT, pruebas | Parcial |
| **OWASP API3** | Mass Assignment | 11 | DTOs, pruebas | Cubierto |
| **OWASP API4** | Resource Consumption | 11 | Rate limit, límites | Parcial |
| **OWASP API5** | BFLA | 11 | Revisión | Pendiente |
| **OWASP API8** | Misconfiguration | 07, 08, 11 | CORS, headers, contenedor | Parcial |
| **OWASP LLM01** | Prompt Injection | IA local, 11 | Conjunto dorado, pruebas de inyección y matriz de perturbación | Diseño: sin ejecución |
| **OWASP LLM02** | Salida no confiable | API | Validación de esquema y *fallback* determinista | Diseño |
| **OWASP LLM07** | Fuga del prompt de sistema | IA local | Canario de fuga (C2) | Diseño |
| **OWASP LLM10** | Consumo ilimitado | API, 11 | Límite de tokens, cuota y alerta | Parcial: rate limit de laboratorio, sin gateway de IA |
| **ISO 27001 A.8** | Gestión de activos | 03 | Auditoría | Parcial |
| **ISO 27001 A.12** | Operaciones | 09, 12 | Monitorización | Parcial |
| **ISO 27001 A.14** | Desarrollo seguro | 07, 11 | DevSecOps, pruebas | Cubierto |

## Evidencia por repositorio

| Repositorio | Evidencia principal | Estado |
|---|---|---|
| `portfolio-ciberseguridad-lorenzo` | Módulos 01–12, bitácoras, prácticas y 7 evidencias indexadas | Documentado; 3 evidencias de ejecución y 4 documentales o verificables |
| `lab-api-local-azure` | Código, tests, CI, Bicep | Implementado y probado localmente |
| `ai-agent-local-lab` | Laboratorio local-first, evaluación y robustez de prompts | Documentado |
| `lanuzalorenzo` | Perfil profesional | Publicado |
| `lanuzalorenzo.github.io` | Portfolio web | Publicado |

Las evidencias (3 de ejecución y 4 documentales o verificables) están registradas en el [índice de evidencias](../docs/laboratorio-final/evidencias/README.md).

## Brechas declaradas

1. **Sin auditoría externa:** la matriz no sustituye una certificación.
2. **Sin despliegue completo:** Bicep, APIM, Sentinel y Storage no se han desplegado.
3. **Sin evidencias de producción:** los datos son de laboratorio.
4. **Sin autorización granular:** scopes/roles pendientes en la API.
5. **Sin tabletop:** el playbook no se ha ejercitado.
6. **Sin medición de tiempos:** detección, contención y recuperación no están medidas.
7. **Sin SBOM ni firma de artefactos:** línea de trabajo DevSecOps.
8. **Sin evidencias de IA:** la integración, la evaluación y la robustez de LLM están diseñadas y no ejecutadas; las filas **OWASP LLM** reflejan diseño, no validación.

## Próximos pasos

- Convertir cada «Parcial» en una prueba ejecutada y enlazada.
- Añadir un registro de evidencias con fecha, entorno y resultado.
- Revisar la matriz contra la versión vigente de cada marco.
- Separar controles de laboratorio de controles de producción en la narrativa.

## Aviso

Esta matriz es una herramienta de comunicación técnica. No constituye asesoramiento legal, certificación ni declaración de conformidad.
