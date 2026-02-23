Perfecto.
Te hago un **resumen ultra esquemático de Tema 50**, orientado 100% a examen tipo test.

---

# 📘 TEMA 50 — Plataforma de Gestión de Dispositivos (MDM / UEM)

---

## 🔹 1️⃣ Conceptos base

### MDM (Mobile Device Management)

* Gestión de dispositivos móviles.
* Configuración del sistema.
* Seguridad del dispositivo.
* Borrado remoto.

Centro: el dispositivo.

---

### MAM (Mobile Application Management)

* Gestión solo de aplicaciones corporativas.
* Protección de datos dentro de la app.
* No controla el dispositivo completo.

Centro: la aplicación.

---

### EMM (Enterprise Mobility Management)

* Evolución de MDM.
* Incluye MDM + MAM + gestión de contenidos.

Centro: movilidad empresarial.

---

### UEM (Unified Endpoint Management)

* Gestión unificada de todos los dispositivos:

  * Móviles
  * Portátiles
  * PCs
  * Tablets
  * IoT

Centro: todos los endpoints.

---

## 🔹 2️⃣ Solución Microsoft

### Microsoft Intune

* Es UEM.
* Gestión cloud.
* Integrado con identidad.
* Integrado con acceso condicional.

---

## 🔹 3️⃣ Conceptos clave que caen en examen

### Inscripción (Enrollment)

Proceso mediante el cual:

* El dispositivo queda registrado.
* Se vincula a la organización.
* Se le pueden aplicar políticas.

---

### Perfil de configuración

Define:

* Cómo debe estar configurado el dispositivo.
  Ej: PIN obligatorio, cifrado, bloqueo automático.

---

### Política de cumplimiento

Evalúa:

* Si el dispositivo cumple requisitos.
  Resultado:
* Conforme / No conforme.

---

### Dispositivo conforme

Cumple todas las condiciones:

* Versión mínima
* Cifrado
* No jailbreak
* Parche actualizado

---

## 🔹 4️⃣ Integración con identidad

Identidad + Estado del dispositivo = Decisión de acceso.

Si no es conforme:

* Puede bloquearse acceso a correo, SharePoint, etc.

---

## 🔹 5️⃣ Borrado remoto

### Borrado completo

* Elimina todo el dispositivo.
* Típico en dispositivos corporativos.

### Borrado selectivo

* Elimina solo datos corporativos.
* Típico en BYOD.

---

## 🔹 6️⃣ Arquitectura

### On-premise

* Servidor interno.
* Requiere red corporativa.

### Cloud

* Gestión desde la nube.
* No requiere VPN.

### Híbrido

* Combina ambos.
* Transición progresiva.

---

## 🔹 7️⃣ Escenarios típicos

### BYOD

* Gestión solo aplicaciones.
* Protección sin invadir privacidad.

### COBO (Corporate Owned Business Only)

* Gestión completa.
* Control total.

---

## 🔹 8️⃣ Importancia en Administración Pública

* Protección datos personales.
* Cumplimiento normativo.
* Esquema Nacional de Seguridad.
* Prevención fuga de información.

---

# 🎯 Estado final Tema 50

Tienes dominado:
✔ MDM vs MAM vs UEM
✔ Intune
✔ Cumplimiento
✔ Arquitectura
✔ BYOD
✔ Integración con identidad

Tema consolidado.

---

🚀 Pasamos al **Tema 51 — Endpoint Configuration Manager (ECM / SCCM)**.

Antes de empezar:

¿Quieres enfoque comparativo con Intune (muy habitual en examen)
o empezamos desde cero definiendo qué es y para qué sirve?
