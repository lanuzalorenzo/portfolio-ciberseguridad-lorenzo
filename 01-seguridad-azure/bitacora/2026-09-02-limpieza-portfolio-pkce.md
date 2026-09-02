# Bitácora - Limpieza del Portfolio y registro del laboratorio PKCE - 02/09/2026

**Fecha**: 2026-09-02  
**Proyecto**: Portfolio Ciberseguridad - Lorenzo  
**Bloque**: 01-seguridad-azure / Mantenimiento del Portfolio  
**Estado**: ✅ COMPLETADO

---

## Objetivo del Bloque

Revisar el repositorio del portfolio, identificar artefactos creados accidentalmente durante un laboratorio de autenticación OAuth2 con PKCE y Azure AD, eliminarlos sin afectar proyectos reales o documentación oficial del portfolio, y dejar una referencia escrita en la bitácora del bloque para dejar constancia del trabajo realizado.

---

## Acciones Realizadas

### 1. Auditoría del repositorio
- **Acción**: Revisar el contenido del repositorio y compararlo con el README principal del portfolio.
- **Resultado**: Se detectaron archivos y carpetas ajenas al propósito del portfolio que pertenecían al laboratorio PKCE.
- **Estado**: ✅ Completado

### 2. Identificación de artefactos del laboratorio PKCE
Se localizaron y separaron los elementos no pertenecientes al portfolio original, entre ellos:

- `api-local/`
- `oauth2-pkce-lab/`
- `scripts` de PKCE
- archivos `server.js`, `package.json`, `validateToken.js`
- archivos `.sh`, `.env`, `.js`
- documentación del laboratorio (`docs/laboratorio-pkce-azure.md`)
- bitácora del laboratorio no integrada en la estructura real del portfolio

- **Estado**: ✅ Completado

### 3. Limpieza del repositorio
- **Acción**: Eliminar únicamente los archivos y carpetas creados para el laboratorio PKCE.
- **Verificación**: Se mantuvo intacto el README principal, las carpetas de proyectos reales, la documentación del portfolio y los scripts propios del repositorio.
- **Estado**: ✅ Completado

### 4. Registro en la bitácora del portfolio
- **Acción**: Añadir esta entrada en la bitácora del bloque para dejar constancia de que el laboratorio PKCE se realizó como prueba técnica y que se decidió moverlo fuera del portfolio para mantenerlo profesional y estructurado.
- **Resultado**: El repositorio queda limpio y alineado con la finalidad de portfolio profesional.
- **Estado**: ✅ Completado

---

## Decisión Arquitectónica

Se decidió que el laboratorio de autenticación OAuth2 con PKCE y Azure AD no debía permanecer dentro del portfolio principal porque:

- no forma parte de un proyecto real del portfolio,
- no está referenciado en el README principal,
- no aporta un caso de uso productivo del repositorio,
- y puede desviar la atención de la presentación profesional del portafolio.

Por ello, el laboratorio se considera una prueba experimental y se mantiene fuera del repositorio principal, con un seguimiento independiente y una documentación separada.

---

## Estructura Conservada

Los siguientes elementos se mantienen intactos:

- README principal del portfolio
- carpetas de proyectos reales
- documentación técnica del portfolio
- auditorías y bitácoras del bloque Azure
- pipelines y scripts reales del repositorio
- estructura general de la sección `01-seguridad-azure`

---

## Estado Final del Repositorio

### ✅ Mantenido
- [x] Portfolio profesional y ordenado
- [x] README principal intacto
- [x] Proyectos reales conservados
- [x] Bitácoras del portfolio correctamente documentadas
- [x] Scripts y documentación validos del portfolio

### ✅ Eliminado
- [x] Laboratorio PKCE
- [x] Scripts de prueba asociados al flujo OAuth2
- [x] API local experimental
- [x] Archivos `.js`, `.sh`, `.env` y `package.json` del laboratorio
- [x] Documentación ajena al portfolio

---

## Conclusión

La limpieza del repositorio ha dejado el portfolio en un estado más profesional, mantenible y consistente con la finalidad del proyecto. El laboratorio PKCE quedó registrado como una actividad experimental y no como parte de la presentación final del portfolio.

---

## Notas Finales

- El portfolio queda preparado para ser compartido como demostración técnica profesional.
- La documentación del laboratorio puede mantenerse en un repositorio independiente para continuidad del aprendizaje.
- La bitácora del portfolio refleja el criterio de limpieza y la decisión de separar pruebas experimentales de proyectos reales.
