# Evidencia — Laboratorio local / VM de pruebas con disco cifrado

> **Identificador:** `2026-11-06-lab-vm-pruebas`
>
> **Tipo:** ejecución (ruta A)
>
> **Resultado:** PASS
>
> **Runbook:** [VM de pruebas](../../vm-de-pruebas.md)

## 1. Contexto

- **Fecha:** 2026-11-06
- **Responsable:** autor del repositorio
- **Entorno:** Ubuntu con VirtualBox 7.2.6; invitado Kali 2026.3 desde la imagen oficial de VirtualBox.
- **Alcance:** importar la imagen, añadir y cifrar el disco del perfil, comprobar navegador y llavero, y tomar un snapshot base.
- **Datos:** sintéticos; no se usan credenciales reales.
- **Autorización:** no aplica. Todo local, sin recursos cloud ni red externa.

## 2. Comandos ejecutados

En [`comandos.md`](comandos.md), con la salida redactada: sumas de la imagen, registro de la VM, `lsblk -f` con el volumen abierto, demonio del llavero y snapshot.

## 3. Validación

| Prueba | Resultado esperado | Resultado observado | Veredicto |
|---|---|---|---|
| Verificar la imagen descargada | `sha256sum -c` termina en `OK` | `OK` para el archivo de VirtualBox 2026.3 | PASS |
| Registrar sin tocar las VM existentes | la lista crece en una y las demás siguen | una VM nueva; las dos anteriores intactas | PASS |
| Cifrar el segundo disco | `sdb` con tipo `crypto_LUKS` | `sdb crypto_LUKS` con `perfil` en `ext4` | PASS |
| Montar el volumen | `ext4` montado en `/home/kali/perfil` | montado, 9,2 GB disponibles | PASS |
| Navegador instalado | binario de Firefox presente | `/usr/bin/firefox` y `/usr/bin/firefox-esr` | PASS |
| Llavero operativo | demonio con componente `secrets` | `gnome-keyring-daemon` con `pkcs11,secrets` | Parcial |
| Snapshot base | `base` en la lista, VM apagada | `base` presente, VM apagada | PASS |

El llavero se declara **Parcial** porque la comprobación con `ps` demuestra que el demonio arrancó, no que custodie un secreto. Esa prueba queda para la ejecución de la práctica que lo use.

## 4. Conclusiones

- La imagen oficial se importa sin instalador y deja un invitado utilizable en minutos.
- El cifrado de un volumen aparte permite montar y desmontar el perfil sin apagar la máquina.
- El snapshot base permite volver al punto de partida con el login ya cambiado.

## 5. Limitaciones

- El perfil del navegador no se movió al volumen cifrado en esta ejecución.
- No se ejecutó la prueba negativa (volumen cerrado y datos ilegibles) ni la comprobación tras reiniciar.
- El disco del sistema no está cifrado.
- No es una máquina productiva: sin copia fuera del equipo, sin monitorización y sin actualizaciones gestionadas.

## 6. Coste y tiempo

- Coste: cero. Todo local.
- Tiempo: unos 40 minutos, con la descarga incluida.

## 7. Limpieza

```bash
VBoxManage unregistervm "Kali pruebas" --delete
rm -rf ~/Descargas/kali
```
