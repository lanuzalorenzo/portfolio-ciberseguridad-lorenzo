# Bitácora — 2026-09-02: Primera integración con Entra ID y Troubleshooting

> [!NOTE]
> El código al que se hace referencia está externalizado en `lab-api-local-azure`.

**Objetivo:** Configurar la API .NET para que exija un JWT válido emitido por nuestro tenant de Entra ID.

Hoy la sesión ha sido intensa. Empecé configurando el pipeline de .NET (`Program.cs`) para inyectar `UseAuthentication()` y configurar el esquema JWT Bearer. Añadí las credenciales base en `appsettings.json` (`TenantId`, `ClientId`, `Audience` y `Authority`).

Una vez protegidos los controladores con `[Authorize]`, tiré la primera petición y recibí un esperado 401 Unauthorized. Hasta ahí, perfecto. 

El problema vino al intentar probar el flujo de Authorization Code con Postman para obtener un token real. Me topé de frente con el **Error AADSTS501481**. Tras un rato depurando y revisando la documentación, me di cuenta de que el registro de aplicación en Azure no estaba configurado correctamente como "Public Client", por lo que me rechazaba el intento de usar PKCE sin un client secret. Lo arreglé cambiando el tipo de plataforma en el App Registration.

Poco después me saltó un **Error AADSTS90013**. El token no traía el scope adecuado. Resulta que estaba pidiendo la audiencia incorrecta porque no había concedido el Admin Consent al scope `access_as_user` en el portal. 

Tras corregir ambos bloqueos, la validación del JWT por fin pasó en la API local y logré acceder a los productos. Lección de hoy: el diablo está en los detalles de configuración del App Registration.
