# 🧪 Guion — Práctica 01: Defender for Identity

## 🎯 Objetivo
Integrar Active Directory con Microsoft Defender for Identity mediante la instalación del sensor, la validación de telemetría, la revisión de detecciones iniciales y el análisis de las superficies de ataque relacionadas con identidades y credenciales.

---

## 🧩 Contexto técnico
Microsoft Defender for Identity es una solución de seguridad que analiza señales de Active Directory para detectar:
- Movimientos laterales.
- Técnicas de persistencia.
- Ataques basados en credenciales.
- Actividad anómala de cuentas privilegiadas.
- Reconocimiento interno previo a un ataque.

La práctica se centra en desplegar el sensor, validar su funcionamiento y observar cómo se generan las primeras señales de seguridad.

---

## 🛠 Preparación del entorno

### 🔹 1. Validación del controlador de dominio
Antes de instalar el sensor:
- Confirmar versión del sistema operativo compatible.
- Verificar que el DC tiene acceso a Internet (HTTPS).
- Validar que el servidor puede leer:
  - Security Event Log  
  - Directory Service Log  
  - Sysmon (si está presente)

### 🔹 2. Requisitos de permisos
El usuario debe disponer de:
- Permisos de instalación en el DC.
- Permisos para ejecutar el instalador del sensor.
- Permisos para acceder al portal de Defender for Identity.

---

## 📥 Descarga del sensor

### 🔹 3. Obtención del paquete
Desde el portal de Microsoft Defender for Identity:
- Acceder a **Configuration → Sensors**.
- Descargar el paquete de instalación.
- Copiarlo al controlador de dominio.

El paquete incluye:
- Instalador del servicio.
- Clave de acceso única para el tenant.
- Configuración predefinida del sensor.

---

## 🏗 Instalación del sensor

### 🔹 4. Ejecución del instalador
En el controlador de dominio:
- Ejecutar el instalador con privilegios elevados.
- Introducir la clave de acceso del portal.
- Validar que el servicio:
  - Se instala correctamente.
  - Se inicia sin errores.
  - Registra eventos en el visor de sucesos.

### 🔹 5. Validación del servicio
Comprobar:
- Estado del servicio: **Running**
- Conectividad con el servicio cloud.
- Lectura de logs del DC.
- Registro de telemetría en el portal.

---

## 📡 Validación de conectividad y telemetría

### 🔹 6. Estado del sensor en el portal
En Defender for Identity:
- El sensor debe aparecer como **Healthy**.
- Debe mostrar:
  - Última conexión.
  - Volumen de eventos procesados.
  - Estado de los componentes internos.

### 🔹 7. Confirmación de ingestión de señales
Validar que el portal recibe:
- Eventos de autenticación.
- Cambios de privilegios.
- Accesos a objetos sensibles.
- Actividad de cuentas privilegiadas.

---

## 🔍 Revisión inicial de alertas

### 🔹 8. Detecciones automáticas
Tras la instalación, el motor de análisis comienza a generar señales relacionadas con:
- Pass-the-Hash.
- Pass-the-Ticket.
- Kerberoasting.
- Reconocimiento de AD.
- Intentos de movimiento lateral.
- Uso anómalo de cuentas de servicio.

### 🔹 9. Análisis de alertas
Para cada alerta:
- Revisar el origen.
- Validar el tipo de técnica detectada.
- Comprobar el impacto potencial.
- Registrar observaciones relevantes.

---

## 🧠 Cierre de la práctica

### 🔹 10. Conclusiones técnicas
- Evaluar la calidad de las señales recibidas.
- Confirmar que el sensor está completamente operativo.
- Identificar mejoras futuras (Sysmon, auditorías avanzadas, hardening del DC).

### 🔹 11. Registro en bitácora
Documentar:
- Estado final del sensor.
- Validaciones realizadas.
- Alertas observadas.
- Próximos pasos para el módulo.

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en un entorno de laboratorio.
No contiene información sensible ni perteneciente a ninguna organización real.
Las configuraciones y ejemplos son demostraciones técnicas con fines educativos.
