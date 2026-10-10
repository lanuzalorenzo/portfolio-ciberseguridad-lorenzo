# 01 | Ingestión y normalización con Logstash

## Contexto y alcance

**Escenario:** un entorno de laboratorio con logs de autenticación, acceso a servicios y actividad del sistema. Se recoge un caso realista de detección basado en fallos de autenticación, intentos repetidos y cambios sospechosos en la actividad de un host. La práctica se centra en convertir esos eventos en señales útiles para análisis y detección.

**Objetivo de seguridad:** consolidar logs procedentes de diferentes fuentes para detectar anomalías, correlacionar eventos y preparar la señal para análisis posterior en Kibana.

> [!NOTE]
> La práctica se documenta como ejercicio técnico y no representa una implementación en producción.

## Caso real de logs utilizado

| Fuente | Ejemplo de evento | Valor para detección |
|---|---|---|
| Auth log | `Failed password` repetidos | Identifica fuerza bruta o abuso de credenciales. |
| Sistema operativo | `sudo` o comandos privilegiados | Detecta uso anómalo de permisos. |
| Servicio web | Acceso a rutas inesperadas | Señala exploración o explotación. |
| SSH / accesos | Logins desde IPs no habituales | Ayuda a detectar pivote o accesos externos. |

Se utilizará una composición de logs de sistema y servicios para simular un escenario de seguridad operativa con patrones típicos de análisis.

## Arquitectura y componentes

| Componente | Función | Observación |
|---|---|---|
| Elasticsearch | Almacenamiento y búsqueda | Motor principal para índices y consultas. |
| Logstash | Ingesta, transforma y enruta eventos | Se usa para normalizar y filtrar logs. |
| Kibana | Visualización y análisis | Permite explorar datos y construir dashboards. |
| Fuente de logs | Aplicaciones, servicios o eventos de seguridad | Pueden venir de Linux, servicios web o actividad de red. |

## Trabajo propuesto

- Definir un caso de seguridad concreto: accesos fallidos, anomalías por IP, uso de sudo, rutas sospechosas o cambios de servicio.
- Configurar una pipeline de Logstash para leer el log y normalizar sus campos.
- Extraer y estructurar campos clave: timestamp, host, servicio, usuario, ip_origen, evento, nivel, resultado y detalle.
- Enviar la salida a un índice de Elasticsearch con un esquema claro para su análisis.
- Validar la ingesta y confirmar que los eventos quedan preparadas para detección en Kibana.

## Resultados esperados

- Logs capturados y transformados de forma consistente.
- Campos normalizados para consultas de detección y paneles.
- Base útil para identificar patrones anómalos con contexto.

## Validación planificada

| Prueba | Método | Resultado esperado | Estado |
|---|---|---|---|
| Ingesta de eventos | Carga de logs con fallos de autenticación y accesos sospechosos | Flujo correcto y sin pérdida | Pendiente |
| Normalización | Validación de campos clave para investigación | Esquema consistente y trazable | Pendiente |
| Exploración en Elasticsearch | Consulta por usuario, IP y servicio | Datos visibles y recuperables para análisis | Pendiente |
| Detección básica | Identificación de patrones repetidos | Evidencia útil para Kibana y alertado | Pendiente |

## Aprendizaje clave

- La calidad de los datos es más importante que el volumen y clave para la detección.
- La normalización no solo ordena el log, también permite correlacionar señales con contexto.
- ELK es especialmente útil cuando se quiere combinar eventos de autenticación, acceso y sistema para construir alertas y análisis de riesgo.
