#!/usr/bin/env python3
"""Resume los JSONL de las tres tandas en una tabla legible."""
import glob
import json
import os
import sys

DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "artefactos")

for ruta in sorted(glob.glob(os.path.join(DIR, "tanda-*.jsonl"))):
    tanda = os.path.basename(ruta).split("-")[1].split(".")[0]
    eventos = [json.loads(l) for l in open(ruta, encoding="utf-8") if l.strip()]
    inicio = next((e["t"] for e in eventos if e["evento"] == "inicio"), None)
    resumen = next((e for e in eventos if e["evento"] == "resumen"), {})
    fin = next((e for e in eventos if e["evento"] == "fin"), {})
    controles = [e for e in eventos if e["evento"] == "control"]
    senales = resumen.get("senales", [])

    print(f"\n## Tanda {tanda}")
    for c in controles:
        print(f"control {c['prueba']}: {c.get('observado') or c.get('status')} {c.get('error') or ''}")
    print(f"peticiones={resumen.get('peticiones')} senales={[s['tipo'] for s in senales]}")
    print(f"tokens: entrada={resumen.get('tokens_entrada')} salida={resumen.get('tokens_salida')} segundos={resumen.get('segundos')}")
    print(f"fin: {str(fin.get('resumen'))[:300]}")
    primera = None
    for e in eventos:
        if e["evento"] == "senal" and primera is None:
            primera = round(e["t"] - inicio, 1)
    print(f"primera_senal_seg={primera}")

    print("| n | user | método | ruta | estado |")
    print("|---|---|---|---|---|")
    for e in eventos:
        if e["evento"] == "peticion":
            resp = next((r for r in eventos if r["evento"] == "respuesta" and r.get("n") == e["n"]), {})
            print(f"| {e['n']} | {e['user']} | {e['method']} | {e['path']} | {resp.get('status')} |")
