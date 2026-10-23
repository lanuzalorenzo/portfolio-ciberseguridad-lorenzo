# 02 | Auditoría de recursos críticos

> **Estado:** **Validado** en laboratorio (evidencia documental).
>
> **Referencias:** MCSB DP-2, DP-3, DP-4, NS-1 · CIS Azure 3.7 · NIST SP 800-52.

Almacenamiento, bases de datos y almacenes de secretos son donde vive lo que hay que proteger. Sus valores por defecto priman la rapidez de despliegue, y casi todos dejan una puerta abierta hasta que alguien la cierra.

## Hallazgos

| ID | Qué se comprobó | Cómo | Resultado observado | Gravedad |
|---|---|---|---|---|
| SEC-RES-01 | Acceso anónimo a blobs | Petición HTTP anónima al contenedor | Estaba habilitado; se desactivó y la petición pasó a devolver `409` | Crítica |
| SEC-RES-02 | Versión mínima de TLS | Negociación con TLS 1.0 y 1.1 | Estaba en TLS 1.0; se fijó en 1.2 y el *handshake* antiguo se rechaza | Alta |
| SEC-RES-03 | Cortafuegos de Azure SQL | Inspección de reglas del servidor | Regla abierta a «todos los servicios de Azure» | Alta |
| SEC-RES-04 | Protección contra borrado | Configuración de Key Vault | Sin *Purge Protection*: un borrado podía ser definitivo | Media |

Se corrigieron y verificaron los dos primeros. Los otros dos quedaron recomendados: reglas de firewall por IP o *Private Endpoints*, y activar *Purge Protection* con retención de 90 días.

## Lecciones

- Dejar el parámetro seguro a nivel de cuenta no basta si el operador puede volver a abrirlo: hace falta una política que lo impida.
- TLS 1.0 sigue siendo el valor por defecto de muchos recursos creados sin plantilla endurecida.
- «Permitir servicios de Azure» no distingue tus recursos de los de cualquier otro tenant.
- *Soft Delete* sin *Purge Protection* protege del error, no del ataque.

## Más detalle

- [Informe técnico con la matriz completa](docs/auditoria-recursos-criticos-documento-tecnico.md)
- [Bitácora del 15 de septiembre](../../bitacora/2026-09-15-cierre-modulo-03.md)
