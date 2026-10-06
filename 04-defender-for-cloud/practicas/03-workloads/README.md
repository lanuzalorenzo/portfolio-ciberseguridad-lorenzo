# 03 | Protección de Workloads con Defender for Cloud (CWPP)

## Descripción del escenario y objetivo de seguridad

**Escenario:** Máquinas virtuales y servicios PaaS de la suscripción de laboratorio sin cobertura activa de detección y respuesta ante amenazas (Endpoint Detection and Response), expuestos a ataques de ejecución de código, movimiento lateral y exfiltración.
**Objetivo de seguridad:** Habilitar las capacidades de Cloud Workload Protection (CWPP) de Defender for Cloud sobre las cargas de trabajo del laboratorio, verificando la integración de Defender for Endpoint (MDE), el escaneo de vulnerabilidades y la generación de alertas de seguridad.
**Alcance:** Máquinas virtuales (Windows/Linux) en la suscripción de laboratorio y cuentas de almacenamiento evaluadas por Defender for Storage.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for Servers Plan 1** | EDR para VMs mediante integración con Microsoft Defender for Endpoint | Aprovisionamiento automático del sensor MDE activado en la directiva del plan. |
| **Extensión MDE (Azure Connected Machine / MMA)** | Agente instalado en VM para telemetría de seguridad | Instalado automáticamente por el aprovisionamiento del plan; comprobado en extensiones de la VM. |
| **Microsoft Defender Vulnerability Management (MDVM)** | Escaneo de vulnerabilidades nativo en VMs | Disponible en Plan 2; evaluado como capacidad adicional. |
| **Defender for Storage** | Detección de anomalías y malware en blobs | Análisis de actividad anómala en cuentas de almacenamiento; evaluado en el catálogo del plan. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Detección y respuesta en endpoints (EDR) | Integración de Defender for Servers con Microsoft Defender for Endpoint | Activación del plan y aprovisionamiento automático | MCSB EP-1 / EP-2 |
| Escaneo continuo de vulnerabilidades | MDVM integrado en Defender for Servers Plan 2 | Detección y puntuación de CVEs en runtime | MCSB PV-1 / PV-5 |
| Detección de anomalías en almacenamiento | Defender for Storage con alertas sobre operaciones inusuales | Motor de Machine Learning de Defender for Cloud | MCSB LT-2 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Verificación de instalación del sensor MDE | Inspección de extensiones en VM de prueba en el portal de Azure | Extensión `MDE.Windows` o `MDE.Linux` presente y aprovisionada | PASS: Extensión instalada automáticamente conforme al plan activado |
| Comprobación de cobertura CWPP en el panel | Revisión de *Workload protections* en Defender for Cloud | VMs de la suscripción listadas con estado de cobertura | PASS: VMs visibles con estado de protección registrado |
| Generación de alerta de prueba | Verificación de actividad detectable (herramienta de prueba de seguridad en entorno aislado) | Alerta generada y visible en el panel de *Security alerts* | No ejecutada — pruebas de simulación de amenazas fuera del alcance de este laboratorio |

> [!WARNING]
> La generación de alertas reales requiere un entorno controlado y aislado. No se ejecutaron pruebas de simulación de malware.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **EP-1: Protección de endpoints** | Defender for Servers con EDR integrado | La integración nativa entre Defender for Cloud y Microsoft Defender for Endpoint elimina el proceso manual de onboarding de máquinas al servicio EDR. |
| **PV-5: Gestión de vulnerabilidades** | MDVM para priorización de CVEs en runtime | La gestión de vulnerabilidades basada en contexto de exposición real es más eficaz que los escaneos periódicos sin priorización. |

- Las extensiones instaladas automáticamente por el aprovisionamiento del plan pueden generar costes adicionales en las máquinas; revisar la política de aprovisionamiento y excluir máquinas de desarrollo no críticas cuando proceda.
