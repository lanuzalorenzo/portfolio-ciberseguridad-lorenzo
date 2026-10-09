# Informe técnico — Detección con KQL y análisis de alertas

## Estado del documento

Diseño de laboratorio en curso. No se han ejecutado consultas ni validado alertas reales.

## Escenario y objetivo

Se plantea evaluar la capacidad de Sentinel para detectar patrones sospechosos a partir de eventos de acceso, identidad y recursos. El objetivo es comprobar cómo una consulta KQL puede identificar anomalías con contexto suficiente para investigación.

## Estructura propuesta de laboratorio

1. Definir la fuente de datos y el conector asociado: Entra ID, Azure, Defender o recursos del entorno.
2. Seleccionar un caso de uso concreto: acceso anómalo, privilegios excesivos, comportamiento fuera de horario o cambios de configuración sensibles.
3. Generar una consulta KQL con filtros, agregaciones y contexto de riesgo.
4. Validar el resultado con datos reales o simulados, documentando la evidencia y la salida.
5. Relacionar la detección con un incidente y decidir qué automatización o revisión manual es necesaria.

## Validación planificada

| Caso | Evidencia a recoger | Resultado esperado | Estado |
|---|---|---|---|
| Consulta de propiedad | Resultado de KQL con filtro y contexto | Datos útiles para análisis | Pendiente |
| Detección ad hoc | Registros sospechosos o anomalías | Señal compatible con la hipótesis | Pendiente |
| Correlación con incidentes | Vinculación con eventos asociados | Contexto suficiente para alertado | Pendiente |

## Límites y consideraciones

- KQL debe usarse con casos específicos; la detección genérica suele producir ruido.
- La validación real dependerá del conector y del tipo de datasource disponible.
- La elección de la hora, entidad y contexto es crítica para reducir falsos positivos.
