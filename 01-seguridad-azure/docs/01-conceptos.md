# Conceptos — autenticación y autorización

**Proyecto:** Módulo 01 — OAuth 2.0, PKCE y validación de JWT.

No hace falta saber qué es un token para leer esto. El detalle técnico está en [02 — flujo OAuth 2.0 con PKCE](02-flujo-oauth2-pkce.md) y [03 — validación JWT y JWKS](03-validacion-jwt-jwks.md).

## Prestar la contraseña

Una aplicación quiere leer tus datos y esos datos están en otro servicio. Lo fácil sería darle tu contraseña, pero entonces podría hacer cualquier cosa y, si la pierde, la pierde para siempre.

OAuth 2.0 evita eso. La aplicación nunca ve la contraseña: el servicio que te conoce, Entra ID, comprueba quién eres y le entrega a la aplicación un pase temporal, limitado a una API y a unos permisos concretos.

## Quién es quién

| Personaje | Nombre técnico | Qué hace |
|---|---|---|
| Tú | *usuario* | Tienes los datos |
| La app | *cliente público* | Quiere acceso y no es de fiar al cien por cien |
| El conserje | Entra ID | Te autentica y reparte pases |
| El edificio | la API (`EcommerceApi`) | Tiene los datos y pide el pase |
| El pase | token | Permiso temporal con destinatario y caducidad |

## Autenticación y autorización no son lo mismo

La autenticación responde a quién eres, y la resuelve Entra ID cuando inicias sesión. La autorización responde a qué puedes hacer, y la comprueba la API con lo que lleva el pase dentro.

Entrar en el edificio no es abrir la sala de servidores. Puedes estar perfectamente identificado y no tener permiso para una operación concreta.

## Qué lleva el pase

Tres cosas explican casi todo su comportamiento. Caduca solo, normalmente en una hora. Vale para una API y unos permisos concretos, no para todo. Y va firmado, así que nadie puede fabricarlo ni modificarlo sin que la API lo note.

Por eso un pase robado es menos grave que una contraseña robada: sirve menos tiempo, para menos cosas, y su manipulación se detecta.

## Por qué PKCE

El pase no se entrega directamente. Primero hay un resguardo, el `authorization_code`, que viaja por la barra de direcciones y puede quedar en el historial o en un log. Si alguien lo copia y lo canjea, obtiene el pase.

PKCE hace que el resguardo no sirva solo. La aplicación se guarda un secreto, el `code_verifier`, y solo envía su huella, el `code_challenge`. Al canjear el resguardo presenta el secreto, y quien tenga el resguardo sin el secreto se queda sin pase. Es la taquilla del aeropuerto: el resguardo no basta, hay que enseñar además el DNI.

## Por qué JWT y JWKS

El pase es una tarjeta firmada. La API no llama a Entra ID en cada petición: se descarga las claves públicas que Entra publica y comprueba la firma con ellas. Como el portero que mira el holograma contra la lista de hologramas válidos.

La firma no basta. La API comprueba también que el pase es para ella (`aud`), que no ha caducado (`exp` y `nbf`) y que lo emitió el tenant correcto (`iss`). Sin esas comprobaciones, un pase emitido para otra aplicación serviría igual.

## Confusiones habituales

1. Un token no es una contraseña: caduca, vale solo para una API y no abre otros servicios.
2. PKCE no cifra el token. Impide que un resguardo interceptado se pueda canjear; el token viaja protegido por TLS, que es otra pieza.
3. Revocar una sesión no corta el acceso al instante. El access token ya emitido sigue válido hasta que caduca; lo que se invalida es el refresh token y la sesión de autenticación.

## Para seguir

- [02 — Flujo OAuth 2.0 con PKCE](02-flujo-oauth2-pkce.md): el paso a paso y los límites de PKCE.
- [03 — Validación JWT y JWKS](03-validacion-jwt-jwks.md): cómo comprueba la API el pase.
- [Práctica 01](../practicas/01-pkce-manual/README.md): hacerlo a mano.
- [Guía de lectura](../../docs/guia-de-lectura.md): glosario del resto del portfolio y orden recomendado.
