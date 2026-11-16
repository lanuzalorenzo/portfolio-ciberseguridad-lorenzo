# Comandos y salida — 2026-11-15 · 02 · cookie de sesión

Equipo de trabajo, app de laboratorio en `127.0.0.1:8011` con TTL de 30 s, llavero desbloqueado. El valor de la cookie no se imprime en ninguna salida.

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

`caducada: sí` lo lee el script de la fecha de expiración guardada en el almacén. La app fija esa fecha y el `Max-Age` al mismo TTL, así que coincidir es una consecuencia del código; lo medido es el rechazo del servidor.

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

Comprobado el 16/11, con el equipo ya arrancado:

```
$ lsblk -o NAME,FSTYPE,MOUNTPOINTS
nvme0n1p1 vfat        /boot/efi
nvme0n1p2 ext4        /boot
nvme0n1p3 crypto_LUKS
└─dm_crypt-0  LVM2_member
  └─ubuntu--vg-ubuntu--lv ext4 /
```

El volumen raíz está sobre LUKS: la partición es `crypto_LUKS`, el volumen LVM vive dentro y la raíz ext4 cuelga de él. Que sin desbloquear el contenedor no se cree el volumen que la contiene es la consecuencia esperada de esa pila, no una prueba de arranque; el arranque sin la passphrase no se probó.
