### 🛡️ Módulo 01 — Seguridad en Azure (PKCE + OAuth2 + JWT)

#### 📘 Descripción
Laboratorio práctico que implementa un flujo de autenticación moderno con Entra ID (Azure AD). Incluye Authorization Code Flow con PKCE, emisión de JWT firmados con RS256 y validación dinámica de claves mediante JWKS. Diseñado para demostrar capacidad de diseño, implementación y auditoría de flujos de identidad seguros en entornos cloud.

#### 🎯 Objetivos
- Implementar Authorization Code Flow con PKCE integrado en Entra ID.  
- Emitir y validar JWTs firmados con RS256 usando JWKS dinámico.  
- Diseñar una API que exija y verifique tokens en endpoints protegidos.  
- Documentar decisiones de diseño, validaciones y mitigaciones de riesgo.

#### 📚 Contenido técnico
- **Flujo de autenticación**: Authorization Code + PKCE.  
- **Proveedor de identidad**: Entra ID (registro de aplicación, scopes, redirect URIs).  
- **Tokens**: emisión y estructura de JWT; verificación de `iss`, `aud`, `exp`, `nbf`, `iat`, `scp`.  
- **Validación de firma**: verificación RS256 contra JWKS; manejo de rotación de claves.  
- **API protegida**: middleware que valida token, scopes y claims relevantes.  
- **Pruebas técnicas**: validación de tokens expirados, firma inválida y scopes insuficientes.  
- **Operativa**: cache seguro de JWKS, control de errores y logging mínimo para auditoría.

#### 🔧 Cómo se hizo
1. **Registro en Entra ID**: aplicación con `client_id`, redirect URI y scopes mínimos.  
2. **Cliente PKCE**: generación de `code_verifier` y `code_challenge` en el cliente; uso de `S256`.  
3. **Intercambio seguro**: el backend realiza el intercambio del código por token; `client_secret` no expuesto en cliente público.  
4. **Validación en API**: comprobación de `iss`, `aud`, `exp`, `nbf`, `iat`; verificación de firma RS256 usando JWKS obtenido desde el `/.well-known/jwks.json` del tenant.  
5. **Gestión de JWKS**: recuperación periódica y cache con TTL; fallback ante rotación de claves.  
6. **Mitigaciones operativas**: validación de `state`/`nonce`, uso de HTTPS, limitación de scopes y logging de intentos fallidos para detección.

#### ⚠️ Riesgos mitigados
- **Replay attacks**: uso de `state` y `nonce` en el flujo.  
- **Token theft**: intercambio de código en backend; no exponer `client_secret`.  
- **Clave rotada**: cache de JWKS con reintento y refresco.  
- **Validación incompleta**: verificación estricta de `iss`, `aud`, `alg` y claims críticos.  
- **Scopes excesivos**: principio de mínimo privilegio en scopes y roles.

#### ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio. No contiene información sensible ni perteneciente a ninguna organización real. Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.

#### 🔐 Licencia
Distribuido bajo licencia MIT. Consulta el archivo LICENSE en la raíz del repositorio para más información.
