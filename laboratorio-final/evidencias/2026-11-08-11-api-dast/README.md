# Evidencia — Módulo 11 / DAST sin autenticar sobre EcommerceApi

> **Identificador:** `2026-11-08-11-api-dast`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** Parcial
>
> **Runbook:** [`runbook.md`](runbook.md).

Un escáner DAST (análisis dinámico de aplicaciones) es como un revisor que recorre la casa con una lista: comprueba lo que está a la vista, no abre puertas cerradas. Aquí solo había una puerta abierta, `/health`; el resto de la API exige una llave que el laboratorio no tiene.

## 1. Contexto

- **Fecha:** 2026-11-08
- **Responsable:** autor del repositorio
- **Entorno:** Linux 7.0.0-38 x86_64 con Docker 29.1.3; API `ecommerce-api:local` construida desde `f202777`; OWASP ZAP 2.17.0 en contenedor (`sha256:9624669d…`).
- **Alcance:** superficie HTTP anónima de la API en Docker. ZAP parte de `/health` y de la raíz; la raíz devuelve `404` y no aporta enlaces. Los endpoints de negocio exigen un JWT de Entra ID y el laboratorio no tiene tenant, así que quedan fuera.
- **Datos:** sintéticos; sin credenciales ni tokens.
- **Autorización:** no aplica; sin recursos cloud. La imagen de ZAP se descarga una vez de `ghcr.io`.

## 2. Comandos ejecutados

En [`comandos.md`](comandos.md), con la salida redactada: arranque de la API, comprobación de `/health` y ejecución del baseline.

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| La API responde | `200` en `/health` | `200`, Kestrel y cabeceras de seguridad | PASS |
| ZAP recorre la superficie | al menos `/health` | 5 URLs, 4 endpoints; 2 respuestas son `404` | PASS con alcance `/health` |
| Sin hallazgos altos | 0 FAIL, 0 WARN | 0 FAIL, 0 WARN, 62 PASS | PASS |
| Cobertura de endpoints de negocio | peticiones autenticadas | `401` sin token; no escaneados | **No ejecutada**: falta tenant |

El plan de automatización avisa de que la raíz devuelve `404` y que el spider no encontró enlaces que llevaran a más endpoints; el alcance real es `/health`.

## 4. Artefactos

- [`artefactos/zap-report.html`](artefactos/zap-report.html): informe completo.
- [`artefactos/zap-report.md`](artefactos/zap-report.md): resumen en Markdown.
- [`artefactos/zap-report.json`](artefactos/zap-report.json): salida estructurada de ZAP 2.17.0.
- [`artefactos/zap.yaml`](artefactos/zap.yaml): plan de automatización ejecutado.
- [`artefactos/zap-baseline.log`](artefactos/zap-baseline.log): salida de consola, con los 62 PASS y el aviso del spider.
- [`artefactos/entorno.txt`](artefactos/entorno.txt): versiones y digests de la ejecución.

## 5. Limpieza

- **Recursos creados:** contenedor efímero de ZAP y los informes en `artefactos/`.
- **Recursos eliminados:** el intento de contenedor en `Development` (`api-dast` y su volumen) y el contenedor de la API al terminar (`docker compose down`); el volumen `api-data` se conserva.
- **Verificación:** `docker compose ps` ya no muestra el servicio `api`; la base SQLite sigue en el volumen.

## 6. Coste

- **Estimado:** 15 min.
- **Real:** unos 20 min, incluida la descarga de la imagen de ZAP.
- **Notas:** sin coste cloud.

## 7. Conclusiones

La superficie anónima de la API no devuelve ningún hallazgo pasivo: cabeceras de seguridad presentes, sin cookies y sin número de versión. La cabecera `Server: Kestrel` revela el servidor, no su versión. Eso no cubre los endpoints de negocio, que quedan detrás de JWT y de un tenant que el laboratorio no tiene.

## 8. Limitaciones y lo no ejecutado

- El baseline no prueba los endpoints autenticados: sin token solo devuelven `401`.
- Swagger está apagado en Producción, así que no hay especificación OpenAPI que importar.
- El arranque en `Development` falla por una dependencia cautiva: `ProcessOrderHandler` es singleton y consume `IProcessedMessageStore`, que es scoped. El contenedor sale con código `139` tras la excepción. Queda anotado para el caso de remediación, no se corrige aquí.
- No se ejecutó escaneo activo ni autenticado.
- No se ejecutó una prueba de control contra un objetivo vulnerable conocido; el `0 FAIL` no demuestra por sí solo que el escáner detecte fallos.

## 10. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas.
- [x] Sin identificadores reales ni datos personales.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
- [x] Lo no ejecutado está marcado como tal.
