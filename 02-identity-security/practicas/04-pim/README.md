# 04 | Privileged Identity Management (PIM)

> **Estado:** **Validado** en laboratorio (evidencia documental). Tenant de prueba, sin datos reales.
>
> **Referencias:** MCSB PA-1, PA-2, PA-3, LT-1.

Si una cuenta administrativa tiene el privilegio todo el día, basta con robarla una vez. PIM lo convierte en una excepción: el rol está disponible pero inactivo, y se activa cuando hace falta, con un motivo, un límite de tiempo y un segundo factor.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Estado inicial | Inspección de asignaciones | Sin privilegios activos | PASS: solo *Eligible* |
| Activación sin justificación | Flujo *My Roles* | Bloqueo | PASS: exige justificación y MFA |
| Activación y expiración | Activación JIT y espera | *Active* temporal y vuelta a *Eligible* | PASS: evento registrado en auditoría |

## Lecciones

- Cuanto menos tiempo está activo un privilegio, menos vale una credencial robada.
- PIM necesita Access Reviews: una elegibilidad que nadie revisa sigue siendo una puerta abierta.
- Hacen falta cuentas de emergencia permanentes, fuera de PIM y monitorizadas, para no quedarse sin acceso.

## Más detalle

- [Configuración y validación](docs/informe-tecnico.md)
- [Bitácora del módulo](../../bitacora/2026-09-07-pim-entra-id.md)
