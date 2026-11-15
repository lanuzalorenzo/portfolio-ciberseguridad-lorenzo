# 08 | Robo y reutilización de la cookie de sesión

> **Estado:** **Validado** el 15/11/2026 en el equipo de trabajo: cookie extraída del perfil real de Brave, reutilizada contra la zona privada, muerta tras cerrar sesión y caducidad medida. El bloqueo del disco cifrado se deduce del diseño; el arranque sin clave no se probó.
>
> **Referencias:** OWASP ASVS V3 · NIST SP 800-63B · OWASP Session Management Cheat Sheet.

Una llave de hotel que sigue abriendo la habitación después de devolverla no es una llave: es una copia. Con la cookie de sesión pasa lo mismo. Si el servidor no la invalida al cerrar sesión y el navegador la guarda en disco como un fichero cualquiera, quien lea ese disco entra sin contraseña.

**In English.** A hotel key that still opens the room after you hand it back is not a key, it is a copy. If the server does not invalidate the cookie on logout and the browser keeps it on disk, whoever reads that disk gets in without a password.

## Alcance

Local y propio, sin máquina virtual: app en el equipo, navegador de uso diario por loopback y perfiles de Chromium, Chrome o Brave propios. Nada contra servicios ajenos, cuentas personales ni datos reales.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso sin cookie | Petición a la zona privada sin cabecera | Redirección | 302 a `/login` |
| Acceso con cookie válida | Cuenta de demostración y cookie del perfil real | 200 | 200 |
| Reutilización tras cerrar sesión | Cierre en el servidor y repetición | La cookie ya no sirve | 302 a `/login` |
| Extracción desde un perfil real | Lectura del almacén de Brave y descifrado | Valor utilizable | `v10`/`v11` con la clave del llavero de Brave |
| Defensa del disco | Estado del volumen raíz | Disco cifrado | LUKS según `lsblk`; el bloqueo sin passphrase se deduce, no se midió |
| Defensa del llavero | Clave del llavero del escritorio | Sin la clave no se descifra | Con otra clave el descifrado falla |
| Caducidad | App con TTL de 30 s | La cookie deja de valer | Expiración guardada a 30 s; el servidor responde 302 a los 32 s |

## Hallazgos

La cookie guardada abre la zona privada sin contraseña: aquí la entrada solo pide una cuenta de demostración, así que el robo salta esa barrera, no un segundo factor que no existe. Quien lea el disco se lleva la credencial entera; la ventana la acotan el TTL del servidor y la caducidad del navegador, que coincidieron en 30 s.

## Cómo se ejecuta

```bash
python3 app.py --puerto 8011 --ttl 30 --host 127.0.0.1
python3 extraer_cookie.py --sin-cookie
python3 extraer_cookie.py --url http://127.0.0.1:8011
python3 extraer_cookie.py --url http://127.0.0.1:8011 --logout
```

El [app](../../lab/sesion-cookie/app.py) y el [script](../../lab/sesion-cookie/extraer_cookie.py) viven en `lab/sesion-cookie/`; el script no imprime la cookie, solo el estado HTTP y un `sha256` recortado. Salida completa: [evidencia del 15/11](evidencias/2026-11-15-cookie-sesion.md).

## Lecciones

- Cerrar sesión solo en el cliente no cierra nada: si el servidor no invalida la sesión, la cookie copiada vale hasta que caduque.
- Una cookie es una credencial completa y en disco vale lo mismo que una contraseña en claro.
