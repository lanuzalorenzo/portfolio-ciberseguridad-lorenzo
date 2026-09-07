# 🛡️ Práctica — Protección de la rama main en GitHub

## 🧾 Contexto
La rama `main` es el punto de referencia del código en todos los repositorios del portfolio.  
Protegerla es un control DevSecOps esencial para garantizar integridad, trazabilidad y seguridad en el ciclo de vida del código.

---

## 🎯 Objetivo
Aplicar reglas de protección en GitHub para asegurar que la rama `main` evoluciona de forma controlada, evitando cambios no revisados, errores humanos y modificaciones accidentales.

---

## 🛠️ Trabajo realizado

### 1. Bloqueo de push directo
Se ha impedido que cualquier usuario pueda realizar un push directo a `main`.

### 2. Requerir Pull Request para todos los cambios
Todo cambio debe pasar por un Pull Request, garantizando revisión y trazabilidad.

### 3. Requerir al menos una aprobación
Se ha configurado la necesidad de una aprobación antes de fusionar cualquier PR.

### 4. Impedir borrar la rama main
La rama principal queda protegida contra eliminación accidental o malintencionada.

### 5. Impedir force‑push
Se ha bloqueado el uso de `git push --force` sobre la rama protegida.

### 6. Aplicación en todos los repositorios del portfolio
Las reglas se han replicado en todos los repositorios para mantener una política unificada.

---

## 🔍 Validaciones realizadas
- La rama `main` rechaza push directo.  
- Los PR requieren aprobación obligatoria.  
- El force‑push está bloqueado.  
- La rama no puede ser eliminada.  
- La configuración es consistente en todos los repositorios del portfolio.

---

## ⚠️ Problemas encontrados
- Algunos repositorios heredaban configuraciones antiguas.  
- La interfaz de GitHub oculta ciertas opciones avanzadas en menús secundarios.

---

## 🛠 Soluciones aplicadas
- Revisión manual de cada repositorio para garantizar coherencia.  
- Documentación de la ruta exacta en GitHub para localizar las reglas.  
- Unificación de la política DevSecOps en el módulo 4.

---

## 🔐 Implicaciones de seguridad
- Se evita la introducción accidental de fallos en producción.  
- Se garantiza trazabilidad completa de cada cambio.  
- Se refuerza la calidad del código mediante revisión obligatoria.  
- Se reduce el riesgo de modificaciones no autorizadas.  
- Se establece una política mínima de seguridad aplicable a cualquier entorno profesional.

---

## 📎 Recursos útiles
- GitHub Branch Protection Rules  
- Buenas prácticas DevSecOps  
- Documentación de Pull Requests

---

## ⚖️ Aviso Legal
Este documento describe prácticas realizadas en repositorios personales con fines educativos.  
No contiene información sensible ni perteneciente a ninguna organización real.  
Las configuraciones y ejemplos son demostraciones técnicas para formación en DevSecOps.

