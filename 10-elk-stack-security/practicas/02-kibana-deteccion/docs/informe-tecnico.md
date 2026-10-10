# Informe técnico — Visualización, detección y análisis con Kibana

## Estado del documento

Diseño del laboratorio en curso. No se ha ejecutado una validación real en entorno operativo.

## Escenario

Se propone un caso de detección basado en un patrón de anomalías distribuidas en tiempo y contexto:

- fallos de autenticación repetidos desde una IP específica;
- uso de rutas o endpoints no habituales;
- comandos de privilegios en una ventana temporal inusual;
- combinación de esos eventos para construir una hipótesis de abuso o intento de acceso anómalo.

La idea es comprobar cómo Kibana ayuda a convertir la ingesta de Logstash en un conjunto de señales útiles para análisis y toma de decisiones.

## Diseño propuesto

1. Revisar el índice o vista generada por Logstash.
2. Crear visualizaciones por tiempo, usuario, IP y servicio.
3. Definir una o varias consultas enfocadas a anomalías repetidas.
4. Correlacionar la actividad por ventana temporal para diferenciar ruido de sospecha.
5. Determinar qué patrón sería lo suficientemente sólido para considerarlo una alerta preliminar.

## Elementos a revisar en Kibana

| Elemento | Objetivo |
|---|---|
| Series temporales | Ver el comportamiento a lo largo del tiempo. |
| Conteos por usuario y servicio | Detectar actividad anómala por origen. |
| Filtros por IP | Identificar actores repetidos o no habituales. |
| Dashboard de contexto | Combinar evento, servicio y resultado para analizar riesgo. |

## Consideraciones técnicas

- El valor de la detección depende más del contexto que del número de logs.
- La correlación por tiempo y origen es clave para distinguir ruido de actividad sospechosa.
- La facilidad de análisis se incrementa si cada evento ya lleva un formato normalizado y consistente.

## Siguientes pasos

- Ejecutar la práctica con un conjunto mínimo de logs y verificar la corrección del índice.
- Revisar los paneles generados y ajustar filtros.
- Identificar qué patrones son útiles para alertado y qué requieren validación humana.
- Preparar la siguiente fase del módulo con una detección más avanzada y casos comparables a una operación real de SOC o ELK.
