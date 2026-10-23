# 02 | Línea temporal y consultas KQL

Durante un incidente, los eventos están repartidos entre identidad, actividad de recursos, aplicación y secretos. La línea temporal los pone en el mismo eje de tiempo para separar causa, impacto y alcance. Las siete consultas están escritas y revisadas; ninguna se ha ejecutado contra un workspace con datos.

**Referencias:** NIST SP 800-61 · MCSB IR-2

| Consulta | Qué responde |
|---|---|
| Fallos de inicio de sesión | Fuerza bruta, password spraying o errores de configuración |
| Éxito tras fallos | Credencial comprometida o acceso legítimo tras errores |
| Cambios de roles y aplicaciones | Elevación de privilegios o persistencia |
| Cambios de infraestructura | NSG, VNet, Key Vault y App Service modificados |
| Accesos a Key Vault | Lectura masiva o acceso anómalo a secretos |
| Errores 401/403 | Enumeración, fuerza bruta o fallos de autorización |
| `union` de fuentes | Línea temporal única para el informe y la custodia |

El código completo está en el [informe técnico](../../docs/informe-tecnico.md). La validación pendiente no es sintáctica: es comprobar que las tablas y campos existen en el workspace real, que el `join` no multiplica eventos y que el ruido es tolerable.

Sin ejecución no hay resultados que presentar, y una consulta que compila pero devuelve vacío no demuestra nada. La correlación necesita un identificador común —usuario, IP o recurso—, un rango temporal explícito y una hora normalizada a UTC. Tampoco se ha medido el coste de las consultas.
