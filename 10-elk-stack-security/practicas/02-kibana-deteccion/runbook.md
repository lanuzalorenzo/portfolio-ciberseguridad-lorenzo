# Runbook — Visualización, detección y análisis con Kibana

> **Estado:** Validado en local. Ejecutado el 2026-10-19 con la vista de datos, 6 consultas KQL y dashboard exportado.
>
> **Última revisión:** 2026-10-19.
>
> **Objetivo:** crear una vista de datos, validar consultas de detección y construir un dashboard con los eventos normalizados del runbook 01.
>
> **Ruta manual:** este runbook está pensado para seguirlo sin asistente. Cada paso indica qué abrir, qué escribir y qué debe aparecer. Si algo no coincide, no continúes: revisa el punto de control.

> Con los registros ya cargados, este documento enseña a mirarlos, hacer seis preguntas y guardar las respuestas en un panel. Es la parte de mirar, no la de recoger.

## 1. Prerrequisitos

- Pila ELK levantada con el runbook 01.
- `./scripts/verify.sh` con 15 eventos y verificación correcta.
- Kibana accesible en <http://localhost:5601>.

Comprobación rápida:

```bash
cd 10-elk-stack-security/lab
curl -fsS 'http://localhost:9200/_cat/indices/lab-security-*?v&h=index,docs.count'
```

**Debe aparecer** un índice `lab-security-2026.10.20` con `15` documentos.

## 2. Cómo usar este runbook

1. Lee el punto completo antes de ejecutarlo.
2. Haz cada paso en orden.
3. Comprueba el resultado esperado antes de pasar al siguiente.
4. Guarda cada visualización con el nombre indicado; así el dashboard y la exportación coinciden.
5. Al final, captura las pantallas y la exportación NDJSON.

### Convenciones

- **Menú:** ruta de clics en Kibana.
- **Campo:** nombre exacto que hay que escribir.
- **Debe aparecer:** resultado que confirma que el paso ha ido bien.
- `Ctrl/Cmd + F` no funciona dentro de Kibana; usa el buscador de campos.

### Atajos directos

| Pantalla | URL local |
|---|---|
| Data Views | <http://localhost:5601/app/management/kibana/dataViews> |
| Discover | <http://localhost:5601/app/discover> |
| Visualize | <http://localhost:5601/app/visualize> |
| Dashboards | <http://localhost:5601/app/dashboards> |
| Saved Objects | <http://localhost:5601/app/management/kibana/objects> |

## 3. Crear la vista de datos

1. Abre el navegador en <http://localhost:5601>.
2. Espera a que Kibana cargue. Si aparece una pantalla de bienvenida, pulsa **Explore on my own**.
3. **Menú:** abre el menú lateral (icono de hamburguesa) → **Stack Management**.
4. **Menú:** dentro de Stack Management, en la sección **Kibana**, pulsa **Data Views**.
5. Pulsa **Create data view**.
6. Rellena:
   - **Name:** `Lab Security`
   - **Index pattern:** `lab-security-*`
   - **Time field:** `@timestamp`
7. Pulsa **Save data view to Kibana**.

**Debe aparecer:** la vista `Lab Security` en la lista, con el patrón `lab-security-*`. En **Discover**, al seleccionarla y ajustar el rango temporal, el contador mostrará `15 hits`.

> Si la versión de Kibana muestra **Index Patterns** en vez de **Data Views**, es la misma función.

## 4. Ajustar el rango temporal

Los eventos son de `2026-10-20` entre `09:00:00Z` y `09:06:00Z`. Kibana los muestra en la zona horaria del navegador.

1. **Menú:** abre **Discover** (icono de brújula o lupa en el menú lateral).
2. Arriba a la izquierda, selecciona la vista **Lab Security** si no está ya seleccionada.
3. Arriba a la derecha, pulsa el selector de tiempo (icono de reloj).
4. Elige **Absolute**.
5. Escribe:
   - **From:** `2026-10-19 00:00:00.000`
   - **To:** `2026-10-22 00:00:00.000`
6. Pulsa **Apply**.

**Debe aparecer:** en la parte superior de Discover, un contador con `15 hits`.

> Si tu navegador está en UTC+2, los eventos de las 09:00Z se verán a las 11:00 locales; el rango amplio los cubre igual.

## 5. Consultas de detección en Discover

En **Discover**, con la vista `Lab Security` y el rango temporal aplicado, escribe cada consulta en la barra de búsqueda (KQL) y pulsa **Refresh** o `Enter`.

| Consulta KQL | Hits esperados | Qué demuestra |
|---|---|---|
| `event.outcome.keyword: "failure"` | 10 | Fallos totales |
| `service.name.keyword: "ssh" and event.outcome.keyword: "failure"` | 6 | Fuerza bruta SSH |
| `source.ip.keyword: "203.0.113.45" and event.outcome.keyword: "failure"` | 10 | Correlación por IP |
| `http.response.status_code >= 400` | 4 | Errores web |
| `event.action.keyword: "sudo"` | 1 | Actividad privilegiada |
| `url.path.keyword: "/admin"` | 1 | Acceso a ruta protegida |

**Debe aparecer:** el contador de hits de la tabla anterior para cada consulta.

> Los campos de texto se indexan con un subcampo `.keyword`. Usa `.keyword` para coincidencias exactas y agregaciones. `http.response.status_code` es numérico y no necesita subcampo.

### Comprobación opcional por API

Si quieres guardar la salida en la evidencia, valida las mismas consultas por API:

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_count' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}}}'
```

**Debe aparecer:** `{"count":10,...}`.

```bash
curl -fsS -H 'Content-Type: application/json' \
  'http://localhost:9200/lab-security-*/_search?pretty&size=0' \
  -d '{"query":{"term":{"event.outcome.keyword":"failure"}},"aggs":{"por_ip":{"terms":{"field":"source.ip.keyword","size":5}},"por_servicio":{"terms":{"field":"service.name.keyword","size":5}}}}'
```

**Debe aparecer:** `203.0.113.45` con `10` y los servicios `ssh` con `6` y `web` con `4`.

## 6. Construir el dashboard

El dashboard se construye con cinco visualizaciones. Para cada una:

1. **Menú:** **Visualize Library** (o **Visualize**) → **Create visualization**.
2. Elige **Lens** si Kibana pregunta por el tipo.
3. Configura los campos según la tabla.
4. Pulsa **Save**.
5. **Title:** el nombre indicado.
6. **Add to dashboard:** déjalo marcado si vas a montar el dashboard al final; si no, selecciona el dashboard `Lab Security — ELK`.

### Visualización 1 — Eventos por servicio

- **Tipo:** Bar vertical.
- **X-axis:** `service.name.keyword`.
- **Y-axis:** `Records`.
- **Filtro:** ninguno.
- **Nombre:** `Lab 01 - Eventos por servicio`.

**Debe aparecer:** `ssh` con 7, `web` con 6 y `system` con 2.

### Visualización 2 — Fallos por IP

- **Tipo:** Table.
- **Filtro:** `event.outcome.keyword: "failure"`.
- **Rows:** `source.ip.keyword`.
- **Metrics:** `Records`.
- **Orden:** descendente por `Records`.
- **Nombre:** `Lab 02 - Fallos por IP`.

**Debe aparecer:** `203.0.113.45` con 10.

### Visualización 3 — Fallos en el tiempo

1. **Visualize Library** → **Create visualization** → **Lens**.
2. Vista de datos: **Lab Security**.
3. Tipo de gráfico: **Line**.
4. En la barra KQL, escribe:
   ```text
   event.outcome.keyword: "failure"
   ```
   Pulsa `Enter` o **Refresh**.
5. Arrastra `@timestamp` al eje **Horizontal axis**.
6. Arrastra `Records` al eje **Vertical axis**.
7. En el panel derecho, dentro de **Horizontal axis**, cambia el intervalo de **Auto** a **1 minute**. Es importante fijarlo: con `Auto`, el intervalo cambia según el ancho del panel y los conteos pueden no coincidir.
8. **Debe aparecer:** 6 fallos a las 11:00 (UTC+2), 2 a las 11:03 y 2 a las 11:04. En UTC serían las 09:00, 09:03 y 09:04.
9. **Save**:
   - **Title:** `Lab 03 - Fallos en el tiempo`
   - **Add to dashboard:** `None`
   - **Add to library:** marcado
   - **Save**

### Visualización 4 — Errores web (búsqueda guardada)

Para esta visualización es más claro usar una **búsqueda guardada en Discover**: muestra los eventos individuales y evita el cruce de dimensiones de una tabla de Lens.

1. **Menú:** abre **Discover**.
2. Selecciona la vista **Lab Security**.
3. Aplica el rango temporal absoluto `2026-10-19 00:00:00.000` → `2026-10-22 00:00:00.000`.
4. En la barra KQL, escribe:
   ```text
   http.response.status_code >= 400
   ```
5. Pulsa `Enter` o **Refresh**.
6. En la lista de campos, añade como columnas:
   - `url.path.keyword`
   - `source.ip.keyword`
   - `http.response.status_code`
7. **Debe aparecer:** 4 eventos:
   - dos `POST /api/login` con `401`
   - un `GET /admin` con `403`
   - un `GET /../../etc/passwd` con `400`
8. Pulsa **Save**.
9. **Title:** `Lab 04 - Errores web`.
10. Guarda la búsqueda.

> Alternativa con Lens: usa una tabla con un solo campo en **Rows** (`url.path.keyword`) y añade `source.ip.keyword` y `http.response.status_code` como **Metrics** (`Top values` o `Last value`). Si añades los tres campos a **Rows**, Lens cruza los valores y muestra filas vacías.

### Visualización 5 — Total de fallos

- **Tipo:** Metric.
- **Filtro:** `event.outcome.keyword: "failure"`.
- **Metric:** `Records`.
- **Nombre:** `Lab 05 - Total de fallos`.

**Debe aparecer:** `10`.

### Montar el dashboard

1. **Menú:** **Dashboard** → **Create dashboard**.
2. Configura el rango temporal del dashboard en un intervalo que incluya los eventos. Si tu navegador está en **UTC+2**:
   - **From:** `2026-10-20 10:30:00.000`
   - **To:** `2026-10-20 11:30:00.000`
   - **Apply**
   Si estás en **UTC**, usa `2026-10-20 08:30:00.000` → `2026-10-20 09:30:00.000`. El objetivo es que la línea temporal muestre los eventos con detalle, no un rango de varios días.
3. Pulsa **Add panel** → **Add from library**.
4. Añade las cuatro visualizaciones:
   - `Lab 01 - Eventos por servicio`
   - `Lab 02 - Fallos por IP`
   - `Lab 03 - Fallos en el tiempo`
   - `Lab 05 - Total de fallos`
5. Para la búsqueda guardada, pulsa **Add panel** → **Saved search** (o cambia a la pestaña **Saved searches** dentro de la librería) y elige:
   - `Lab 04 - Errores web`
6. Organízalas y redimensiona si quieres. Una distribución útil:
   - Arriba: `Lab 05` (métrica) y `Lab 01` (barras).
   - En medio: `Lab 03` (línea temporal) a ancho completo.
   - Abajo: `Lab 02` (tabla de IPs) y `Lab 04` (búsqueda de errores web).
7. Pulsa **Save**.
8. **Title:** `Lab Security — ELK`.
9. Marca **Store time range** o **Save current time range** si aparece. Así el dashboard abrirá siempre con el rango correcto y no con «Last 15 minutes».
10. Pulsa **Save**.
11. Pulsa **Switch to view mode** para salir del modo edición.

> Si el diálogo de guardado no ofrece **Store time range**, el dashboard no almacenará el rango. En ese caso, al abrirlo aplica manualmente el rango del paso 2 y anótalo en la evidencia.

**Debe aparecer:** un dashboard con la métrica `10`, las barras `ssh=7 / web=6 / system=2`, la línea temporal con 6 fallos a las 11:00 y 2+2 a las 11:03–11:04 (UTC+2), la tabla de IPs con `203.0.113.45` y 10, y los 4 errores web.

> Si la línea temporal muestra conteos más bajos de lo esperado (por ejemplo, 2 en lugar de 6), revisa que el intervalo de **Horizontal axis** esté fijado en **1 minute** y no en **Auto**. Después pulsa **Refresh** en el dashboard.

## 7. Exportar los objetos de Kibana

### Opción A — Desde la interfaz

1. **Menú:** **Stack Management** → **Saved Objects**.
2. Selecciona la vista, las cinco visualizaciones y el dashboard.
3. Pulsa **Export**.
4. Guarda el archivo como `kibana-saved-objects.ndjson` en la carpeta de evidencia.

### Opción B — Por API

```bash
mkdir -p ../../laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos
curl -fsS -X POST 'http://localhost:5601/api/saved_objects/_export' \
  -H 'kbn-xsrf: true' \
  -H 'Content-Type: application/json' \
  -d '{"type":["dashboard","visualization","search","index-pattern"],"includeReferencesDeep":true}' \
  -o ../../laboratorio-final/evidencias/2026-10-19-10-elk-ingesta/artefactos/kibana-saved-objects.ndjson
```

**Debe aparecer:** un archivo NDJSON con el dashboard y sus referencias.

> La ruta de evidencia usa la fecha de ejecución `2026-10-19`. Si repites el laboratorio otro día, cambia la carpeta por la fecha correspondiente.

## 8. Evidencia a capturar

| Artefacto | Cómo obtenerlo | Destino |
|---|---|---|
| Vista de datos | Captura de Stack Management → Data Views | `artefactos/data-view.png` |
| Consultas | Captura de Discover con una consulta y sus hits | `artefactos/consultas-kql.png` |
| Dashboard | Captura del dashboard completo | `artefactos/dashboard.png` |
| Objetos exportados | Opción A o B | `artefactos/kibana-saved-objects.ndjson` |
| Conteos por API | `curl` de la sección 5 | `artefactos/consultas-elasticsearch.txt` |

Guarda también un `README.md` en la carpeta de evidencia con:

- Fecha y entorno.
- Objetivo.
- Resultado: PASS o parcial.
- Consultas y conteos.
- Limitaciones.
- Enlaces a los artefactos.

Puedes usar la [plantilla de evidencia](../../../plantillas/evidencia-template.md).

## 9. Validación

| Prueba | Método | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|---|
| Vista de datos | Stack Management | 15 documentos | `Lab Security`, `lab-security-*`, `@timestamp`, 15 documentos | Validado en local |
| Fallos totales | KQL `event.outcome.keyword: "failure"` | 10 | 10 | Validado en local |
| Fuerza bruta SSH | KQL `service.name.keyword: "ssh"` | 6 | 6 | Validado en local |
| Correlación por IP | KQL `source.ip.keyword: "203.0.113.45"` | 10 | 10 | Validado en local |
| Errores web | KQL `http.response.status_code >= 400` | 4 | 4 | Validado en local |
| Actividad `sudo` | KQL `event.action.keyword: "sudo"` | 1 | 1 | Validado en local |
| Accesos a `/admin` | KQL `url.path.keyword: "/admin"` | 1 | 1 | Validado en local |
| Dashboard | Exportación NDJSON | Objetos presentes | 7 objetos exportados: vista, dashboard, 4 Lens y búsqueda | Validado en local |

## 10. Limpieza

Cuando termines la captura de evidencia:

```bash
./scripts/down.sh --yes
```

**Debe aparecer:** los contenedores y el volumen `lab_esdata` eliminados.

## 11. Coste y tiempo

- **Coste:** 0.
- **Tiempo estimado:** 60–90 minutos.

## 12. Limitaciones

- No hay autenticación en Kibana: es un laboratorio local.
- El dashboard se construye manualmente; la exportación NDJSON permite reproducirlo.
- Los datos son sintéticos y de bajo volumen.
- La detección es una consulta KQL, no una regla de alerta automatizada.

## 13. Referencias

- [Laboratorio ELK](../../lab/README.md).
- [Runbook 01 — Ingestión](../01-ingestion-logstash/runbook.md).
- [Plantilla de evidencia](../../../plantillas/evidencia-template.md).
