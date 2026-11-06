# VM de pruebas: Kali importada y con el disco del perfil cifrado

> **Estado:** **Validado** en local el 2026-11-06 para importación, cifrado del disco del perfil, llavero y snapshot; **Pendiente** llevar el perfil del navegador al volumen cifrado, la prueba negativa del cierre y el fondo con la identidad visual. Evidencia: [2026-11-06-lab-vm-pruebas](evidencias/2026-11-06-lab-vm-pruebas/README.md).

Un banco de trabajo de carpintería no se monta en el salón: se monta en un cuarto donde se puede serrar, verter barniz y dejarlo todo hecho un desastre. Esta máquina virtual (VM) cumple ese papel para las prácticas que necesitan un navegador de verdad, un disco que se pueda cifrar y un llavero del sistema operativo. Si se rompe, se descarta y se vuelve a importar en minutos.

Se usa la imagen oficial de VirtualBox en lugar de la ISO porque evita el instalador y permite cifrar solo el volumen donde vivirá el perfil del navegador, que es el activo que se quiere medir. Cifrar todo el sistema también valdría, pero obliga a apagar la máquina para demostrar que el volumen está cerrado.

## Prerrequisitos

- VirtualBox 7.x, `7z`, `curl` y un gestor de contraseñas fuera de la VM.
- Unos 31 GB libres en el pico: 3,7 GB del archivo descargado, 17 GB de la imagen extraída y 10 GB del disco del perfil. Después de borrar el archivo quedan 27 GB.
- La passphrase (frase de paso que protege la clave del volumen cifrado) no se guarda en el llavero de la VM: el llavero es una de las defensas que se miden, y usarlo para custodiar la clave sería medir un atajo propio.

## 1. Descargar y verificar la imagen

```bash
mkdir -p ~/Descargas/kali && cd ~/Descargas/kali
f=$(curl -fsSL https://cdimage.kali.org/current/SHA256SUMS | grep -oE 'kali-linux-[0-9.]+-virtualbox-amd64\.7z' | head -1)
echo "$f"
curl -L# -o "$f" "https://cdimage.kali.org/current/$f"
curl -fsSL https://cdimage.kali.org/current/SHA256SUMS | grep " $f$" | sha256sum -c
```

El `-L` no es opcional: `cdimage.kali.org/current` responde con una redirección y, sin seguirlas, la lista de sumas llega vacía. La comprobación debe terminar en `OK` antes de seguir.

`current` apunta a la última versión publicada, que cambia con el tiempo. Los pasos siguientes derivan el nombre del archivo de `$f` para no fijar una versión que caduque.

## 2. Extraer y registrar

No se extrae en `/tmp`: en muchas distribuciones es un `tmpfs` en memoria y la extracción aborta con la cuota agotada. Se extrae en la carpeta de máquinas virtuales.

```bash
cd ~/Descargas/kali
VB="$HOME/Maquinas virtuales"
base="${f%.7z}"
7z x "$f" -o"$VB"
mv "$VB/$base" "$VB/kali-pruebas"

before=$(VBoxManage list vms | grep -oE '\{[^}]+\}' | sort)
VBoxManage registervm "$VB/kali-pruebas/$base.vbox"
new=$(comm -13 <(echo "$before") <(VBoxManage list vms | grep -oE '\{[^}]+\}' | sort) | tr -d '{}')
VBoxManage modifyvm "$new" --name "Kali pruebas"
VBoxManage list vms
```

El identificador único (UUID) se obtiene comparando la lista de antes y la de después. Usar `tail -1` es un atajo que renombra la última VM registrada, que puede ser otra. Renombrar después de registrar no mueve ficheros: la carpeta conserva su nombre.

## 3. Añadir el disco del perfil

```bash
VBoxManage createmedium disk --filename "$VB/kali-pruebas/perfil-cifrado.vdi" --size 10240
VBoxManage storageattach "Kali pruebas" --storagectl SATA --port 1 --device 0 \
  --type hdd --medium "$VB/kali-pruebas/perfil-cifrado.vdi"
```

Dentro de la VM:

```bash
passwd
lsblk
sudo cryptsetup luksFormat --verify-passphrase /dev/sdb
sudo cryptsetup open /dev/sdb perfil
sudo mkfs.ext4 /dev/mapper/perfil
sudo mkdir -p /home/kali/perfil
sudo mount /dev/mapper/perfil /home/kali/perfil
sudo chown kali:kali /home/kali/perfil
```

`luksFormat` pide confirmación con `YES` en mayúsculas; `--verify-passphrase` hace escribir la frase dos veces, porque un error en una sola pasada no se descubre hasta el primer `open`. Comprobar el dispositivo con `lsblk` antes: el cifrado destruye lo que haya en `/dev/sdb`.

La apertura y el montaje se repiten después de cada arranque:

```bash
sudo cryptsetup open /dev/sdb perfil
sudo mount /dev/mapper/perfil /home/kali/perfil
```

No se automatiza con `/etc/crypttab` y un fichero de clave: ese fichero viviría en el disco sin cifrar y anularía la defensa que se quiere medir.

## 4. Comprobar navegador y llavero

```bash
which firefox firefox-esr
ps -ef | grep -i keyring | grep -v grep
```

`ps` solo demuestra que el demonio está en marcha, no que guarde secretos. Para probarlo de verdad hace falta `secret-tool` (`libsecret-tools`): `secret-tool store` y `secret-tool lookup` deben devolver el secreto. Mientras no se instale, esta comprobación es **Parcial**.

## 5. Snapshot base

Con la VM apagada, para que la instantánea no arrastre la memoria:

```bash
VBoxManage snapshot "Kali pruebas" take "base" \
  --description "Imagen oficial; login cambiado; sdb LUKS montado en /home/kali/perfil"
```

Un `snapshot` (instantánea) guarda el estado del disco en ese momento; no es una copia de seguridad fuera del equipo y no cubre la pérdida del equipo.

## 6. Perfil sobre el volumen cifrado — Pendiente

Sin este paso, el navegador sigue escribiendo en `~/.mozilla`, que está en el disco sin cifrar, y el cifrado no protege lo que se quiere medir.

```bash
firefox --CreateProfile "perfil /home/kali/perfil/firefox"
firefox -P perfil
```

La comprobación es que `~/.mozilla` no crece al navegar y que el perfil aparece bajo `/home/kali/perfil`.

## Verificación

| Comprobación | Resultado esperado | Estado |
|---|---|---|
| `sha256sum -c` de la imagen | `OK` | Observado |
| `VBoxManage list vms` | la VM nueva registrada, sin tocar las demás | Observado |
| `lsblk -f` dentro de la VM | `sdb` con `crypto_LUKS`; `perfil` en `ext4` montado en `/home/kali/perfil` | Observado |
| `ps -ef \| grep keyring` | `gnome-keyring-daemon` con `secrets` | Observado; **Parcial** sin `secret-tool` |
| `VBoxManage snapshot "Kali pruebas" list` | `base` presente | Observado |
| Tras `sudo cryptsetup close perfil`, leer el montaje | el punto de montaje queda vacío y los datos no son legibles | Pendiente |
| Tras reiniciar | hay que abrir y montar a mano; `/home/kali/perfil` vacío antes de hacerlo | Pendiente |

## Límites y lo no ejecutado

- No es una máquina productiva: no hay copia fuera del equipo, ni monitorización, ni actualizaciones gestionadas. El snapshot sirve para volver atrás en un ensayo, no para recuperar un servicio.
- El disco del sistema no va cifrado; solo el volumen del perfil. Es una decisión, no un olvido.
- El perfil del navegador todavía no se ha movido al volumen cifrado.
- La prueba negativa del cierre y el comportamiento tras reiniciar están sin ejecutar.
- El fondo de escritorio y el icono de carpeta con la identidad visual quedan pendientes.

## Limpieza

```bash
VBoxManage unregistervm "Kali pruebas" --delete
rm -rf ~/Descargas/kali
```

Elimina la VM y sus discos. Las claves del gestor de contraseñas se borran a mano.
