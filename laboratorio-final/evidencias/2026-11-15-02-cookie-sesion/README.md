# 2026-11-15 — 02 — Robo y reutilización de la cookie de sesión

- **Práctica:** [08 | Robo y reutilización de la cookie de sesión](../../../02-identity-security/practicas/08-sesion/README.md)
- **Comandos y salida:** [comandos.md](comandos.md)
- **Entorno:** equipo de trabajo, navegador Brave con el perfil de uso diario, app de laboratorio en `127.0.0.1:8011` con TTL de 30 s. Sin máquina virtual. Llavero del escritorio, desbloqueado.
- **Resultado:** la cookie extraída del perfil abre la zona privada (200), muere tras cerrar sesión (302) y el servidor la rechaza a los 32 s (302). El valor de la cookie no se imprime.
- **Limitación:** el bloqueo del disco cifrado no se probó con un arranque sin passphrase; se deduce del diseño de LUKS.

## Qué se hizo

Se inició sesión en el app con la cuenta de demostración desde el navegador de uso diario y se ejecutó el script de extracción contra el perfil real: lee el almacén de cookies, encuentra la de `sid`, la descifra con la clave del llavero y la prueba contra la zona privada sin imprimir su valor. Después se repitió la petición tras cerrar sesión y, con el app arrancado con TTL corto, pasados 32 s.

## Nota

La clave del llavero de Brave es distinta de la de Chromium: el script tomaba la primera disponible y el descifrado fallaba aunque el llavero estuviera abierto. Ahora prueba todas las claves del llavero y admite el perfil de Brave.
