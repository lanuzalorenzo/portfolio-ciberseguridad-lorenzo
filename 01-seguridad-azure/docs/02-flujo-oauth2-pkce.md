# Flujo OAuth2 Authorization Code + PKCE

Este documento describe el flujo de autenticación utilizado en el módulo.

## 1. Code Verifier
Cadena aleatoria generada por el cliente.
Se mantiene en secreto y se usa en el intercambio final.

## 2. Code Challenge
Derivado del code_verifier mediante SHA256.
Se envía en la solicitud de autorización.

## 3. Authorization Request
El cliente inicia el flujo solicitando un authorization_code a Azure AD.

## 4. Autenticación del usuario
Azure AD verifica la identidad del usuario mediante el método configurado.

## 5. Authorization Code
Azure AD devuelve un código temporal al cliente.

## 6. Token Exchange
El cliente intercambia el authorization_code por un token de acceso.
Aquí se utiliza el code_verifier para validar la integridad del flujo.

## 7. Token de acceso
Azure AD emite un JWT firmado con RS256.

## 8. Validación en la API
La API valida el token usando JWKS y comprueba claims, issuer y audiencia.
