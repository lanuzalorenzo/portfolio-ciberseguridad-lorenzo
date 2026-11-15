# 08 | Robo y reutilización de la cookie de sesión

> **Estado:** **Diseño**. Comprobado en el equipo de trabajo contra el app local; falta la extracción desde un perfil real y la comprobación de las defensas del disco.
>
> **Referencias:** OWASP ASVS V3 (gestión de sesión) · NIST SP 800-63B · OWASP Session Management Cheat Sheet.

Una llave de hotel que sigue abriendo la habitación después de devolverla no es una llave: es una copia. Con la cookie de sesión pasa lo mismo. Si el servidor no la invalida al cerrar sesión y el navegador la guarda en disco como si fuera un fichero cualquiera, cualquiera que lea ese disco entra sin contraseña.

Este laboratorio mide las dos mitades del problema sobre una aplicación propia: si la sesión se cierra de verdad en el servidor y qué hace falta para reutilizar la cookie guardada.

## Qué se prueba

| Pregunta | Qué la responde |
|---|---|
| ¿Cerrar sesión invalida la cookie en el servidor? | Reutilizar la cookie después del cierre y comprobar que ya no abre la zona privada |
| ¿La cookie viaja protegida cuando se extrae del disco? | Descifrar el almacén de Chromium y obtener un valor utilizable |
| ¿Qué defensas del equipo la protegen? | Disco cifrado, llavero del escritorio y caducidad de la cookie |

## Alcance

Laboratorio local y propio. El app de prueba escucha en el equipo anfitrión y la máquina virtual lo alcanza por la red interna del hipervisor; el script solo admite destinos de esa red y perfiles de Chromium del propio equipo. No se prueba contra servicios ajenos, ni con cuentas personales, ni con datos reales.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso sin cookie | Petición a la zona privada sin cabecera | Redirección al inicio de sesión | 302 a la pantalla de acceso |
| Acceso con cookie válida | Sesión iniciada con una cuenta de demostración | Respuesta de la zona privada | 200 |
| Reutilización tras cerrar sesión | Cierre en el servidor y repetición de la petición | La cookie ya no sirve | 302 |
| Extracción desde un perfil real | Lectura del almacén de Chromium y descifrado | Valor utilizable y medible | Pendiente: solo probado con el perfil de laboratorio |
| Defensa del disco | Disco cifrado del equipo | La cookie no se lee sin la clave del sistema | Pendiente |
| Defensa del llavero | Secreto del llavero del escritorio | Sin llavero desbloqueado no se descifra | Pendiente |
| Caducidad | Cookie con fecha de expiración | El navegador deja de enviarla | Pendiente |

Las tres primeras filas están comprobadas en el equipo de trabajo; las cuatro últimas son lo que falta para cerrar la práctica. La tabla se actualiza al cerrarlas, no antes.

## Cómo se ejecuta

El app y el script viven en [`../../lab/sesion-cookie/`](../../lab/sesion-cookie/).

```bash
# 1. Estado de referencia: sin cookie
python3 extraer_cookie.py --sin-cookie

# 2. Extraer la cookie del perfil y probarla contra el app
python3 extraer_cookie.py --url http://10.0.2.2:8011

# 3. Cerrar sesión en el servidor y repetir la prueba
python3 extraer_cookie.py --url http://10.0.2.2:8011 --logout
```

El script no imprime el valor de la cookie: devuelve el estado HTTP y un `sha256` recortado que sirve de evidencia sin publicar el secreto. La captura que acompaña a la práctica muestra esas tres líneas.

## Lecciones

- Cerrar sesión solo en el cliente no cierra nada: si el servidor no invalida la sesión, la cookie copiada sigue valiendo hasta que caduque.
- Una cookie de sesión es una credencial completa. En disco debe valer lo mismo que una contraseña guardada en claro, y por eso el disco cifrado y el llavero dejan de ser un detalle.
- El cifrado del almacén del navegador no es un control de seguridad frente a quien ya controla el equipo: solo evita que la cookie se lea por accidente o con otro perfil de usuario.
- Medir las tres defensas por separado evita el error de dar por buena la que no se ha probado.

## Más detalle

- [App de laboratorio](../../lab/sesion-cookie/app.py): sesión en memoria, cierre en servidor y zona privada.
- [Script de extracción](../../lab/sesion-cookie/extraer_cookie.py): lectura y descifrado del almacén de Chromium, acotado al laboratorio.
