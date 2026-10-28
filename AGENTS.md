# Guía del repositorio

Portfolio público de documentación y laboratorios de ciberseguridad cloud (Azure, Entra ID, Defender, DevSecOps). Describe trabajo documentado, no producción. La arquitectura del lab final, los runbooks y el índice de evidencias viven aquí; el código y la IaC, en [lab-api-local-azure](https://github.com/lanuzalorenzo/lab-api-local-azure).

Entrada pública: `docs/guia-de-lectura.md`. Este archivo es el contrato de trabajo y la referencia editorial de los repos públicos de la familia.

## Contrato editorial

- Español claro y directo, sin épica ni rótulos de registro («En fácil», «TL;DR», «En resumen»). Nombres oficiales de productos y controles.
- Estados: **Validado**, **Parcial**, **Runbook preparado**, **Diseño**, **Pendiente**. Un diseño o runbook sin ejecutar no es validación.
- Distingue ejecutado, observado, recomendado y planificado. No inventes evidencias; un hallazgo no es un PASS.
- Sin secretos, datos personales, IPs internas ni identificadores reales. Explica con una analogía antes del detalle técnico.

## Reglas de trabajo

- Comprueba el árbol y los documentos relacionados antes de crear o enlazar; el estado actual del repo es la referencia.
- Conserva la organización y sigue el patrón del módulo cercano. No crees carpetas vacías, documentos de relleno ni reestructuraciones por uniformidad.
- No abras módulos nuevos hasta consolidar los existentes.
- Mantén el estado coherente entre la puerta del módulo, la guía de lectura, el índice y la web/perfil.
- Definición de hecho: 0 enlaces rotos; estado coherente; sin duplicados página-informe; sin restos de plantilla.

## Estructura y formatos

- **Puerta del módulo** (`README.md`): 250–500 palabras; problema en prosa, piezas con estado, ejecutado frente a recomendado.
- **Práctica** (`practicas/<caso>/`): 240–310 palabras; problema, referencias (MCSB/CIS/NIST), tabla de hallazgos, 2–3 lecciones y enlaces. Sigue `plantillas/README-practica-template.md`.
- **Informe** (`informe.md`, junto a la práctica): solo catálogo, configuración, matriz o verificación; no repite la página.
- **Runbook** (`runbook.md` + `evidencias/`): solo prácticas reejecutables, con el contrato de abajo.
- **Bitácora** (`bitacora/`): solo hechos que no estén en página ni informe (decisión, fallo, fecha, limitación). Primera persona, fechas, paneles y mensajes de error tal cual. Puede no existir; si extraña, la puerta lo explica en una frase. Sin epígrafes vacíos ni índices de tareas.
- **Docs del módulo** (`docs/`): conceptos y arquitectura compartidos. **Lab** (`lab/`): artefactos locales. **Lab final** (`laboratorio-final/`): arquitectura, plan de ejecución e índice de evidencias. **Plantillas** (`plantillas/`): índice y plantillas.

## Cómo se trabaja un módulo

Lee y cuenta → cuéntalo antes de tocarlo → inventaría (único, repetido o vacío) → propón qué queda, se fusiona o se retira y a qué estado pasa, confirmando borrados y cambios → aplica → verifica y cierra.

## Runbooks y evidencias

Responsabilidades: `README.md` (por qué, alcance, estado y enlaces), `runbook.md` (cómo), `evidencias/` (salidas reales fechadas y redactadas) y `bitacora/` (qué ocurrió).

Contrato mínimo del runbook: prerrequisitos y permisos; variables y nombres; comandos copiables; resultado esperado; evidencia a capturar; prueba negativa o de control; limpieza y restauración; coste y tiempo; limitaciones y lo no ejecutado.

Reglas: un comando no ejecutado se marca como tal; cada evidencia lleva fecha, runbook, entorno, resultado y enlaces; sin secretos, IPs internas, IDs reales ni datos personales. Un despliegue de laboratorio requiere autorización, suscripción de lab, presupuesto, grupo de recursos temporal, datos sintéticos y plan de limpieza.

## Guía de lectura

`docs/guia-de-lectura.md` es la puerta pública: rutas, glosario, mapa de módulos y criterios de verificación. Mantenla alineada al cambiar estados, evidencias, orden o enlaces. No dupliques su contenido en la web ni en el perfil.

## Commits

Formato: `type(scope): imperative summary in English`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Scopes: código o módulo (`01-azure`, `02-identity`, …, `compliance`), `lab`, `repo`.
