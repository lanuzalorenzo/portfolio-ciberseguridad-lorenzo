# 02 | Revisión y Remediación de Recomendaciones de Seguridad

## Descripción del escenario y objetivo de seguridad

**Escenario:** Suscripción de laboratorio con planes de Defender for Cloud activos que genera un catálogo de recomendaciones de seguridad sin priorizar ni remediar, reduciendo la eficacia del CSPM.
**Objetivo de seguridad:** Analizar el panel de recomendaciones de Defender for Cloud, priorizar las de mayor impacto en el Secure Score y aplicar remediaciones directas, distinguiendo entre correcciones automáticas (*Quick Fix*) y procedimientos manuales.
**Alcance:** Suscripción de laboratorio en Azure; recomendaciones de los dominios de red, identidad y cifrado generadas por la iniciativa Microsoft Cloud Security Benchmark.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Azure utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Defender for Cloud — Recommendations** | Motor de evaluación continua de postura | Recomendaciones agrupadas por control de seguridad con puntuación de impacto. |
| **Secure Score** | Indicador numérico del estado de seguridad | Puntuación sobre 100 basada en controles del MCSB. |
| **Quick Fix** | Remediación automatizada directa desde el portal | Disponible en recomendaciones con impacto alto y remediación estandarizada. |
| **Azure Resource Graph** | Consulta de recursos afectados por recomendación | Permite inspeccionar y filtrar los recursos evaluados por Defender for Cloud. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| Priorización de recomendaciones por impacto | Ordenación por deducción de puntos sobre el Secure Score | Análisis en panel *Recommendations* | MCSB GS-1 |
| Remediación de puertos de administración expuestos | Habilitación de acceso Just-in-Time (JIT) en VMs | *Quick Fix* desde el panel de Defender for Cloud | MCSB NS-1 / CIS 6.2 |
| Actualización de versión mínima de TLS | Forzado de TLS 1.2 en Storage Accounts afectados | Remediación directa en propiedades del recurso | MCSB DP-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Aplicación de Quick Fix en recomendación crítica | Remediación en un clic desde el panel de Defender for Cloud | La recomendación pasa a estado *Healthy* en el siguiente ciclo de evaluación | PASS: Recurso marcado como conforme tras la remediación |
| Comprobación del incremento del Secure Score | Comparativa de puntuación antes/después de las remediaciones | Incremento proporcional al peso de los controles remediados | PASS: Mejora observada en la puntuación del control aplicado |
| Verificación de recomendaciones con remediación manual | Identificación de recomendaciones sin *Quick Fix* disponible | Acciones descritas y documentadas para remediación manual | No ejecutada — algunos controles requieren cambios de arquitectura fuera del alcance del laboratorio |

> [!WARNING]
> Las pruebas no ejecutadas se registran como pendientes. No se declaran como PASS.

## Lecciones aprendidas y buenas prácticas del Microsoft Cloud Security Benchmark

| Dominio o control MCSB aplicable | Aplicación en la práctica | Lección aprendida |
|---|---|---|
| **GS-2: Gestión de la postura de seguridad** | Revisión y remediación periódica del Secure Score | El Secure Score no es un fin en sí mismo; debe combinarse con análisis de riesgo para priorizar correctamente. |
| **NS-1: Seguridad de red perimetral** | Cierre de puertos de administración expuestos innecesariamente | Los puertos RDP (3389) y SSH (22) no deben estar accesibles desde Internet; el acceso JIT reduce la ventana de exposición a minutos bajo demanda. |

- Algunas recomendaciones de Defender for Cloud requieren cambios de arquitectura significativos (como migrar a Private Endpoints) que no son aplicables en laboratorios de coste cero; documentarlos como hallazgos pendientes es la práctica correcta.
