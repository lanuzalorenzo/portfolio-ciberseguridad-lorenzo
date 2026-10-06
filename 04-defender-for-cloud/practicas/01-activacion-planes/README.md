# 01 | Activación de Planes de Microsoft Defender for Cloud

## Descripción del escenario y objetivo de seguridad

**Escenario:** Suscripción de laboratorio en Azure con únicamente el nivel gratuito (*Foundational CSPM*) habilitado, sin protección activa contra amenazas en workloads ni telemetría de seguridad en servicios PaaS.
**Objetivo de seguridad:** Evaluar el catálogo de planes de protección de Defender for Cloud y habilitar los pertinentes al entorno, entendiendo el impacto de cada plan en la postura de seguridad (CSPM) y en la protección de cargas de trabajo (CWPP).
**Alcance:** Suscripción de laboratorio en Azure. Evaluación de planes disponibles y validación de capacidades activadas desde el portal de Microsoft Defender for Cloud.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Defender for Cloud** | Plataforma unificada de CSPM y CWPP | Habilitado en la suscripción; evaluación desde *Environment settings*. |
| **Foundational CSPM (Gratuito)** | Inventario de recursos, Secure Score y recomendaciones básicas | Activo por defecto en todas las suscripciones. |
| **Defender CSPM (Plan de pago)** | CSPM avanzado: Attack Path Analysis, Cloud Security Explorer, gobernanza | Evaluado; no activado por restricciones de coste del laboratorio. |
| **Defender for Servers (Plan 1 / Plan 2)** | Protección de VMs con integración de Microsoft Defender for Endpoint y MDVM | Plan 1 activado para evaluación; Plan 2 evaluado a nivel de capacidades. |
| **Defender for Storage** | Detección de malware en blobs y accesos anómalos en Storage Accounts | Evaluado en el catálogo de planes. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Visibilidad de postura de seguridad (CSPM) | Foundational CSPM activo con Secure Score y recomendaciones | Sin coste adicional; habilitado por defecto | MCSB GS-1 |
| Protección de VMs contra amenazas (CWPP) | Defender for Servers Plan 1 habilitado | Aprovisionamiento automático del agente MMA/AMA | MCSB EP-1 / EP-2 |
| Detección de comportamientos anómalos | Alertas de seguridad generadas por los planes activos | Motor de detección de amenazas de Defender for Cloud | MCSB IR-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Verificación de estado de planes | Panel *Environment settings* → suscripción de laboratorio | Planes habilitados visibles con estado *On* | PASS: Foundational CSPM y Defender for Servers Plan 1 activos |
| Impacto en Secure Score tras activación | Comparativa de puntuación antes y después | Aparición de nuevas recomendaciones gestionadas por los planes | PASS: Nuevas recomendaciones de red y cifrado incorporadas al Secure Score |
| Aprovisionamiento automático del agente | Inspección de extensiones en VM de prueba | Presencia de la extensión MDE o Azure Monitor Agent | PASS: Extensión instalada automáticamente según política del plan |

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **GS-1: Alinear con estrategia de seguridad** | Selección deliberada de planes conforme al perfil de riesgo | Activar todos los planes sin análisis previo puede generar un coste desproporcionado al valor obtenido en laboratorios pequeños. |
| **EP-1: Protección de endpoints** | Defender for Servers como capa de EDR sobre VMs | La integración de Defender for Servers con Microsoft Defender for Endpoint es transparente y se activa sin necesidad de onboarding manual separado. |

- El nivel *Foundational CSPM* gratuito es suficiente para obtener visibilidad e identificar brechas; los planes de pago añaden capacidades de prevención activa (JIT, MDVM, Attack Path) que requieren justificación de negocio o alcance de laboratorio ampliado.
