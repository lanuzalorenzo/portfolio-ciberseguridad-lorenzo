# Conceptos del Módulo 01

Este documento recoge los conceptos fundamentales utilizados en el módulo de Autenticación y Autorización en Azure.

## Autenticación vs Autorización
La autenticación verifica la identidad del usuario.
La autorización determina qué recursos puede acceder.

## OAuth2
Framework de autorización que permite a aplicaciones obtener acceso delegado a recursos protegidos.

## PKCE
Extensión de OAuth2 diseñada para clientes públicos.
Evita ataques de interceptación del authorization_code.

## JWT
Token firmado que contiene información de identidad y autorización.
Incluye cabecera, payload y firma.

## JWKS
Conjunto de claves públicas que Azure AD publica para validar firmas RS256.

## RS256
Algoritmo de firma asimétrica basado en RSA y SHA256.

## Azure AD / Entra ID
Proveedor de identidad que emite tokens seguros para aplicaciones y APIs.
