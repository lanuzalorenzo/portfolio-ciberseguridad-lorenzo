# Guía del repositorio

Portfolio público de documentación y laboratorios de ciberseguridad cloud (Azure, Entra ID, Defender, DevSecOps). Describe trabajo documentado, no producción. La arquitectura del lab final, runbooks e índice de evidencias viven aquí; código e IaC del workload en `lab-api-local-azure`.

Si llegas nuevo: empieza por `docs/guia-de-lectura.md`. Este archivo es el contrato de trabajo.

## Reglas de trabajo

- Comprueba árbol y documentos relacionados antes de crear/enlazar; el estado actual del repo es la referencia.
- Conserva la organización existente; sigue el patrón del módulo cercano (README de entrada, bitácora, prácticas).
- No crees carpetas vacías ni reestructures por uniformidad.
- Distingue planes de pruebas ejecutadas y resultados observados; no inventes evidencias.
- Estados explícitos: **Validado**, **Parcial**, **Runbook preparado**, **Diseño**, **Pendiente**.
- No crees módulos nuevos hasta consolidar los existentes.
- No añadas secretos, datos personales ni identificadores sensibles.
- Mantén coherencia entre README del módulo, web y perfil.
- Documentación en español claro; nombres oficiales de productos/controles.
- Voz directa y cercana, sin épica; explica conceptos con analogía antes del detalle. Sin rótulos de registro.

## Estructura esperada

- `README.md` del módulo: puerta (qué es, piezas, estado).
- `README.md` de práctica: sigue `plantillas/README-practica-template.md`.
- `practicas/`: un caso por carpeta, con página e informe al lado si hace falta.
- `docs/` del módulo: explicación compartida (conceptos, arquitectura).
- `informe.md` en la práctica: detalle no sostenible en la página.
- `runbook.md` + `evidencias/`: solo prácticas reejecutables.
- `bitacora/`: solo hechos no presentes en otro sitio.
- `lab/`: artefactos locales (compose, pipelines, scripts, datos sintéticos).
- `laboratorio-final/`: arquitectura, plan de ejecución, índice de evidencias.
- `plantillas/`: índice y plantillas.

## Cómo se trabaja un módulo

Orden: 1) lee y cuenta; 2) cuéntalo antes de tocarlo; 3) inventaría (único/repetido/vacío); 4) propón (queda/fusiona/retira/estado) y confirma borrados/cambios de estado; 5) aplica; 6) verifica y cierra.

Formas:
- Puerta del módulo: 250–500 palabras; problema en prosa, estructura si aplica, piezas con estado, ejecutado vs recomendado.
- Página de práctica: 240–310 palabras; problema, referencias (MCSB/CIS/NIST), tabla de hallazgos, 2–3 lecciones, enlaces.
- Informe: solo catálogo/config/matriz/verificación; `informe.md` junto a la página.
- Runbook: solo prácticas reejecutables (contrato abajo).
- Bitácora: según criterio abajo.

Reglas: página no duplica informe; un hallazgo no es PASS; lo no ejecutado se escribe como tal; estado desglosado si madurez distinta; nada de documentos que aparentan.

Definición de hecho: 0 enlaces rotos; estado coherente en puerta/guía/índice/web; sin duplicados página-informe; sin restos de plantilla.

## Runbooks y evidencias

Responsabilidades: `README.md` (por qué/alcance/estado/enlaces), `runbook.md` (cómo), `evidencias/` (salidas reales fechadas redactadas), `bitacora/` (qué ocurrió).

Contrato mínimo del runbook: prerrequisitos/permisos; variables/nombres; comandos copiables; resultado esperado; evidencia a capturar; prueba negativa/control; limpieza/restauración; coste/tiempo; limitaciones/no ejecutado.

Reglas: comando no ejecutado marcado como no ejecutado; cada evidencia con fecha, runbook, entorno, resultado, enlaces; sin secretos/IPs internas/IDs reales/datos personales; despliegue de lab requiere autorización, suscripción de lab, presupuesto, RG temporal, datos sintéticos y plan de limpieza.

## Bitácoras

Solo si guarda un hecho no presente en informe/página (decisión, fallo, fecha, limitación). Primera persona, fechas, nombres de paneles, mensajes de error tal cual. Un módulo puede no tener bitácora; si extraña, la puerta lo explica en una frase. No rellenar epígrafes vacíos ni copiar índice de tareas.

## Guía de lectura

`docs/guia-de-lectura.md` es la puerta pública: rutas, glosario, mapa de módulos, criterios de verificación. Mantenerla alineada al cambiar estado/evidencias/orden/enlaces. No duplicar en web/perfil.

## Reglas de calidad

Bitácoras útiles para lector técnico; sin secretos/IDs reales/datos sensibles/evidencia inventada; distinguir ejecutado vs planificado; mostrar criterio técnico; indicar pendiente/runbook/diseño cuando no haya validación real.

## Convenciones de commits

Formato: `type(scope): imperative summary in English`. Tipos: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`. Scopes: código/módulo (`01-azure`, `02-identity`, …, `compliance`), `lab`, `repo`. Asunto imperativo, conciso, en inglés. Commit/push requieren autorización explícita por lote.