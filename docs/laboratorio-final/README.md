# Laboratorio final

> **Estado:** tres evidencias de ejecución (ELK, módulo 10; BOLA/BFLA, módulo 11; tabletop forense, módulo 12) y cuatro documentales o verificables (02, 03, 04 y 07). Las fases Azure siguen pendientes de autorización y presupuesto; no hay recursos Azure desplegados.
>
> Este documento define el marco común. El estado real de cada control se consulta en el README de su módulo y en el [índice de evidencias](evidencias/README.md).

> **En fácil:** el laboratorio es una casa con varias cerraduras: la puerta de entrada (red), la llave (identidad), lo que se guarda dentro (datos) y la cámara que graba (logs). Se practica cerradura a cerradura, primero en local y sin coste, y no se abre la siguiente hasta que la anterior tiene prueba.

## Objetivo

El laboratorio final conecta los módulos del portfolio sobre una única carga de trabajo: [**EcommerceApi**](https://github.com/lanuzalorenzo/lab-api-local-azure). El objetivo es defensa en profundidad sobre una sola aplicación, no una colección de prácticas aisladas.

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
| Validación ofensiva | OWASP API Top 10, BOLA/BFLA, mass assignment | **Validado en local**: aislamiento de pedidos y mass assignment; pentest desplegado pendiente. Ver [módulo 11](../../11-hacking-etico-api/README.md) y su [evidencia](evidencias/2026-10-21-11-api-bola/README.md) |
| Forense | Recolección, integridad, timeline, cadena de custodia | **Diseño**; ver [módulo 12](../../12-forense-cloud-respuesta/README.md) |
| Laboratorio local | ELK, logs sintéticos, dashboards | **Validado en local**; ver [módulo 10](../../10-elk-stack-security/README.md) y su [evidencia](evidencias/2026-10-19-10-elk-ingesta/README.md) |

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

El módulo 10 (ELK) y la validación local del módulo 11 están registrados en el índice de evidencias. El siguiente paso es convertir el tabletop forense del módulo 12 en un runbook ejecutable y registrar su acta antes de pasar a Azure.
