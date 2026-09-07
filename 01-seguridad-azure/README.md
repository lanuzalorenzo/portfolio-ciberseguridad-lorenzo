# 🔐 01 — Autenticación y Autorización en Azure (PKCE + OAuth2 + JWT)

Este módulo recoge el trabajo práctico relacionado con los flujos modernos de autenticación y autorización en Azure, centrado en **OAuth2**, **PKCE**, **Azure AD / Entra ID** y la **validación de tokens JWT** mediante una API local.  
Incluye las dos prácticas fundamentales que componen el flujo completo de autenticación:

- **Práctica PKCE (OAuth2 Authorization Code + PKCE)**  
- **Práctica de API local con validación de tokens JWT**

Ambas forman parte del mismo módulo porque representan un único flujo técnico:  
**autenticación → emisión de token → validación del token**.

---

## 🧭 Objetivos del módulo

- Comprender el flujo **OAuth2 Authorization Code**.  
- Implementar **PKCE** (code_verifier y code_challenge).  
- Utilizar **Azure AD / Entra ID** como proveedor de identidad.  
- Obtener un **authorization_code** y canjearlo por un **token de acceso**.  
- Validar un **token JWT** en una API local.  
- Interpretar **claims**, **firma**, **cabeceras** y **claves públicas (JWKS)**.  
- Documentar el proceso mediante bitácoras y explicaciones técnicas.

---

## 🧩 Práctica 1: PKCE + OAuth2

Esta práctica implementa el flujo completo de autenticación:

- Construcción de la URL de autorización.  
- Generación de `code_verifier` y `code_challenge`.  
- Obtención del `authorization_code`.  
- Intercambio del código por un token de acceso.  
- Análisis del token JWT emitido por Azure AD.  
- Revisión de claims, cabeceras y firma.  

La bitácora del laboratorio se encuentra en este módulo.

---

## 🧩 Práctica 2: API Local con Validación JWT

La segunda práctica consiste en una API local que permite:

- Validar tokens JWT emitidos por Azure AD.  
- Verificar la firma mediante JWKS.  
- Comprobar la estructura del token y sus claims.  
- Entender cómo una aplicación real valida tokens de identidad.

Repositorio de la API local:  
**https://github.com/lanuzalorenzo/lab-api-local-azure**

---

## 📘 Documentación técnica

El módulo incluye documentación que explica:

- El flujo OAuth2 + PKCE paso a paso.  
- La interacción con Azure AD / Entra ID.  
- La estructura interna de un token JWT.  
- La validación de firma mediante JWKS.  
- Riesgos y buenas prácticas del flujo.  

---

## ⚖️ Aviso Legal

Este módulo contiene prácticas educativas y de laboratorio.  
No incluye información sensible ni perteneciente a ninguna empresa.  
Las configuraciones y ejemplos son demostraciones técnicas en entorno controlado.

---

## 🔐 Licencia

Este módulo se distribuye bajo licencia **MIT**.  
Consulta el archivo `LICENSE` en la raíz del repositorio para más información.
