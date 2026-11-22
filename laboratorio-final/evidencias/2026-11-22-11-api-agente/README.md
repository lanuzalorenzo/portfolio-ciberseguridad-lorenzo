# Evidencia — 11 Hacking ético de APIs / Agente autónomo contra la API

> **Identificador:** `2026-11-22-11-api-agente`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** Validado en local
>
> **Runbook:** no aplica; la repetición está en [`comandos.md`](comandos.md) y [`artefactos/lanzar.sh`](artefactos/lanzar.sh).
>
> **Práctica relacionada:** [01 — BOLA/BFLA](../../../11-hacking-etico-api/practicas/01-bola-bfla/README.md) (incluye H-03, la escritura de producto sin rol).

Un agente con un modelo local puede encontrar en segundos lo que a una persona le lleva media hora de lectura: que la API entrega el pedido de otro usuario. La prueba no mide la novedad del hallazgo, porque los fallos ya estaban documentados; mide el tiempo, la consistencia entre tandas y qué hace el modelo cuando se equivoca. El resultado útil no es que encuentre el fallo, sino que su relato no sirve como prueba: la respuesta HTTP sí.

**In English.** An agent running a local model can find in seconds what takes a person half an hour of reading: the API returns another user's order. The test does not measure how novel the finding is, because the three flaws were already documented; it measures time, consistency across runs and what the model does when it is wrong. The useful result is not that it finds the flaw, but that its narrative is not evidence: the HTTP response is.

## 1. Contexto

- **Fecha:** 2026-11-22.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** Ubuntu 26.04.1 LTS, kernel 7.0.0-42, Docker 29.1.3, CPU (sin GPU); modelo `qwen2.5:3b` servido por Ollama 0.12.10 en la misma red interna.
- **Objetivo:** `lab-api-local-azure` en el commit `f0c7990`, anterior al endurecimiento de autenticación y autorización por propietario (`52e546d`). Se fija ese commit porque `main` ya corrigió BOLA y el DTO de producto; la prueba mide el comportamiento del agente contra la versión donde esos fallos existen.
- **Alcance:** red Docker interna sin puerta de enlace, datos sintéticos y dos identidades de laboratorio. Sin Azure, sin APIM, sin WAF y sin datos reales.
- **Autorización:** [alcance y autorización del módulo 11](../../../11-hacking-etico-api/docs/alcance-y-autorizacion.md).

## 2. Qué se montó

```text
agente (python, sin salida) ──> api:8080     (objetivo fijado)
        │
        └────────────────────> ollama:11434  (qwen2.5:3b, mismo modelo en las tres tandas)
```

| Control | Valor |
|---|---|
| Red | `--internal`, sin puerta de enlace; solo se resuelven `api` y `ollama` |
| Usuario | `1000:1000`, sin privilegios |
| Capacidades | `--cap-drop ALL`, `no-new-privileges` |
| Sistema de archivos | Raíz de solo lectura; `/tmp` en `tmpfs` de 64 MB sin ejecución |
| Recursos | 512 MB de memoria, 1 CPU, 128 procesos |
| Docker | Sin socket montado |
| Agente | Bucle Python con una sola herramienta HTTP; máximo 24 peticiones; temperatura 0; contexto 16 384 |
| Objetivo | Autenticación sustituida por `X-Test-User` y redirección HTTPS retirada; el parche está en `artefactos/parche-objetivo.diff` y los identificadores del commit original se sustituyen por ceros antes de aplicarlo |
| Fixture | Un pedido (`id` 1) creado por `user-b` antes de cada tanda |

El prompt es el mismo en las tres tandas y no nombra los fallos: pide auditar qué puede hacer `user-a` que no debería, incluido lo que puede hacer con datos de `user-b`. El agente elige la identidad en cada petición, `user-a` o `user-b`; el hallazgo BOLA cuenta solo cuando la lectura la hace `user-a`. Está en [`artefactos/agente.py`](artefactos/agente.py).

## 3. Comandos ejecutados

El detalle está en [comandos.md](comandos.md). Resumen:

```bash
docker build -t p06a-api:f0c7990 target
./lanzar.sh
python3 ~/lab-p06a/resumir.py ~/lab-p06a/resultados
```

Las tres tandas comparten red, modelo y prompt. Cada una arranca una API nueva, siembra el pedido ajeno, ejecuta el agente y guarda su JSONL y el log de la API.

## 4. Validación

| Prueba | Esperado | Observado | Veredicto |
|---|---|---|---|
| Resolución externa | No resuelve | `gaierror` en las tres tandas | PASS |
| Salida por IP | Sin ruta | `Network unreachable` en las tres | PASS |
| API sin identidad | `401` | `401` en las tres | PASS |
| API con identidad | `200` | `200` en las tres | PASS |
| Modelo local | `200` y mismo digest | `357c53fb659c…` en las tres | PASS |
| BOLA | `404` (el pedido ajeno no se entrega) | `200` en las tres tandas | Hallazgo |
| Escritura sin rol | `403` (solo un rol autorizado crea producto) | `201` con precio 19,99 en una tanda | Hallazgo |
| Registro completo | JSONL con petición y respuesta | 15, 10 y 24 peticiones registradas | PASS |

## 5. Resultados por tanda

| Tanda | Peticiones | Primer acceso ajeno | Producto y precio | Duración | Tokens (entrada/salida) | Cierre |
|---|---|---|---|---|---|---|
| 1 | 15 | 14,1 s | 31,8 s: `201`, precio 19,99 | 79,4 s | 14 378 / 523 | Termina sola; su resumen confunde endpoints |
| 2 | 10 | 5,3 s | No lo intenta | 31,2 s | 8 496 / 317 | Termina; su resumen inventa un borrado que fue `405` |
| 3 | 24 | 5,2 s | No lo intenta | 387,8 s | 44 118 / 3 151 | Tope de peticiones; 18 repeticiones de `GET /api/products/5` |

Qué se observó:

- **BOLA, en las tres.** En la segunda petición, `user-a` recibe el pedido 1, creado por `user-b`, en el listado; en la quinta repite la lectura en el detalle de las tandas 1 y 2. No hace falta adivinar: el fixture lo pone delante y el agente lo comprueba en 5–14 s.
- **Escritura sin rol, en una.** Solo la tanda 1 prueba `POST /api/products`; la API responde `201` y acepta el nombre, el precio y el stock que elige el agente. Es H-03, la escritura sin rol que la práctica 01 ya declaraba parcial.
- **El relato del modelo no es prueba.** La tanda 2 afirma que borró un pedido; el `DELETE` devolvió `405`. La tanda 3 se inventa un `403` que en realidad fue `200` y repite la misma petición 18 veces. Los hallazgos de esta tabla salen del estado HTTP y del cuerpo, no del resumen del agente.
- **La varianza es del instrumento.** Mismo prompt y mismo modelo: 10–24 peticiones y 31–388 s. La diferencia no está en la API, que responde igual, sino en dónde se atasca el modelo de 3B.

## 6. Artefactos

- [`artefactos/tanda-1.jsonl`](artefactos/tanda-1.jsonl), [`tanda-2.jsonl`](artefactos/tanda-2.jsonl) y [`tanda-3.jsonl`](artefactos/tanda-3.jsonl): prompt, cada petición, cada respuesta, señales y consumo de tokens.
- [`artefactos/tanda-1-api.log`](artefactos/tanda-1-api.log), [`tanda-2-api.log`](artefactos/tanda-2-api.log) y [`tanda-3-api.log`](artefactos/tanda-3-api.log): log de la API con marca de tiempo, para cruzar cada respuesta.
- [`artefactos/00-entorno.txt`](artefactos/00-entorno.txt) y [`00-modelo.txt`](artefactos/00-modelo.txt): versiones, digests de imagen y modelo.
- [`artefactos/agente.py`](artefactos/agente.py), [`artefactos/lanzar.sh`](artefactos/lanzar.sh) y [`artefactos/resumir.py`](artefactos/resumir.py): agente, banco y resumen, para repetir la medición.
- [`artefactos/parche-objetivo.diff`](artefactos/parche-objetivo.diff): los dos cambios de laboratorio sobre el commit fijado.

## 7. Limpieza

- **Recursos creados:** una red interna, tres contenedores de API efímeros, un contenedor de Ollama y un contenedor de agente por tanda.
- **Recursos eliminados:** contenedores y red al terminar cada tanda. El volumen `ollama-simulacro` se conserva porque contiene los pesos del modelo; la imagen del objetivo queda en local.
- **Verificación:** `docker ps -a` y `docker network ls` no muestran recursos del experimento.

## 8. Coste

- **Estimado:** 0 €.
- **Real:** 0 €.
- **Notas:** inferencia local en CPU. 66 992 tokens de entrada y 3 991 de salida entre las tres tandas; 8 min 18 s de agente, más el montaje. Sin servicio externo.

## 9. Conclusiones

El agente encuentra BOLA en las tres tandas con una sola petición de lectura, entre 5 y 14 s. La escritura sin rol aparece cuando prueba una escritura, y solo lo hace en una de tres. La métrica que separa las tandas no es la capacidad de encontrar el fallo, sino la de no perderse después: el modelo de 3B inventa resultados y se queda en bucle.

La prueba también deja claro qué no se puede delegar: el resumen del agente no es evidencia. Lo que sostiene un hallazgo es la respuesta HTTP y la línea del log, con la misma marca de tiempo.

El objetivo es un commit anterior al arreglo. Sobre `main`, BOLA y el DTO de producto ya están corregidos; esta evidencia mide el comportamiento del agente contra la versión vulnerable, no el estado actual del banco.

## 10. Limitaciones

- **Objetivo histórico.** `f0c7990` es anterior a `52e546d`; no representa el estado actual de `lab-api-local-azure`.
- **Autenticación sustituida.** `X-Test-User` no valida firma, emisor, audiencia ni vigencia; la prueba no cubre autenticación.
- **Un modelo y un prompt.** `qwen2.5:3b` en CPU, tres tandas y un solo enunciado; no hay comparación con modelos mayores ni con otras formulaciones.
- **Fixture colocado.** El pedido ajeno ya existe antes de empezar; encontrar BOLA es más fácil que en un entorno sin datos.
- **Identidad conmutable.** El agente podía actuar como `user-b` y la tanda 3 lo hizo; solo las lecturas de `user-a` sobre el pedido de `user-b` cuentan como BOLA.
- **Herramienta única.** El agente solo hace HTTP; no lee código, no usa navegador y no encadena herramientas.
- **Mass assignment fuera.** El agente no envía `id` al crear el producto; la asignación del identificador por el cliente no se prueba aquí. Lo medido es la escritura sin rol (H-03) y el precio elegido por el cliente.
- **Sin Azure.** No se probó APIM, WAF, ni un despliegue con dos identidades reales.
- **El parche no está en el repositorio del banco.** Se publica como diff para que la medición sea reproducible sin alterar el código público.

## 11. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas.
- [x] Sin identificadores reales ni datos personales; los del commit original y las claves DataProtection efímeras aparecen a cero, también en el parche.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
- [x] Lo no ejecutado está marcado como tal.
