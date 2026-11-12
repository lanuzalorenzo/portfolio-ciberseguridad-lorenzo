# Evidencia — Remediación de la cabecera `Server` en EcommerceApi

> **Identificador:** `2026-11-09-07-remediacion-server-header`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** **Validado en local y en CI**
>
> **Runbook:** no aplica; es un caso de remediación, no una práctica reejecutable.

Un hallazgo arreglado sin prueba es como cerrar una grieta tapándola con cinta y no volver a mirar: no se sabe si la cinta aguanta ni si la grieta sigue ahí debajo. Este caso toma un defecto real y pequeño, la huella del servidor web, y lo demuestra en el orden correcto: la prueba falla antes del cambio, pasa después y un check recién añadido impide que vuelva.

**In English.** A finding closed without a test is like sealing a crack with tape and never looking again: you learn neither whether the tape holds nor whether the crack is still underneath. This case takes a small, real defect — the web server fingerprint — and proves it in the right order: the check fails before the change, passes after it, and a new pipeline gate keeps it from coming back.

## 1. Contexto

- **Fecha:** 2026-11-09.
- **Responsable:** autor del repositorio.
- **Entorno local:** Ubuntu 26.04.1 LTS, Docker 29.1.3 y Compose 2.40.3; imagen construida desde `main` con el `Dockerfile` del repositorio.
- **Entorno de CI:** GitHub Actions, job `container-security` del workflow `devsecops-ci.yml`.
- **Objetivo:** [EcommerceApi](https://github.com/lanuzalorenzo/lab-api-local-azure), la misma carga del resto del portfolio.
- **Alcance:** una cabecera de respuesta en las rutas anónimas. La validación de token y los endpoints de negocio quedan fuera.
- **Datos:** sin datos personales, credenciales ni recursos cloud.

## 2. Hallazgo

Con el contenedor en marcha, `curl -D - -o /dev/null` contra `/health` devolvió `200` con la cabecera `Server: Kestrel`. Aparecía también en el `401` de `/api/products` y en un `404`. Cualquier cliente anónimo sabe así qué servidor web hay detrás.

## 3. Causa

Kestrel publica esa cabecera por defecto (`KestrelServerOptions.AddServerHeader`). El proyecto ya fijaba cabeceras de seguridad con `UseSecurityHeaders` y no había ninguna prueba que cubriera esta, porque `TestServer`, el que usan las pruebas de integración, nunca la escribe: el defecto no era visible desde la suite.

## 4. Cambio

- `EcommerceApi/Program.cs`: `builder.WebHost.ConfigureKestrel(options => options.AddServerHeader = false)`.
- `tests/EcommerceApi.Tests/ServerHeaderTests.cs`: fija la opción para que un refactor no la reactive.
- `scripts/check-server-header.sh`: falla si la cabecera reaparece en una URL dada.
- Job `container-security`: arranca la imagen, espera `/health` y ejecuta el script después del escaneo y la publicación del SARIF de Trivy.
- `docs/api.md` y `docs/capacidades.md`: documentan la capacidad y su comprobación.

Cambio: [`b328fcc`](https://github.com/lanuzalorenzo/lab-api-local-azure/commit/b328fcc81b0615bb4bbbf913e266a57c2837a740), PR [#52](https://github.com/lanuzalorenzo/lab-api-local-azure/pull/52). El control no se quedó en `Program.cs`: pasó a `LL.Security 0.3.0`, dentro de `UseSecurityHeaders` y con la opción `SuppressServerHeader`, para que cualquier API que monte el paquete lo herede; el consumidor ya no configura Kestrel.

## 5. Prueba de regresión

| Momento | Prueba | Resultado |
|---|---|---|
| Antes del cambio | `scripts/check-server-header.sh http://localhost:8080/health` (script del árbol de trabajo) contra la imagen construida desde `main` | Sale 1 e imprime `Server: Kestrel` |
| Antes del cambio | `ServerHeaderTests` sin el apagado, ni en `Program.cs` ni en el paquete | Falla: `AddServerHeader` es `true` |
| Después del cambio | El mismo script contra la imagen corregida | Sale 0: «Sin cabecera Server» |
| Después del cambio | Suite completa | 88 pruebas, 0 fallos; `/health` sigue en `200` y las cabeceras de seguridad no cambian |

Los comandos y la salida redactada están en [`comandos.md`](comandos.md); las cabeceras, en [`artefactos/cabeceras.txt`](artefactos/cabeceras.txt).

## 6. Ejecución posterior, fechada

El run [42685834576](https://github.com/lanuzalorenzo/lab-api-local-azure/actions/runs/42685834576) del 2026-11-09 ejecutó el paso nuevo contra la imagen del commit y registró «Sin cabecera Server en http://localhost:8080/health». Los siete checks del pipeline pasaron y la PR se fusionó con squash.

## 7. Límites

- La comprobación cubre el contenedor que sirve Kestrel, no una capa delante de él. Un front end de App Service o un proxy podrían añadir su propia cabecera y este check no lo vería.
- La suite de pruebas no reproduce la cabecera: `TestServer` no la escribe. Por eso la ausencia en HTTP se demuestra contra el contenedor, y la prueba de integración solo fija la opción.
- Solo se comprobaron rutas anónimas; las autenticadas pasan por las mismas cabeceras, pero no se midieron una a una.

## 8. Severidad CVSS 3.1

| Campo | Valor |
|---|---|
| Fecha | 2026-11-12 |
| Versión | CVSS 3.1 |
| Vector | `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N` |
| Puntuación | **5,3 (Media)** |
| Justificación | Divulgación de información de reconocimiento desde la red: el producto (`Kestrel`) se anuncia en la respuesta, sin versión ni capacidad de ejecución. Confidencialidad baja; integridad y disponibilidad sin impacto. |
| Referencia | [07 — DevSecOps, severidad del hallazgo `Server`](../../../07-devsecops/README.md#severidad-del-hallazgo-server) |

La puntuación no convierte el hallazgo en un incidente: mide el valor de la huella para un atacante que prepara un ataque posterior. La remediación elimina esa señal, y el check de CI impide que vuelva.
