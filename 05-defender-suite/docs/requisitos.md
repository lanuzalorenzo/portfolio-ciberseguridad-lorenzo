# Qué hace falta para validar el módulo 05

Las catorce prácticas de este módulo están en **Diseño**: describen qué se configuraría y qué se observaría, pero no conservan evidencia de ejecución. Esta tabla dice qué prueba cerraría cada una, qué licencia y qué recurso exige, y en qué punto está el laboratorio hoy.

Los precios no aparecen porque dependen del contrato y cambian. Lo que no cambia es la licencia y el recurso.

| # | Producto | Qué ve | Licencia mínima | Recurso que hay que montar | Prueba que lo valida | ¿Hoy? |
|---|---|---|---|---|---|---|
| 01 | Defender for Identity | Autenticación en Active Directory | Defender for Identity, incluido en Microsoft 365 E5 o contratado aparte | Un controlador de dominio de laboratorio con el sensor y una cuenta de servicio | Sensor en estado Healthy y una técnica conocida en el timeline | No: sin dominio |
| 02 | Defender for Endpoint | Procesos, red y archivos de un equipo | Defender for Endpoint P2 | Un equipo Windows o Linux y el paquete de onboarding | Dispositivo en el portal y una muestra de prueba detectada | No: sin licencia |
| 03 | Defender for Office 365 | Correo, enlaces y adjuntos | Defender for Office 365 P1 o P2 | Tenant con dos buzones y una política de enlaces y adjuntos | Enlace bloqueado y adjunto detonado con su alerta | No: sin tenant de correo |
| 04 | Defender XDR | La correlación de las señales anteriores | Incluido con los productos conectados | Al menos dos productos emitiendo señales | Un incidente con entidades de identidad y equipo en un solo caso | No: depende de 01–03 |
| 05 | Defender for APIs | Tráfico de APIs publicadas en API Management | Defender for APIs, plan de pago | Una instancia de API Management y la API importada | Enumeración de pedidos detectada y cuota con `429` | No: la API es local |
| 06 | Defender for Containers | Clúster, imágenes y auditoría de Kubernetes | Defender for Containers, plan de pago | Un clúster de AKS o compatible y un registro de imágenes | Imagen vulnerable marcada y pod anómalo detectado | No: sin clúster |
| 07 | Defender for Storage | Plano de datos de una cuenta de almacenamiento | Defender for Storage, plan de pago | Una cuenta de laboratorio con diagnóstico activo | Archivo EICAR en cuarentena y acceso anónimo bloqueado | No: sin cuenta con plan |
| 08 | Defender EASM | Lo que ya está publicado de ti en Internet | Defender EASM, facturado por activos | Un dominio propio verificable | Activos descubiertos y una exposición confirmada | No: sin dominio público propio |
| 09 | Defender Vulnerability Management | Inventario de software y vulnerabilidades | Incluido en Defender for Endpoint P2 | Un equipo con Endpoint y un paquete vulnerable instalado | El CVE aparece en el inventario con su remediación | No: depende de 02 |
| 10 | Defender App Governance | Permisos y comportamiento de aplicaciones OAuth | Defender for Cloud Apps con el complemento App Governance | Aplicaciones con permisos de Graph y actividad real | Una app con permiso excesivo marcada y su alerta | No: sin licencia |
| 11 | Defender for DevOps | Repositorios, pipelines, IaC y secretos | Conector gratuito; los hallazgos requieren Defender CSPM | Un repositorio de GitHub conectado con una plantilla de infraestructura | Un fallo en la plantilla detectado y enlazado a su commit | Parcial: el repositorio existe |
| 12 | Defender CSPM | Configuración del cloud y rutas de ataque | Defender CSPM, plan de pago | La suscripción de laboratorio con el plan activo | Un hallazgo con ruta de ataque y su recomendación | Parcial: la suscripción existe |
| 13 | Defender CNAPP | La vista conjunta de postura y cargas | No se contrata: resulta de CSPM y los planes de carga | Lo de 05, 06, 07, 11 y 12 al mismo tiempo | Un fallo seguido desde la plantilla hasta el runtime | No: depende de las demás |
| 14 | Simulación y XDR | La cadena completa de un ataque | Lo de 01–04 | Los cuatro productos activos y un escenario autorizado por escrito | Un incidente único con identidad, equipo, correo y nube | No: depende de todas |

## Tres niveles de coste

1. **Sin licencia nueva.** Las prácticas 11 y 12 se acercan con el plan gratuito de Defender for Cloud y el repositorio que ya existe. Lo que distingue a estos productos —rutas de ataque y hallazgos de IaC— exige el plan de pago.
2. **Con un plan de Defender for Cloud.** Las prácticas 05, 06 y 07 necesitan además API Management, un clúster y una cuenta de almacenamiento. Los planes se facturan por recurso y el laboratorio tendría que crear tres recursos nuevos.
3. **Con Microsoft 365 E5 o equivalente.** Las prácticas 01–04, 08–10, 13 y 14 dependen de una licencia que el laboratorio no tiene. Es el salto caro y decide si el módulo pasa de diseño a validación.

## Orden si se decide ejecutar

Primero lo barato y lo que alimenta al resto: **12 → 11 → 07 → 02 → 09 → 06 → 05 → 01 → 03 → 10 → 08 → 04 → 13 → 14**.

Cada práctica validada alimenta a la siguiente. Las tres últimas no se pueden adelantar: XDR necesita señales, CNAPP necesita cargas y la simulación necesita la suite entera.
