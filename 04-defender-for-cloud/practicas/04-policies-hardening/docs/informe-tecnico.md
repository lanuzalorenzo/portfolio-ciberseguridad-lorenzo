# Informe técnico — Políticas y hardening preventivo con Azure Policy

**Módulo:** 04 — Defender for Cloud
**Práctica:** 04 — Policies + Hardening

## Contexto y objetivo

Una suscripción sin directivas acepta cualquier recurso con la configuración que traiga por defecto: almacenamiento con acceso público, TLS antiguo, puertos de administración abiertos. El panel de recomendaciones lo detecta después; una directiva lo impide antes. Esta práctica documenta la asignación de la iniciativa Microsoft Cloud Security Benchmark como línea base y la aplicación de directivas en modo *Audit* y *Deny*.

## Componentes y decisiones

| Componente | Función | Configuración aplicada |
| :--- | :--- | :--- |
| Azure Policy | Motor declarativo de cumplimiento y gobernanza | Directivas individuales y agrupadas en iniciativas, asignadas a la suscripción |
| Iniciativa Microsoft Cloud Security Benchmark | Línea base de controles de referencia | Asignada desde *Security policy* de Defender for Cloud |
| Efecto *AuditIfNotExists* | Visibilidad sin bloqueo | Aplicado a la versión mínima de TLS y al registro de diagnóstico |
| Efecto *Deny* | Prevención activa | Aplicado al acceso público en cuentas de almacenamiento |

## Directivas aplicadas

| Control | Directiva | Efecto | Referencia |
| :--- | :--- | :--- | :--- |
| Línea base de cumplimiento | Iniciativa MCSB asignada en *Security policy* | Auditoría | MCSB GS-2 |
| Almacenamiento con acceso público | `allowBlobPublicAccess = true` | *Deny* | MCSB DP-4 / CIS 3.7 |
| Versión mínima de TLS | *AuditIfNotExists* sobre `minimumTlsVersion` | *Audit* | MCSB DP-3 |
| Recursos sin diagnóstico configurado | *AuditIfNotExists* sobre *Diagnostic Settings* | *Audit* | MCSB LT-1 |

## Verificación

| Prueba | Resultado observado |
| :--- | :--- |
| Iniciativa MCSB visible en *Security policy* | Listada como activa y evaluando los recursos de la suscripción |
| Creación de una cuenta de almacenamiento con acceso público | Azure Policy bloquea la operación antes de aprovisionar el recurso |
| Recursos sin TLS 1.2 | Marcados como *Non-compliant* para su remediación |

## Conclusiones técnicas

- La combinación de directivas en modo *Audit* con una iniciativa regulatoria da visibilidad de cumplimiento sin interrumpir lo que ya funciona.
- El modo *Deny* es la única prevención real: *Audit* deja constancia de la desviación, pero no la impide.
- El orden recomendable es auditar primero y pasar a *Deny* cuando se comprueba que la regla no rompe flujos legítimos.
