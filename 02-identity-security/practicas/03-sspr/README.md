# 03 | Autoservicio de restablecimiento de contraseña (SSPR)

> **Estado:** **Validado** en laboratorio (evidencia documental). Tenant de prueba, sin datos reales.
>
> **Referencias:** MCSB IA-1 · NIST SP 800-63B · CIS Microsoft 365.

Cuando alguien olvida la contraseña o se queda fuera, la salida rápida es llamar a soporte. Ese teléfono es también un vector de ingeniería social: quien convence al técnico obtiene la cuenta. SSPR permite que la persona se recupere sola con los factores que ya registró.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso sin métodos registrados | Usuario sin factores dados de alta | El flujo se bloquea | PASS: no permite continuar |
| Registro de métodos | Alta de correo y móvil alternativos | Métodos validados por código | PASS: estado confirmado |
| Recuperación completa en `aka.ms/sspr` | Código, cambio de contraseña y login | Contraseña restablecida sin soporte | PASS: recuperación autónoma |

## Lecciones

- Registrar MFA y SSPR en la misma sesión reduce el trabajo del usuario y aumenta la cobertura.
- En entornos híbridos hace falta *Password Writeback* para que el cambio llegue a Active Directory.
- Los métodos caducan: si no se revisan, la recuperación falla justo cuando se necesita.

## Más detalle

- [Configuración y validación](informe.md)
- [Bitácora del módulo](../../bitacora/2026-09-08-identity-security.md)
