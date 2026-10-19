# Laboratorio final

> **Estado:** diseño y planificación. No hay recursos Azure desplegados ni evidencias de ejecución asociadas todavía.
>
> Este documento define el marco común. El estado real de cada control se consulta en el README de su módulo y en el [índice de evidencias](evidencias/README.md).

## Objetivo

El laboratorio final conecta los módulos del portfolio sobre una única carga de trabajo: [**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure). La intención es demostrar un modelo de defensa en profundidad coherente, no una colección de prácticas aisladas.

Cada capa debe poder activarse, validarse y retirarse de forma controlada. El resultado esperado es un recorrido reproducible:

1. Diseñar la arquitectura y sus límites de confianza.
2. Ejecutar el runbook en un entorno controlado.
3. Capturar evidencia redactada.
4. Declarar el estado real: **Validado**, **Parcial**, **Runbook preparado**, **Diseño** o **Pendiente**.
5. Destruir los recursos temporales y registrar el coste.

## Alcance

| Capa | Componentes previstos | Estado de referencia |
|---|---|---|
| Workload | API .NET, DTOs, autorización por propietario, tests | **Validado en CI** para el workload; integración Azure no desplegada |
| Identidad | Entra ID, OAuth 2.0/PKCE, JWT/JWKS, RBAC, Managed Identities | Ver módulos [01](../../01-seguridad-azure/README.md), [02](../../02-identity-security/README.md) y [06](../../06-identity-protection/README.md) |
| Red | VNet, subredes, NSG, Private Endpoints, DNS privado | **Diseño + IaC validada estáticamente** en el [módulo 08](../../08-seguridad-red-azure/README.md) |
| Datos y secretos | Key Vault, Storage, acceso privado | **Diseño** |
| Observabilidad | Log Analytics, Application Insights, diagnóstico | **Diseño** |
| Detección y respuesta | Defender for Cloud, Sentinel, KQL, playbooks | **Diseño**; ver módulos [04](../../04-defender-for-cloud/README.md), [05](../../05-defender-suite/README.md) y [09](../../09-microsoft-sentinel/README.md) |
| Validación ofensiva | OWASP API Top 10, BOLA/BFLA, mass assignment | **Parcial**: pruebas locales en el [módulo 11](../../11-hacking-etico-api/README.md) |
| Forense | Recolección, integridad, timeline, cadena de custodia | **Diseño**; ver [módulo 12](../../12-forense-cloud-respuesta/README.md) |
| Laboratorio local | ELK, logs sintéticos, dashboards | **Diseño**; ver [módulo 10](../../10-elk-stack-security/README.md) |

## Reparto de repositorios

| Repositorio | Responsabilidad |
|---|---|
| `portfolio-ciberseguridad-lorenzo` | Arquitectura, runbooks, plantillas, evidencias y narrativa. |
| `lab-api-local-azure` | Código, tests, Dockerfile, CI e IaC del workload. |
| `ai-agent-local-lab` | Laboratorio de IA independiente; no forma parte del laboratorio de seguridad. |

No se crea un repositorio nuevo para el laboratorio en esta fase: el diseño, los runbooks y las evidencias pueden mantenerse aquí. Una capa de plataforma reutilizable solo se extraería si el IaC compartido crece hasta justificarlo.

## Documentos

- [Arquitectura de referencia](arquitectura.md): capas, flujos, límites de confianza y orden de activación.
- [Plan de ejecución](plan-ejecucion.md): fases, requisitos, gates, costes y limpieza.
- [Índice de evidencias](evidencias/README.md): qué se ha ejecutado y dónde está la prueba.
- [Plantilla de runbook](../../plantillas/runbook-template.md).
- [Plantilla de evidencia](../../plantillas/evidencia-template.md).

## Estados

| Estado | Significado |
|---|---|
| **Validado** | Ejecutado con evidencia enlazada. |
| **Parcial** | Ejecutado en parte, con brechas declaradas. |
| **Runbook preparado** | Pasos y comandos escritos, todavía no ejecutados. En resúmenes públicos se muestra como «Diseño · runbook listo». |
| **Diseño** | Arquitectura y decisiones documentadas; no hay runbook ejecutable. |
| **Pendiente** | Identificado y no iniciado. |

Un runbook preparado no es una validación.

## Reglas del laboratorio

- Los despliegues Azure requieren autorización explícita, suscripción de laboratorio, presupuesto, resource group temporal, datos sintéticos y plan de limpieza.
- No se ejecuta nada en producción ni con datos reales.
- Cada comando no ejecutado se marca como **no ejecutado**.
- Cada evidencia elimina secretos, direcciones IP internas, identificadores reales y datos personales.
- Los estados de los módulos, la web, el perfil y la matriz de cumplimiento deben coincidir.

## Próximo paso

Convertir el módulo 10 (ELK) en el primer runbook ejecutable y registrar su evidencia. Después, repetir el patrón con el tabletop forense del módulo 12 antes de pasar a Azure.
