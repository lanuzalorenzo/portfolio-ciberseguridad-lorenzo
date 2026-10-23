# 07 | Identidades administradas en Azure

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB IA-1, PA-1 · OWASP A10:2021.

Key Vault resuelve dónde guardar el secreto, pero la aplicación sigue necesitando uno para entrar. Una identidad administrada elimina ese último secreto: Azure reconoce al recurso por lo que es y le entrega un token temporal, sin contraseña que caduque ni que rotar.

## Validación

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Petición a IMDS sin cabecera `Metadata: true` | `curl` al endpoint de metadatos | Rechazo | PASS: 400, mitigación de SSRF |
| Token con cabecera de seguridad | `curl -H "Metadata: true"` | JWT firmado por Entra ID | PASS: token sin credenciales estáticas |
| Consumo de un secreto con ese token | Petición a Key Vault | Secreto devuelto según el rol | PASS: acceso concedido |

## Lecciones

- La cabecera obligatoria `Metadata: true` impide que una SSRF pida tokens desde dentro del recurso.
- Al destruir el recurso de cómputo, Azure elimina su identidad: no quedan permisos huérfanos.
- El rol asignado sigue siendo lo importante: sin mínimo privilegio, la identidad administrada solo cambia el problema de sitio.

## Más detalle

- [Configuración y validación](docs/managed-identities-documento-tecnico.md)
- [Bitácora del módulo](../../bitacora/2026-09-11-ejercicio-07-managed-identities.md)
