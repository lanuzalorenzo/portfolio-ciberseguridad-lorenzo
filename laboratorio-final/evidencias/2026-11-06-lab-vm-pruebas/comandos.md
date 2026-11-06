# Comandos ejecutados — VM de pruebas

Salida redactada. Sin rutas con nombre de usuario, sin UUID reales y sin frases de paso.

## Descarga y verificación

```bash
f=$(curl -fsSL https://cdimage.kali.org/current/SHA256SUMS \
  | grep -oE 'kali-linux-[0-9.]+-virtualbox-amd64\.7z' | head -1)
curl -L# -o "$f" "https://cdimage.kali.org/current/$f"
curl -fsSL https://cdimage.kali.org/current/SHA256SUMS | grep " $f$" | sha256sum -c
```

**Salida observada:**

```text
kali-linux-2026.3-virtualbox-amd64.7z: OK
```

## Extracción y registro

```bash
VB="$HOME/Maquinas virtuales"
base="${f%.7z}"
7z x "$f" -o"$VB"
mv "$VB/$base" "$VB/kali-pruebas"

before=$(VBoxManage list vms | grep -oE '\{[^}]+\}' | sort)
VBoxManage registervm "$VB/kali-pruebas/$base.vbox"
new=$(comm -13 <(echo "$before") <(VBoxManage list vms | grep -oE '\{[^}]+\}' | sort) | tr -d '{}')
VBoxManage modifyvm "$new" --name "Kali pruebas"
```

**Salida observada:** tres máquinas registradas al terminar; las dos anteriores con su nombre de antes. El nombre de la nueva queda como `Kali pruebas`.

## Disco del perfil

```bash
VBoxManage createmedium disk --filename "$VB/kali-pruebas/perfil-cifrado.vdi" --size 10240
VBoxManage storageattach "Kali pruebas" --storagectl SATA --port 1 --device 0 \
  --type hdd --medium "$VB/kali-pruebas/perfil-cifrado.vdi"
```

Dentro del invitado:

```bash
sudo cryptsetup luksFormat --batch-mode /dev/sdb
sudo cryptsetup open /dev/sdb perfil
sudo mkfs.ext4 /dev/mapper/perfil
sudo mkdir -p /home/kali/perfil
sudo mount /dev/mapper/perfil /home/kali/perfil
sudo chown kali:kali /home/kali/perfil
lsblk -f
```

**Salida observada (redactada):**

```text
NAME   FSTYPE FSVER LABEL UUID FSAVAIL FSUSE% MOUNTPOINTS
sda
└─sda1 ext4   1.0   root  <uuid>  58,2G  21% /
sdb    crypto 2           <uuid>
└─perfil
       ext4   1.0          <uuid>   9,2G   0% /home/kali/perfil
sr0
```

## Navegador y llavero

```bash
which firefox firefox-esr
ps -ef | grep -i keyring | grep -v grep
```

**Salida observada (redactada):**

```text
/usr/bin/firefox
/usr/bin/firefox-esr
kali  914  888  0 08:18 ?  00:00:00 /usr/bin/gnome-keyring-daemon --foreground --components=pkcs11,secrets --control-directory=/run/user/1000/keyring
```

## Snapshot

```bash
VBoxManage snapshot "Kali pruebas" take "base" \
  --description "Imagen oficial; login cambiado; sdb LUKS montado en /home/kali/perfil"
VBoxManage snapshot "Kali pruebas" list
```

**Salida observada:**

```text
   Name: base (UUID: <uuid>) *
   Description: Imagen oficial; login cambiado; sdb LUKS montado en /home/kali/perfil
```
