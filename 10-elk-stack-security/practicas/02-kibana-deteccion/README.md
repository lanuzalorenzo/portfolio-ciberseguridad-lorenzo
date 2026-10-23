# 02 | Visualización, detección y análisis con Kibana

> **Estado:** Validado en local. La vista de datos, las 6 consultas KQL y el dashboard se han ejecutado y verificado con los datos sintéticos.
>
> **Runbook:** [runbook.md](runbook.md).
>
> **Informe:** [informe.md](informe.md).
>
> **Evidencia:** [2026-10-19-10-elk-ingesta](../../../docs/laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/README.md).

## Contexto y alcance

**Escenario:** una vez centralizados los eventos en Elasticsearch, la práctica se centra en convertir esos datos en señales de seguridad útiles. La idea es convertir un conjunto de logs normalizados en una secuencia de indicadores para apoyar la investigación de actividad sospechosa.

**Objetivo de seguridad:** detectar patrones, validar hipótesis de seguridad y construir una vista operativa útil para investigación y respuesta.

> [!NOTE]
> La práctica se documenta como ejercicio técnico y no representa una implementación en producción.

## Caso de detección del laboratorio

Se va a trabajar con este patrón de eventos:

- varios intentos fallidos de autenticación desde la misma dirección IP;
- accesos a rutas no habituales en un servicio web;
- uso de comandos privilegiados o administración fuera del horario habitual;
- correlación de esos sucesos durante la misma ventana temporal.

Ese conjunto de eventos puede sugerir fuerza bruta, enumeración, uso indebido de credenciales o intento de escalada de privilegios.

## Arquitectura y componentes

| Componente | Función | Observación |
|---|---|---|
| Elasticsearch | Almacenamiento de eventos normalizados | Proporciona la capa de búsqueda y correlación. |
| Kibana | Visualización y análisis | Permite construir dashboards y consultar secuencias de eventos. |
| Logstash | Normalización de la fuente | Prepara la señal para ser útil en detección. |
| Índice de seguridad | Agrupación de eventos | Facilita comparaciones por usuario, servicio, IP o host. |

## Trabajo propuesto

- Crear un índice o vista útil para los eventos de seguridad normalizados.
- Diseñar un dashboard con series temporales, conteos por servicio y recuento de eventos por resultado.
- Definir consultas sobre comportamiento anómalo: accesos fallidos, picos de autenticación, actividad anómala por IP o uso de privilegios.
- Correlacionar señales para reconocer un patrón sospechoso con datos de contexto.
- Documentar qué se consideraría una alerta útil y qué debería revisarse de forma manual.

## Resultados esperados

- Visualización clara de eventos con contexto suficiente para análisis.
- Identificación de patrones de riesgo y anomalías.
- Base para dashboards y detección más avanzada en futuras iteraciones.

## Validación planificada

| Prueba | Método | Resultado esperado | Estado |
|---|---|---|---|
| Dashboard base | Visualización de eventos por tiempo y servicio | Evidencia clara y legible | Validado en local |
| Consulta por fallos y IP | Filtro de autenticación repetitiva | Señal visible y correlacionable | Validado en local |
| Consulta por actividad privilegiada | Búsqueda de comandos o acceso administrativo | Detección de patrón anómalo | Validado en local |
| Correlación | Comparación de eventos en ventana de tiempo | Hipótesis de seguridad sustentada | Validado en local |

## Aprendizaje clave

- Kibana convierte el dato bruto en contexto operativo y analítico.
- Una detección útil no se basa solo en alertas; requiere correlación y tiempo.
- La combinación de log normalizado + visualización permite construir hipótesis de seguridad con mucho más valor que la simple consulta aislada.
