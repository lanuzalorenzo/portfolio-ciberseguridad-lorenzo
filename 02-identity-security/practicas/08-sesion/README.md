# 08 | Robo y reutilización de la cookie de sesión

> **Estado:** **Validado** en el servidor y en el llavero el 15/11/2026: cookie del perfil real de Brave, 200 con ella, 302 tras el cierre y 302 del servidor a los 32 s. La pila del disco se observó el 16/11: la raíz ext4 vive en un volumen LVM dentro de una partición `crypto_LUKS` según `lsblk`. El arranque sin la passphrase no se probó; que sin desbloquear el contenedor no se monte es la consecuencia esperada de esa pila.
>
> **Referencias:** OWASP ASVS V3 (verificación de seguridad de aplicaciones) · NIST SP 800-63B · OWASP Session Management Cheat Sheet.

Una llave de hotel que sigue abriendo la habitación después de devolverla no es una llave: es una copia. Con la cookie de sesión pasa lo mismo. Si el servidor no la invalida al cerrar sesión y el navegador la guarda en disco como un fichero cualquiera, quien lea ese disco entra sin contraseña.

**In English.** A hotel key that still opens the room after you hand it back is not a key, it is a copy. If the server does not invalidate the cookie on logout and the browser keeps it on disk, whoever reads that disk gets in without a password.

## Alcance

Local y propio, sin máquina virtual: app en el equipo y navegador de uso diario por loopback, con perfiles de Chromium, Chrome o Brave propios. Nada contra servicios ajenos ni datos reales.

## Qué se comprobó

| Prueba | Método | Esperado | Observado |
|---|---|---|---|
| Acceso sin cookie | Petición a la zona privada | Redirección | 302 a `/login` |
| Acceso con cookie válida | Cuenta de demostración y cookie del perfil real | 200 | 200 |
| Reutilización tras cerrar sesión | Cierre en el servidor y repetición | La cookie ya no sirve | 302 a `/login` |
| Extracción desde un perfil real | Lectura del almacén de Brave y descifrado | Valor utilizable | `v10`/`v11` con la clave del llavero de Brave |
| Defensa del disco | Pila del volumen raíz | Raíz dentro de un contenedor cifrado | `crypto_LUKS` → LVM → ext4 en `/` según `lsblk` del 16/11; el arranque sin passphrase no se probó, así que el bloqueo no se ejerció |
| Defensa del llavero | Clave del llavero del escritorio | Sin la clave no se descifra | Con otra clave el descifrado falla |
| Caducidad | App con TTL de 30 s | La cookie deja de valer | Expiración y `Max-Age` fijados por la app a 30 s; el servidor da 302 a los 32 s |

## Hallazgos

| Hallazgo | Impacto | Qué lo mitiga |
|---|---|---|
| La cookie guardada abre la zona privada sin contraseña | Alto | Cierre en el servidor y TTL corto |
| El almacén la guarda en disco | Alto | Disco cifrado y clave en el llavero |
| La ventana de reutilización depende del TTL | Medio | Caducidad corta en servidor y navegador |

En el app de prueba la entrada solo pide una cuenta de demostración, así que el robo salta esa barrera y no un segundo factor, que aquí no existe.

## Cómo se ejecuta

```bash
cd lab/sesion-cookie
python3 app.py --puerto 8011 --ttl 30 --host 127.0.0.1
python3 extraer_cookie.py --sin-cookie
python3 extraer_cookie.py --url http://127.0.0.1:8011
python3 extraer_cookie.py --url http://127.0.0.1:8011 --logout
```

El [app](../../lab/sesion-cookie/app.py) y el [script](../../lab/sesion-cookie/extraer_cookie.py) no imprimen la cookie: solo el estado HTTP y un `sha256` recortado. Salida completa: [evidencia del 15/11](../../../laboratorio-final/evidencias/2026-11-15-02-cookie-sesion/README.md).

## Lecciones

- Cerrar sesión solo en el cliente no cierra nada: si el servidor no invalida la sesión, la cookie copiada vale hasta que caduque.
- Una cookie es una credencial completa y en disco vale lo mismo que una contraseña en claro.
