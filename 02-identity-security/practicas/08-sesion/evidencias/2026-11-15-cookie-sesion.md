# 2026-11-15 — Robo y reutilización de la cookie de sesión

- **Runbook o práctica:** [08 | Robo y reutilización de la cookie de sesión](../README.md)
- **Entorno:** equipo de trabajo, navegador Brave con el perfil de uso diario, app de laboratorio en `127.0.0.1:8011` con TTL de 30 s. Sin máquina virtual. El llavero del escritorio, desbloqueado.
- **Resultado:** sesión aceptada con la cookie extraída del perfil (200), muerta tras cerrar sesión (302) y rechazada por el servidor a los 32 s (302). El valor de la cookie no se imprime.
- **Limitación:** el bloqueo del disco cifrado no se probó con un arranque sin passphrase; se deduce del diseño de LUKS.

## Salida

```
$ python3 app.py --puerto 8011 --ttl 30

$ python3 extraer_cookie.py --sin-cookie
/privado sin cookie: 302 /login

$ python3 extraer_cookie.py --url http://127.0.0.1:8011 --logout
perfil: ~/.config/BraveSoftware/Brave-Browser/Default/Cookies
llavero: sí
host 127.0.0.1
cifrada: v10/v11
caducada: no
descifrado: sí — llavero:brave
sha256: 4c061245389b78f0
/privado: 200 http://127.0.0.1:8011/privado
/privado tras logout: 302 /login

$ python3 extraer_cookie.py --url http://127.0.0.1:8011   # 32 s después
caducada: sí — no se prueba
```

`caducada: sí` lo lee el script de la fecha de expiración guardada en el almacén; que el navegador deje de enviarla en ese plazo es la consecuencia esperada, no una medición aparte.

## Control de la caducidad en el servidor

Sesión de demostración iniciada por HTTP, sin tocar el perfil:

```
$ curl -s -o /dev/null -w 'login=%{http_code}\n' -c jar.txt -d 'u=demo&p=demo' http://127.0.0.1:8011/login
login=200
$ curl -s -o /dev/null -w 'privado_ahora=%{http_code}\n' -b jar.txt http://127.0.0.1:8011/privado
privado_ahora=200
$ sleep 32
$ curl -s -o /dev/null -w 'privado_tras_32s=%{http_code}\n' -b jar.txt http://127.0.0.1:8011/privado
privado_tras_32s=302
```

## Defensa del disco

```
$ lsblk -o NAME,FSTYPE,MOUNTPOINTS
nvme0n1p1 vfat        /boot/efi
nvme0n1p2 ext4        /boot
nvme0n1p3 crypto_LUKS
└─dm_crypt-0  LVM2_member
  └─ubuntu--vg-ubuntu--lv ext4 /
```

El volumen raíz está sobre LUKS. No se arrancó sin la passphrase: que sin ella no se monte es cómo funciona LUKS, no algo medido aquí.

## Notas

La clave del llavero de Brave es distinta de la de Chromium: el script tomaba la primera disponible y el descifrado fallaba aunque el llavero estuviera abierto. Ahora prueba todas las claves del llavero y admite el perfil de Brave.
