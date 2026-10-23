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
- Mantén la coherencia entre el README del módulo, la web y el perfil.
- Escribe la documentación en español claro y conserva los nombres oficiales de productos y controles cuando corresponda.

## Estructura recomendada para módulos, runbooks y bitácoras

Cada módulo debe mantener una estructura clara y legible, con un objetivo técnico definido y una narrativa de aprendizaje. La intención del portfolio es mostrar progresión real, no solo volumen de documentos.

### Patrones esperados

- `README.md` del módulo: la puerta. Qué es el módulo, qué piezas lo forman y en qué estado está cada una.
- `README.md` de práctica: sigue `plantillas/README-practica-template.md`.
- `practicas/`: un caso por carpeta, con su página y, si lo necesita, su informe al lado.
- `docs/` del módulo: explicación que sirve a varias prácticas a la vez (conceptos, arquitectura del módulo).
- `informe.md` dentro de la práctica: el detalle que la página no puede sostener. Sin subcarpetas para un solo fichero.
- `runbook.md` y `evidencias/`: solo si la práctica se puede volver a ejecutar paso a paso.
- `bitacora/`: solo si guarda un hecho que no está en ningún otro sitio.
- `lab/`: artefactos locales de ejecución (compose, pipelines, scripts y datos sintéticos).
- `docs/laboratorio-final/`: arquitectura, plan de ejecución e índice de evidencias del laboratorio integrado.
- `plantillas/`: runbook y registro de evidencia reutilizables.

### Cómo se trabaja un módulo

Un módulo se recorre siempre en el mismo orden, porque el orden evita reescribir dos veces:

1. **Lee y cuenta.** El módulo completo, su fila en `docs/guia-de-lectura.md` y el estado de Git. Anota ficheros y palabras por documento: el volumen enseña dónde está el peso.
2. **Cuéntalo antes de tocarlo.** Qué problema resuelve el módulo, qué piezas lo forman y qué está ejecutado frente a lo que solo está diseñado. Si no se puede explicar así, todavía no se ha entendido.
3. **Inventaría.** Para cada fichero: qué información única tiene, qué repite y qué no dice nada. Un documento que no aporta ningún hecho se retira, y antes se comprueba quién lo enlaza.
4. **Propón.** Qué se queda, qué se fusiona, qué se retira y qué estado le corresponde a cada pieza. Los borrados y los cambios de estado se confirman antes de aplicarlos.
5. **Aplica** la forma de abajo, sin reestructurar por uniformidad lo que ya funciona.
6. **Verifica y cierra** con la definición de hecho.

Formas de cada pieza:

- **Puerta del módulo:** entre 250 y 500 palabras. Abre con el problema en prosa, muestra la estructura si la hay (un diagrama Mermaid basta), lista las piezas con su estado y separa lo ejecutado de lo recomendado. No repite lo que ya está en la guía de lectura ni en las prácticas.
- **Página de práctica:** entre 240 y 310 palabras. El problema en prosa, una línea de referencias (MCSB, CIS, NIST), una tabla con lo que se hizo o se encontró, dos o tres lecciones y los enlaces que hagan falta: el informe si existe y la bitácora si la hay.
- **Informe:** solo cuando guarda algo que la página no puede sostener: catálogo, configuración con valores, matriz de hallazgos o verificación. Vive en `informe.md`, junto a la página.
- **Runbook:** solo para prácticas reejecutables, con el contrato de la sección siguiente.
- **Bitácora:** según el criterio de más abajo.

Reglas:

- **La página no duplica el informe, y el informe no repite la página.** Si el informe solo cuenta lo mismo con más palabras, no existe: lo que aporte se funde en la página y se retira.
- **Un hallazgo no es un PASS.** Una auditoría que encuentra el problema ha funcionado, pero el control no está aprobado. La tabla lleva el resultado observado y la gravedad, y una frase aparte dice qué se corrigió y qué solo se recomendó.
- **Lo no ejecutado se escribe como no ejecutado**, con la razón. No se omite ni se marca como aprobado.
- **El estado se desglosa** cuando el rótulo del módulo cubre piezas con madurez distinta.
- **Nada de documentos que aparentan.** Un guion sin comandos, resultado esperado y evidencia no es un runbook: o se convierte en uno, o se retira.

Definición de hecho de un módulo:

1. Cero enlaces rotos en el repositorio.
2. El estado coincide en la puerta, la guía de lectura, el índice del repositorio y la web.
3. No hay tablas ni párrafos duplicados entre la página y el informe, ni informes que solo repitan la página.
4. No quedan restos de plantilla: etiquetas de registro, emojis ni frases sin resolver.

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
- Los estados de módulos, web y perfil deben coincidir.

### Bitácoras

Una bitácora registra una sesión de trabajo, no un formulario. Se escribe el día que pasa, porque lo que no se anota entonces no se reconstruye después: la decisión tomada, el error que bloqueó media tarde, la comprobación que el entorno no permitía hacer.

Reglas:

- Solo existe si guarda al menos un hecho que no está en el informe ni en la página de la práctica: una decisión, un fallo, una fecha o una limitación del entorno.
- Si al eliminar la entrada no se pierde ningún hecho, no era una bitácora: no se escribe.
- Se escribe en primera persona, con fechas, nombres de paneles y mensajes de error tal como aparecieron.
- Un módulo puede no tener bitácora. Si su ausencia extraña, la puerta lo explica en una frase.
- No se rellenan epígrafes vacíos ni se copia el índice de tareas del día: eso no es un registro, es una plantilla.

### Guía de lectura

- `docs/guia-de-lectura.md` es la puerta de entrada pública al portfolio: rutas, glosario, mapa de módulos y criterios de verificación.
- Mantenerla alineada cuando cambie el estado de un módulo, se añada o retire una evidencia, cambie el orden recomendado o se renombren enlaces de entrada.
- No duplicar la guía en la web ni en el perfil: esos repos solo enlazan a esta fuente única.
- Al cerrar un cambio que afecte al lector, revisar la sección «Mantenimiento» de la guía y actualizar la fecha de revisión.

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