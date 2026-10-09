# Guía del repositorio

Este repositorio es un portfolio público de documentación y laboratorios de ciberseguridad cloud. El contenido abarca Azure, Microsoft Entra ID, Microsoft Defender y DevSecOps; describe trabajo documentado y no debe presentarse como despliegue de producción.

Al trabajar en el repositorio:

- Comprueba el árbol y los documentos relacionados antes de crear o enlazar contenido; el estado actual del repositorio es la referencia.
- Conserva la organización existente. Para contenido nuevo, sigue el patrón del módulo cercano: README de entrada, bitácora y prácticas cuando correspondan.
- No crees carpetas vacías ni reestructures contenido existente solo para uniformarlo.
- Distingue los planes de las pruebas ejecutadas y sus resultados observados; no inventes evidencias ni afirmaciones técnicas.
- No añadas secretos, datos personales ni identificadores sensibles.
- Escribe la documentación en español claro y conserva los nombres oficiales de productos y controles cuando corresponda.

## Estructura recomendada para módulos y bitácoras

Cada módulo debe mantener una estructura clara y legible, con un objetivo técnico definido y una narrativa de aprendizaje. La intención del portfolio es mostrar progresión real, no solo volumen de documentos.

### Patrones esperados

- README del módulo: presentación del alcance, objetivos y enlaces a prácticas.
- bitácora/: registro del recorrido técnico del módulo.
- practicas/: contenido específico por caso de uso o escenario.
- docs/: artefactos técnicos, informes internos, plantillas y notas de laboratorio.

### Plantilla recomendada para bitácoras

Cada entrada de bitácora debe responder a estas preguntas:

- ¿Cuál es el objetivo del módulo o sesión?
- ¿Qué escenario o caso de uso se está analizando?
- ¿Qué tecnologías o servicios se están revisando?
- ¿Qué se hizo, qué se revisó o qué se probó?
- ¿Qué fue útil, qué falló o qué quedó pendiente?
- ¿Qué aprendizaje técnico aporta?
- ¿Cuál es el siguiente paso?

Formato recomendado para cada entrada:

```md
# Bitácora — [Nombre del módulo o sesión]

## Objetivo

Describir el propósito del trabajo y el problema de seguridad que se está abordando.

## Contexto y alcance

Explicar el escenario, la infraestructura o los servicios implicados y la delimitación del caso de uso.

## Trabajo realizado

- Revisión de arquitectura.
- Evaluación de control, servicio o flujo.
- Diagnóstico o diseño propuesto.
- Validación ejecutada o planificada.

## Resultados

Documentar lo observado, los hallazgos, las decisiones o los puntos de mejora.

## Pendientes o riesgos

Indicar qué queda por validar, qué no se ejecutó o qué requiere un entorno real.

## Aprendizaje

Resumen técnico del valor del ejercicio y de la toma de decisiones.

## Siguiente paso

Qué se hará a continuación para completar o profundizar el módulo.
```

### Reglas de calidad

- Las bitácoras deben ser útiles para un lector técnico, no solo genéricas.
- No deben incluir secretos, identificadores reales, datos sensibles o evidencia inventada.
- Deben distinguir claramente entre trabajo ejecutado y trabajo planificado.
- Deben mostrar criterio técnico, no meras anotaciones administrativas.
- Cuando no haya validación real, debe indicarse explícitamente como pendiente o trabajo de diseño.