# 01 | Conditional Access

> **Estado:** **Diseño**. Políticas descritas y justificadas; no configuradas ni probadas: el tenant no tiene licencia P1.
>
> **Referencias:** MCSB IA-2, IA-3 · CIS 1.1.

Security Defaults impone el segundo factor a todo el mundo y no admite excepciones. Es un buen suelo y un mal traje: no distingue a un administrador de un invitado, ni un portátil corporativo de una IP desconocida, ni una sesión de riesgo alto. Conditional Access sí. Cada política es una condición —quién entra, desde dónde, con qué dispositivo, con qué riesgo— y una decisión: pedir MFA, exigir un equipo conforme o bloquear.

## Qué se diseñó

| Política | Condición | Decisión |
|---|---|---|
| MFA para administradores | Cualquier rol privilegiado | MFA y sesión de una hora |
| Bloqueo de autenticación heredada | Protocolos sin MFA | Bloquear |
| Equipo conforme | Acceso a datos | Exigir dispositivo híbrido |
| Riesgo alto de sesión | IP anónima o viaje imposible | Bloquear y cambiar contraseña |

## Lo que falta para probarlo

Una licencia P1, usuarios de prueba y una cuenta de emergencia excluida de todas las políticas. Sin esa exclusión, un administrador que se bloquea a sí mismo se queda fuera del tenant y la recuperación es un ticket a soporte. También conviene activar cada política en modo *solo informe* unas horas antes de aplicarla.

## Lecciones

- Security Defaults y Conditional Access no conviven: activar el segundo exige apagar el primero.
- La cuenta de emergencia forma parte del diseño, no es un detalle de última hora.
- El modo *solo informe* enseña a quién habría bloqueado la política antes de bloquearlo de verdad.

## Más detalle

- [Módulo 06](../../README.md)
- [MFA con Security Defaults en el módulo 02](../../../02-identity-security/practicas/01-mfa/README.md)
