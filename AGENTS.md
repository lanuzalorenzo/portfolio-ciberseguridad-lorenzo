# Guía del repositorio

Este repositorio es un portfolio público de documentación y laboratorios de ciberseguridad cloud. El contenido abarca Azure, Microsoft Entra ID, Microsoft Defender y DevSecOps; describe trabajo documentado y no debe presentarse como despliegue de producción.

También aloja la arquitectura del laboratorio final, los runbooks y el índice de evidencias. El código y el IaC específicos del workload viven en `lab-api-local-azure`; no dupliques aquí esa infraestructura.

Al trabajar en el repositorio:

- Comprueba el árbol y los documentos relacionados antes de crear o enlazar contenido; el estado actual del repositorio es la referencia.
- Conserva la organización existente. Para contenido nuevo, sigue el patrón del módulo cercano: README de entrada, bitácora y prácticas cuando correspondan.
- No crees carpetas vacías ni reestructures contenido existente solo para uniformarlo.
- Distingue los planes de las pruebas ejecutadas y sus resultados observados; no inventes evidencias ni afirmaciones técnicas.
- Usa el estado explícito: **Validado**, **Parcial**, **Runbook preparado**, **Diseño** o **Pendiente**. Un diseño o un runbook sin ejecutar no son una validación.
- No crees módulos nuevos mientras los existentes no estén consolidados; prioriza profundizar y evidenciar sobre ampliar el catálogo.
- No añadas secretos, datos personales ni identificadores sensibles.
- Mantén la coherencia entre el README del módulo, la web, el perfil y la matriz de cumplimiento.
- Escribe la documentación en español claro y conserva los nombres oficiales de productos y controles cuando corresponda.

## Estructura recomendada para módulos, runbooks y bitácoras

Cada módulo debe mantener una estructura clara y legible, con un objetivo técnico definido y una narrativa de aprendizaje. La intención del portfolio es mostrar progresión real, no solo volumen de documentos.

### Patrones esperados

- README del módulo: presentación del alcance, objetivos y enlaces a prácticas.
- README de práctica: usa `plantillas/README-practica-template.md` para escenario, arquitectura, controles, validación y lecciones.
- bitácora/: registro del recorrido técnico del módulo.
- practicas/: contenido específico por caso de uso o escenario.
- docs/: artefactos técnicos, informes internos, plantillas y notas de laboratorio.
- lab/: artefactos locales de ejecución (compose, pipelines, scripts y datos sintéticos).
- docs/laboratorio-final/: arquitectura, plan de ejecución e índice de evidencias del laboratorio integrado.
- plantillas/: runbook y registro de evidencia reutilizables.

### Runbooks y evidencias

Una práctica ejecutable separa cuatro responsabilidades:

- `README.md`: por qué existe, alcance, estado y enlaces.
- `runbook.md`: cómo ejecutarla paso a paso.
- `evidencias/`: salidas reales, fechadas y redactadas.
- `bitacora/`: qué ocurrió, decisiones y aprendizaje.

Contrato mínimo de un runbook:

1. Prerrequisitos y permisos.
2. Variables y nombres de recursos.
3. Comandos copiables.
4. Resultado esperado.
5. Evidencia que se debe capturar.
6. Prueba negativa o de control.
7. Limpieza y restauración.
8. Coste y tiempo estimados.
9. Limitaciones y lo que no se ha ejecutado.

Reglas:

- Un comando no ejecutado se marca como **no ejecutado**; no se inventan salidas.
- Cada evidencia indica fecha, runbook, entorno, resultado y enlaces; elimina secretos, IPs internas, identificadores reales y datos personales.
- Un despliegue de laboratorio requiere autorización explícita, suscripción de laboratorio, presupuesto, resource group temporal, datos sintéticos y plan de limpieza. Nunca se ejecuta en producción.
- Los estados de módulos, web, perfil y matriz de cumplimiento deben coincidir.

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
- Cuando no haya validación real, debe indicarse explícitamente como pendiente, runbook preparado o trabajo de diseño.

## Convenciones de Commits

Todos los commits de este repositorio (realizados por el usuario o por asistentes de IA como GitHub Copilot, Google Antigravity, Claude, etc.) deben seguir estrictamente el estándar **Conventional Commits**:

- Formato: `type(scope): imperative summary in English`.
- **Ámbitos (`scope`) permitidos:**
  - Código o nombre del módulo: `01-azure`, `02-identity`, `03-audits`, `04-defender`, `05-defender-suite`, `06-identity-protection`, `07-devsecops`, `08-network`, `09-sentinel`, `10-elk`, `11-api-offensive`, `12-forensics`, `compliance`.
  - Laboratorio final, runbooks y plantillas: `lab`.
  - Ámbito general del repositorio: `repo`.
- **Tipos permitidos:** `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
- El asunto debe ser imperativo, conciso y redactado en inglés.
- Ejemplos:
  - `docs(07-devsecops): document branch protection and PR review rules`
  - `docs(01-azure): explain JWT validation and JWKS discovery`
  - `docs(repo): update architecture and defense in depth model`