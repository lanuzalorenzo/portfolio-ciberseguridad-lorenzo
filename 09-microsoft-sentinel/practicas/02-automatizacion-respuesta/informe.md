# Informe técnico — Automatización de respuesta y contención

## Estado del documento

Diseño de laboratorio en curso. No se ha ejecutado una automatización real ni validado un playbook en producción o laboratorio operativo.

## Escenario y objetivo

Se propone diseñar una automatización mínima que reaccione a una alerta sospechosa y lance una acción controlada: revisión, aislamiento o bloqueo de un recurso según el caso de uso. La idea es documentar la lógica de respuesta antes de desplegarla.

## Diseño propuesto

1. Elegir una alerta concreta con impacto limitado y condiciones bien definidas.
2. Documentar las variables de entrada: tipo de alerta, entorno, entidad o recurso afectado, nivel de riesgo y acción recomendada.
3. Crear un playbook con pasos simples y autorizados: revisión con el equipo, eliminación temporal del acceso o aislamiento de una entidad.
4. Verificar que el playbook tiene permisos mínimos y que la acción es reversible o fácilmente evaluable.
5. Registrar qué se comprueba en el entorno y qué acciones no se ejecutarán por prudencia.

## Validación planificada

| Caso | Evidencia a recoger | Resultado esperado | Estado |
|---|---|---|---|
| Disparo del playbook | Registro del evento y acción iniciada | Automación activa y documentada | Pendiente |
| Respuesta mínima | Verificación de que se evitó impacto innecesario | Acción adecuada al riesgo | Pendiente |
| Reversibilidad | Documentación del procedimiento de limpieza | Trabajo reversible y trazable | Pendiente |

## Límites y consideraciones

- La automatización debe estar acompañada de un proceso de validación humana para evitar errores graves.
- El tipo de contención dependerá del servicio afectado; no debe asumirse una acción universal.
- La documentación final debe describir el flujo completo y cómo se interpreta la alerta en el contexto del entorno.
