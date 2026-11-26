#!/usr/bin/env python3
"""Cruce del JSONL del agente con el log de la API, para la tabla de detección.

Uso: python3 deteccion.py <carpeta-de-artefactos>

Solo lee los artefactos de la evidencia y cuenta lo que hay. No interpreta el
relato del agente: cada cifra sale de una línea del log o del JSONL.

Salida: capacidades del log, cruce por marca de tiempo, eventos por tanda,
repetición por ruta, identidad por petición y prueba negativa del contador.
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

TANDAS = (1, 2, 3)
# Dos peticiones iguales seguidas se separan por segundos; el cruce exige
# método, ruta y una diferencia menor que este umbral.
DELTA_MAX = 1.0
# Control negativo: cinco repeticiones de la misma petición en diez minutos.
# El umbral se aplica igual al log entero y a las líneas que no son del agente.
VENTANA = 600
UMBRAL = 5
FINISHED = re.compile(
    r"^(?P<ts>\S+Z)\s+Request finished HTTP/[\d.]+ (?P<metodo>[A-Z]+) (?P<url>\S+)"
    r" - (?P<estado>\d{3}) .*? (?P<ms>[\d.]+)ms$"
)
ACCION = re.compile(r"Executed action (?P<accion>[\w.]+) \(")
CAPACIDADES = {
    "método, ruta y duración": r"Request finished HTTP/",
    "estado HTTP": r"Request finished HTTP/[\d.]+ \w+ \S+ - \d{3} ",
    "acción del controlador": r"Executed action ",
    "identidad (X-Test-User)": r"X-Test-User",
    "identidad de laboratorio (user-a / user-b)": r"user-[ab]",
    "cuerpo de la petición": r"Request body",
    "cuerpo de la respuesta": r"Response body",
    "origen de red (ConnectionId / RemoteIp)": r"ConnectionId|RemoteIp",
    "cliente (User-Agent)": r"User-Agent",
    "correlación (TraceId / SpanId)": r"TraceId|SpanId",
}


def epoch(ts):
    # El log escribe nanosegundos; basta con microsegundos para el cruce.
    fecha, resto = ts.split(".")
    return datetime.strptime(f"{fecha}.{resto[:6]}", "%Y-%m-%dT%H:%M:%S.%f").replace(
        tzinfo=timezone.utc
    ).timestamp()


def leer_log(ruta):
    lineas = []
    for cruda in ruta.read_text().splitlines():
        m = FINISHED.match(cruda)
        if m:
            lineas.append(
                {
                    "t": epoch(m["ts"]),
                    "ts": m["ts"][11:23],
                    "metodo": m["metodo"],
                    "ruta": m["url"].split("api:8080", 1)[-1],
                    "estado": int(m["estado"]),
                    "ms": float(m["ms"]),
                }
            )
    return lineas


def leer_jsonl(ruta):
    return [
        e
        for e in (json.loads(l) for l in ruta.read_text().splitlines() if l.strip())
        if e.get("evento") == "peticion"
    ]


def cruzar(log, reqs):
    """Empareja cada petición con su línea. Devuelve (parejas, deltas, sin)."""
    usadas = {}
    parejas = {}
    deltas = []
    sin = []
    for r in reqs:
        candidatas = [
            (abs(l["t"] - r["t"]), i)
            for i, l in enumerate(log)
            if i not in usadas
            and l["metodo"] == r["method"]
            and l["ruta"] == r["path"]
            and abs(l["t"] - r["t"]) <= DELTA_MAX
        ]
        if not candidatas:
            sin.append(r)
            continue
        delta, i = min(candidatas)
        usadas[i] = r
        parejas[i] = r
        deltas.append(delta * 1000)
    sobran = [l for i, l in enumerate(log) if i not in usadas]
    return parejas, deltas, sin, sobran


def racha(lineas, ventana=VENTANA):
    """Petición que más se repite dentro de una ventana. Devuelve su cuenta."""
    mejor = ((None, None), 0, "—", "—", 0.0)
    for i, l in enumerate(lineas):
        clave = (l["metodo"], l["ruta"])
        dentro = [
            o
            for o in lineas[i:]
            if o["t"] - l["t"] <= ventana and (o["metodo"], o["ruta"]) == clave
        ]
        if len(dentro) > mejor[1]:
            mejor = (
                clave,
                len(dentro),
                dentro[0]["ts"],
                dentro[-1]["ts"],
                dentro[-1]["t"] - dentro[0]["t"],
            )
    return mejor


def main():
    base = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    print("# Detección — cruce de JSONL y log de la API")
    print()

    logs = {n: leer_log(base / f"tanda-{n}-api.log") for n in TANDAS}
    reqs = {n: leer_jsonl(base / f"tanda-{n}.jsonl") for n in TANDAS}
    cruces = {n: cruzar(logs[n], reqs[n]) for n in TANDAS}

    print("## 1. Qué registra el log")
    print()
    print("| Dato | Tanda 1 | Tanda 2 | Tanda 3 |")
    print("|---|---|---|---|")
    for nombre, patron in CAPACIDADES.items():
        celdas = [
            str(len(re.findall(patron, (base / f"tanda-{n}-api.log").read_text())))
            for n in TANDAS
        ]
        print(f"| {nombre} | {' | '.join(celdas)} |")
    print()

    print("## 2. Cruce petición ↔ log por marca de tiempo")
    print()
    print("| Tanda | Peticiones del agente | Con línea en el log | Delta máximo | Sin pareja |")
    print("|---|---|---|---|---|")
    for n in TANDAS:
        _, deltas, sin, _ = cruces[n]
        print(
            f"| {n} | {len(reqs[n])} | {len(deltas)} | {max(deltas):.0f} ms | {len(sin)} |"
        )
    print()

    print("## 3. Líneas del log que no son peticiones del agente")
    print()
    for n in TANDAS:
        _, _, _, sobran = cruces[n]
        detalle = ", ".join(f"{l['metodo']} {l['ruta']} {l['estado']}" for l in sobran)
        print(f"- Tanda {n}: {len(sobran)} — {detalle}")
    print()

    print("## 4. Eventos por tanda, con su línea")
    print()
    print("| Evento | Tanda 1 | Tanda 2 | Tanda 3 |")
    print("|---|---|---|---|")

    def fila(nombre, filtro):
        celdas = []
        for n in TANDAS:
            parejas = cruces[n][0]
            hallados = [
                l for i, l in enumerate(logs[n]) if filtro(l, parejas.get(i))
            ]
            if hallados:
                celdas.append(f"{len(hallados)} ({hallados[0]['estado']}) desde {hallados[0]['ts'][:8]}")
            else:
                celdas.append("0")
        print(f"| {nombre} | {' | '.join(celdas)} |")

    fila(
        "Lectura del pedido ajeno (`GET /api/orders/1` por `user-a`)",
        lambda l, r: l["metodo"] == "GET"
        and l["ruta"] == "/api/orders/1"
        and l["estado"] == 200
        and (r or {}).get("user") == "user-a",
    )
    fila(
        "Listado de pedidos (`GET /api/orders`)",
        lambda l, r: l["metodo"] == "GET" and l["ruta"] == "/api/orders" and l["estado"] == 200,
    )
    fila(
        "Escritura sin rol (`POST /api/products`)",
        lambda l, r: l["metodo"] == "POST" and l["ruta"] == "/api/products",
    )
    fila(
        "Intento de borrado (`DELETE`)",
        lambda l, r: l["metodo"] == "DELETE",
    )
    fila(
        "Sonda y control sin identidad (`401`)",
        lambda l, r: l["estado"] == 401,
    )
    print()

    print("## 5. Repetición por ruta (máximo de una misma petición)")
    print()
    for n in TANDAS:
        cuenta = {}
        for l in logs[n]:
            clave = (l["metodo"], l["ruta"])
            cuenta[clave] = cuenta.get(clave, 0) + 1
        (metodo, ruta), veces = max(cuenta.items(), key=lambda kv: kv[1])
        print(f"- Tanda {n}: {veces} × `{metodo} {ruta}`")
    print()
    print("Peticiones a `GET /api/products/5`, por tanda, con la primera y la última:")
    print()
    for n in TANDAS:
        suyas = [
            l for l in logs[n] if l["metodo"] == "GET" and l["ruta"] == "/api/products/5"
        ]
        if not suyas:
            print(f"- Tanda {n}: 0")
            continue
        segundos = suyas[-1]["t"] - suyas[0]["t"]
        print(
            f"- Tanda {n}: {len(suyas)} entre {suyas[0]['ts'][:8]} y "
            f"{suyas[-1]['ts'][:8]} ({int(segundos // 60)} min {int(segundos % 60)} s)"
        )
    print()

    print("## 6. Identidad por petición (solo en el JSONL)")
    print()
    for n in TANDAS:
        usuarios = {}
        for r in reqs[n]:
            usuarios[r.get("user")] = usuarios.get(r.get("user"), 0) + 1
        detalle = ", ".join(f"{u}={c}" for u, c in sorted(usuarios.items()))
        print(f"- Tanda {n}: {detalle}")
    print()
    print("El log no contiene esa columna: `grep -c 'user-a\\|user-b'` da 0 en las tres.")
    print()

    print("## 7. Prueba negativa del contador")
    print()
    print(
        f"Umbral: {UMBRAL} repeticiones de la misma petición en "
        f"{VENTANA // 60} min. Sin umbral, cualquier lectura repetida sería "
        "abuso. El control son las líneas del log que no son del agente "
        "(sonda, sembrado y comprobaciones)."
    )
    print()
    print("| Conjunto | Máximo | Petición | Primera–última | Duración | Alerta |")
    print("|---|---:|---|---|---:|---|")
    mayor = 0.0
    conjuntos = [(f"Tanda {n}", logs[n]) for n in TANDAS]
    conjuntos += [(f"Control {n}", cruces[n][3]) for n in TANDAS]
    for nombre, conjunto in conjuntos:
        clave, veces, ini, fin, duracion = racha(conjunto)
        if veces == 0:
            print(f"| {nombre} | 0 | — | — | — | no |")
            continue
        mayor = max(mayor, duracion)
        print(
            f"| {nombre} | {veces} | `{clave[0]} {clave[1]}` | "
            f"{ini}–{fin} | {duracion:.0f} s | {'sí' if veces >= UMBRAL else 'no'} |"
        )
    print()
    if mayor < VENTANA:
        print(
            f"La ventana de {VENTANA // 60} min no se ejercita: el conjunto más "
            f"largo dura {mayor:.0f} s; lo probado es el umbral."
        )
        print()


if __name__ == "__main__":
    main()
