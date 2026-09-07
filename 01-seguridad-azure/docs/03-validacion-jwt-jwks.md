# Validación de JWT y JWKS

Este documento explica cómo se valida un token JWT emitido por Azure AD.

## Estructura del JWT
- Cabecera: algoritmo y tipo de token.
- Payload: claims de identidad y autorización.
- Firma: garantiza integridad y autenticidad.

## Claims relevantes
- iss: emisor del token.
- aud: audiencia del token.
- exp: fecha de expiración.
- nbf: fecha de validez.
- oid / sub: identificadores del usuario.

## Firma RS256
Azure AD firma los tokens con claves privadas RSA.
La API valida la firma usando las claves públicas.

## JWKS
Azure AD publica las claves públicas en un endpoint estándar.
La API descarga estas claves y valida la firma del token.

## Rotación de claves
Azure AD rota las claves automáticamente.
La API siempre utiliza el JWKS actualizado.
