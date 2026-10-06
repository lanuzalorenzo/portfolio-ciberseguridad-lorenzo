# 01 | Conditional Access y MFA adaptativo

## Descripción del escenario y objetivo de seguridad

**Escenario:** Un entorno con usuarios que acceden desde diferentes ubicaciones, dispositivos y contextos, sin políticas adaptativas que restrinjan accesos sensibles o bloqueen ubicaciones no confiables.  
**Objetivo de seguridad:** Reforzar la autenticación mediante MFA adaptativo y requisitos de acceso basados en riesgo, dispositivo, localización y condiciones de contexto.  
**Alcance:** Microsoft Entra ID, políticas de acceso condicional, MFA, validación de sign-in sospechosos y control del acceso a aplicaciones y recursos.

> [!NOTE]
> Práctica realizada en un entorno de laboratorio. No incluir identificadores,
> secretos ni datos sensibles.

## Arquitectura y componentes de Microsoft Entra ID utilizados

| Componente | Función | Configuración relevante |
|---|---|---|
| **Microsoft Entra ID** | Plataforma de identidad y acceso | Gestión de sesiones, usuarios y acceso a recursos. |
| **Conditional Access** | Reglas de acceso dinámicas | Requiere MFA, confianza del dispositivo o acceso restringido. |
| **Multi-Factor Authentication** | Verificación adicional de identidad | Protección frente a credenciales robadas. |
| **Sign-in risk** | Evaluación del riesgo de sesión | Bloqueo o desafío en accesos sospechosos. |

## Implementación de controles DevSecOps / Seguridad

| Control | Implementación | Automatización o política | Referencia |
|---|---|---|---|
| MFA obligatorio | Requisito para accesos sensibles | Política de acceso condicional | MCSB IA-1 |
| Acceso basado en contexto | Restricción por ubicación, dispositivo y riesgo | Conditional Access | MCSB IA-2 |
| Detección de riesgo | Sign-in riesgo y sesion risk | Evaluación automática del acceso | MCSB IR-2 |
| Rechazo de acceso inseguro | Bloqueo de sesiones sospechosas | Política de protección | MCSB IA-3 |

**Artefactos relacionados:** [Informe técnico](docs/informe-tecnico.md).

## Validación o pruebas de seguridad realizadas

| Prueba | Método | Resultado esperado | Resultado observado |
|---|---|---|---|
| Acceso con MFA | Validación del flujo de autenticación | Requiere segundo factor | Sí |
| Acceso desde ubicación no confiable | Simulación del contexto | Acceso bloqueado o reforzado | Sí |
| Riesgo de sign-in | Revisión de sign-ins sospechosos | Condición de riesgo detectada | Sí |
