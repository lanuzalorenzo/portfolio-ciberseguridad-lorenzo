#!/usr/bin/env python3
"""App de laboratorio con sesión de servidor para la práctica de robo de cookie.

Solo para la VM y el host locales: credenciales sintéticas, sesión en memoria y
sin persistencia. No se despliega ni se expone fuera de la red del laboratorio.

Uso:
    python3 app.py
    python3 app.py --ttl 10          # caducidad corta para la prueba negativa
    python3 app.py --puerto 8000
"""

from __future__ import annotations

import argparse
import secrets
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

USUARIO = "demo"
CLAVE = "demo"
SESIONES: dict[str, float] = {}

FORMULARIO = """<!doctype html><meta charset="utf-8">
<h1>Entrar</h1>
<form method="post" action="/login">
  <p><label>Usuario <input name="u" value="demo"></label></p>
  <p><label>Clave <input name="p" type="password" value="demo"></label></p>
  <p><button>Entrar</button></p>
</form>"""

PRIVADO = """<!doctype html><meta charset="utf-8">
<h1>Zona privada</h1>
<p>Sesión válida. Esta página solo responde con la cookie <code>sid</code>.</p>
<form method="post" action="/logout"><button>Cerrar sesión</button></form>"""


class Manejador(BaseHTTPRequestHandler):
    ttl = 300

    def _responder(self, codigo, cuerpo, cookies=(), extra=()):
        self.send_response(codigo)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        for cabecera, valor in extra:
            self.send_header(cabecera, valor)
        for cookie in cookies:
            self.send_header("Set-Cookie", cookie)
        self.end_headers()
        self.wfile.write(cuerpo.encode("utf-8"))

    def _sid(self):
        for parte in self.headers.get("Cookie", "").split(";"):
            clave, _, valor = parte.strip().partition("=")
            if clave == "sid":
                return valor
        return ""

    def _valida(self):
        sid = self._sid()
        return sid in SESIONES and SESIONES[sid] > time.time()

    def do_GET(self):
        if self.path == "/":
            self._responder(302, "", extra=[("Location", "/login")])
        elif self.path == "/login":
            self._responder(200, FORMULARIO)
        elif self.path == "/privado":
            if self._valida():
                self._responder(200, PRIVADO)
            else:
                self._responder(302, "", extra=[("Location", "/login")])
        else:
            self._responder(404, "no")

    def do_POST(self):
        largo = int(self.headers.get("Content-Length", 0))
        datos = parse_qs(self.rfile.read(largo).decode("utf-8"))
        if self.path == "/login":
            if datos.get("u") == [USUARIO] and datos.get("p") == [CLAVE]:
                sid = secrets.token_urlsafe(16)
                SESIONES[sid] = time.time() + self.ttl
                self._responder(
                    200,
                    "<p>Sesión iniciada. <a href='/privado'>Ir a la zona privada</a></p>",
                    [f"sid={sid}; HttpOnly; Path=/; Max-Age={self.ttl}; SameSite=Lax"],
                )
            else:
                self._responder(403, "<p>Credenciales incorrectas.</p>")
        elif self.path == "/logout":
            SESIONES.pop(self._sid(), None)
            self._responder(
                200,
                "<p>Sesión cerrada.</p>",
                ["sid=; HttpOnly; Path=/; Max-Age=0; SameSite=Lax"],
            )
        else:
            self._responder(404, "no")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--puerto", type=int, default=8000)
    parser.add_argument("--ttl", type=int, default=300,
                        help="segundos de vida de la sesión (por defecto 300)")
    args = parser.parse_args()
    Manejador.ttl = args.ttl
    print(
        f"http://127.0.0.1:{args.puerto}/login · TTL {args.ttl}s · Ctrl+C para parar"
    )
    HTTPServer((args.host, args.puerto), Manejador).serve_forever()


if __name__ == "__main__":
    main()
