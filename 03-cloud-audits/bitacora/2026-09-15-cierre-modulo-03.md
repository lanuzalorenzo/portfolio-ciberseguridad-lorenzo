# Bitácora — 2026-09-15: Auditoría de Recursos Críticos e Identidades (Cierre Módulo 03)

**Módulo:** 03 — Auditorías Cloud  
**Prácticas:** 02 — Recursos Críticos & 03 — Identidades y Accesos

Jornada dedicada a completar las revisiones de recursos críticos y del directorio de identidades para cerrar formalmente el módulo de auditorías cloud.

En la primera mitad del día me centré en los recursos PaaS. El hallazgo más relevante apareció en una cuenta de almacenamiento: el parámetro `allowBlobPublicAccess` estaba habilitado. Aunque no hubiera contenedores públicos en ese momento, dejar la puerta abierta a nivel de cuenta es un riesgo inaceptable de fuga de datos accidental. Procedí a cambiarlo a `false` y verifiqué con curl que la API de blobs rechaza las peticiones anónimas con error 409. Además, detecté un servidor Azure SQL que permitía conexiones desde cualquier IP interna de Azure (`0.0.0.0`), recomendando el aislamiento mediante reglas específicas o Private Endpoints.

Por la tarde audité el directorio Microsoft Entra ID. Revisé el inventario de *App Registrations* y detecté un Service Principal con un *Client Secret* configurado sin fecha de caducidad (*Never expire*). Este tipo de secretos permanentes son vectores de persistencia silenciosa habituales tras filtraciones en repositorios. Recomendé su sustitución por una Managed Identity o, en su defecto, fijar expiración máxima a 180 días. También documenté el exceso de *Global Administrators* permanentes, abogando por el uso de PIM.

Con estos informes técnicos estructurados con matrices de hallazgos y planes de remediación, doy por finalizado el Módulo 03.
