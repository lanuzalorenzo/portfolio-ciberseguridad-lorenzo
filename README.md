<img src="assets/iconos/portfolio.svg" width="64" alt="Icono del portfolio de ciberseguridad">

# Lorenzo Lanuza | Portfolio de Ciberseguridad, DevSecOps y Arquitectura

Proteger un sistema es como asegurar una casa: no basta una cerradura, hacen falta puertas, rejas, alarma y alguien que sepa qué hacer si suena. Este portfolio aplica Security by Design, DevSecOps, Cloud Security y respuesta a incidentes sobre una misma familia de cargas —Comicteca, la aplicación principal, y EcommerceApi, su banco de pruebas— y recorre la **Defensa en Profundidad** capa a capa, separando lo probado de lo solo diseñado. Cada módulo responde a la misma pregunta: *¿qué control protege qué y cómo se demuestra?*

**In English.** Protecting a system is like securing a house: a lock is not enough —you need doors, bars, an alarm and someone who knows what to do when it goes off. This portfolio applies Security by Design, DevSecOps, Cloud Security and incident response to a single family of workloads —Comicteca, the main application, and EcommerceApi, its test bench— and walks through Defense-in-Depth layer by layer, separating what has been proven from what is only designed. Every module answers the same question: what does this control protect, and how is it demonstrated?

> Este repositorio describe laboratorios, código y documentación técnica. No representa despliegues de producción ni certificaciones. Cada práctica indica su estado: **Validado**, **Parcial**, **Runbook preparado**, **Diseño** o **Pendiente**. No se incluyen secretos, identificadores reales ni datos personales.

[![Portfolio CI](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo/actions/workflows/portfolio-ci.yml/badge.svg)](https://github.com/lanuzalorenzo/portfolio-ciberseguridad-lorenzo/actions/workflows/portfolio-ci.yml)

---

## Arquitectura de referencia

Hay dos cargas con papeles distintos. La principal es **Comicteca** (Blazor WebAssembly y API .NET 10 sobre SQLite en local), versionada en [`comicteca`](https://github.com/lanuzalorenzo/comicteca): es la aplicación principal; los controles compartidos llegan aquí después de estar en verde en el banco de pruebas, y lo que nace aquí sube a la plataforma cuando se generaliza. Comprueba que los controles compartidos se replican fuera del laboratorio —CORS cerrado por defecto, cabeceras y CSP, límite por IP, ProblemDetails, endpoint de salud, Docker sin root, CodeQL y Trivy sobre las imágenes— y que la validación de tokens está **Validada** en local y CI. El alta con la cuenta real sigue **Pendiente**. El conjunto está en **Parcial**, no se presenta como producto, y su despliegue sigue pendiente: la infraestructura y el asíncrono aún viven solo en el banco de pruebas.

El banco de pruebas es **EcommerceApi** (Web API .NET 10 con validación de tokens OAuth 2.0, DTOs, tests y pipeline DevSecOps), versionado en [`lab-api-local-azure`](https://github.com/lanuzalorenzo/lab-api-local-azure): ahí se estrena cada versión de los controles compartidos, el IaC y el diseño asíncrono, y de ahí salen las evidencias de los módulos.

Los controles transversales —CORS cerrado por defecto, validación JWT, cabeceras de seguridad, límite por IP, formato de error, HTTPS con HSTS y endpoint de salud— se extraen a paquetes NuGet en [`shared-dotnet`](https://github.com/lanuzalorenzo/shared-dotnet): los paquetes `0.1.0` están publicados en GitHub Packages y `EcommerceApi` y `Comicteca` los consumen desde el feed con permiso de solo lectura de paquetes.

![Defensa en profundidad: cinco capas, de la detección y respuesta en la parte superior a la arquitectura y AppSec en la base, con la validación ofensiva y el forense como ejes transversales](laboratorio-final/arquitectura-capas.svg)

---

## Módulos y estado

| # | Módulo | Estado |
|---|---|---|
| 01 | [OAuth 2.0, PKCE y JWT](01-seguridad-azure/README.md) | Parcial |
| 02 | [Identity Security](02-identity-security/README.md) | Validado (documental); práctica 08 en local; PIM parcial |
| 03 | [Cloud Audits](03-cloud-audits/README.md) | Validado (documental) |
| 04 | [Defender for Cloud](04-defender-for-cloud/README.md) | Validado (documental) |
| 05 | [Microsoft Defender Suite](05-defender-suite/README.md) | Diseño |
| 06 | [Acceso privilegiado](06-identity-protection/README.md) | Diseño |
| 07 | [DevSecOps y gobernanza](07-devsecops/README.md) | Validado en CI |
| 08 | [Seguridad de red en Azure](08-seguridad-red-azure/README.md) | Diseño + IaC estática |
| 09 | [Microsoft Sentinel](09-microsoft-sentinel/README.md) | Diseño |
| 10 | [ELK Stack Security](10-elk-stack-security/README.md) | Validado en local |
| 11 | [Hacking ético de APIs](11-hacking-etico-api/README.md) | Validado en local |
| 12 | [Forense cloud y respuesta](12-forense-cloud-respuesta/README.md) | Parcial |

**Criterio:** [Estados de validación](#estado-de-validación) — no se presenta un diseño como una validación.

---

## Qué leer primero

- **15 min:** [Guía de lectura](docs/guia-de-lectura.md) → [Índice de evidencias](laboratorio-final/evidencias/README.md) → tabla de estados arriba.
- **60–90 min (hilo identidad + API):** [Arquitectura](laboratorio-final/arquitectura.md) → [Módulo 01](01-seguridad-azure/README.md) → [Módulo 11](11-hacking-etico-api/README.md) + [evidencia BOLA](laboratorio-final/evidencias/2026-10-21-11-api-bola/README.md) → [Módulo 12](12-forense-cloud-respuesta/README.md) + [acta tabletop](laboratorio-final/evidencias/2026-10-22-12-tabletop/README.md).
- **Revisión técnica:** README → índice de evidencias → [módulo 11](11-hacking-etico-api/README.md) → [módulo 07](07-devsecops/README.md) → [Comicteca](https://github.com/lanuzalorenzo/comicteca) → [API reference](https://github.com/lanuzalorenzo/lab-api-local-azure).

---

## Laboratorio final

[Arquitectura](laboratorio-final/arquitectura.md) · [Plan de ejecución](laboratorio-final/plan-ejecucion.md) · [Herramientas](laboratorio-final/herramientas.md) · [Índice de evidencias](laboratorio-final/evidencias/README.md).

> Evidencias de ejecución y documentales, con fecha y resultado, en el [índice](laboratorio-final/evidencias/README.md). Fases Azure pendientes de autorización, presupuesto y resource group temporal; **no hay recursos Azure desplegados**.

---

## Estado de validación

| Estado | Significado |
|---|---|
| **Validado** | Ejecutado y con evidencia enlazada (de ejecución, documental o verificable). |
| **Parcial** | Implementado en código o configuración, pero sin ejecución completa o con brechas. |
| **Runbook preparado** | Pasos y comandos escritos, sin ejecutar. Se muestra como «Diseño · runbook listo». |
| **Diseño** | Arquitectura, procedimiento o IaC documentados; no desplegados. |
| **Pendiente** | Identificado y no iniciado. |

---

## Ecosistema

| Repositorio | Rol |
|---|---|
| **Portfolio** | Documentación, prácticas y narrativa (este repo) |
| **Aplicación principal** | Una aplicación de uso propio que recibe los controles ya probados —CORS, cabeceras y CSP, límite por IP, ProblemDetails, salud, Docker sin root, CodeQL y Trivy—, con la validación de tokens en verde en local y CI; el alta con la cuenta real, pendiente → [`comicteca`](https://github.com/lanuzalorenzo/comicteca) |
| **Banco de pruebas** | Código .NET, tests, CI y Bicep donde se estrena lo que después se aplica → [`lab-api-local-azure`](https://github.com/lanuzalorenzo/lab-api-local-azure) |
| **Aprendizaje en IA** | Guías de herramientas y agentes, experimentos medidos y criterios sobre qué datos salen de la red → [`lab-ia-aprendizaje`](https://github.com/lanuzalorenzo/lab-ia-aprendizaje) |
| **Automatización de CI** | Acciones y workflows compartidos: enlaces, anclas y compilación .NET → [`core`](https://github.com/lanuzalorenzo/core) |
| **Controles compartidos** | Paquetes NuGet con CORS, cabeceras, límite por IP, ProblemDetails y salud → [`shared-dotnet`](https://github.com/lanuzalorenzo/shared-dotnet) |
| **Plantillas de repositorio** | Esqueletos `dotnet new` con la línea base, CI y los controles compartidos → [`plantillas-dotnet`](https://github.com/lanuzalorenzo/plantillas-dotnet) |
| **Perfil** | Trayectoria y stack → [`lanuzalorenzo`](https://github.com/lanuzalorenzo) |
| **Web** | Portfolio visual y contacto → [`lanuzalorenzo.github.io`](https://lanuzalorenzo.github.io) |

---

## Contacto y licencia

**Autor:** Lorenzo Lanuza Arellano — *Software Engineer & Architect \| .NET, DevSecOps & Cloud Security*  
**LinkedIn:** [linkedin.com/in/lanuzalorenzo](https://www.linkedin.com/in/lanuzalorenzo) · **GitHub:** [github.com/lanuzalorenzo](https://github.com/lanuzalorenzo) · **Email:** [lanuzalorenzo@gmail.com](mailto:lanuzalorenzo@gmail.com)

Material técnico y formativo. No acredita configuraciones de producción ni certificaciones. Distribuido bajo licencia [MIT](LICENSE).
