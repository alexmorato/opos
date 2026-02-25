Perfecto.
Te lo estructuro igual que hiciste con Cloud: operativo, claro y enfocado a oposición TS TIC.

---

# **Tema 70. Protección del Acceso Remoto – Resumen Ejecutivo** 🌐🔐

---

## **1️⃣ 🎯 OBJETIVO DEL ACCESO REMOTO SEGURO**

Permitir acceso a sistemas corporativos desde redes no confiables **garantizando**:

* 🔐 Confidencialidad
* 🛡️ Integridad
* 👤 Autenticación fuerte
* 📊 Trazabilidad
* ⚖️ Cumplimiento ENS

---

## **2️⃣ 🌍 TIPOS DE ACCESO REMOTO**

### 🔹 VPN con cliente

* Software instalado.
* Túnel cifrado completo.
* Frecuente con IPsec o SSL VPN.

### 🔹 VPN sin cliente (Clientless)

* Acceso vía navegador.
* Basada en HTTPS/TLS.
* Actúa como reverse proxy seguro.

### 🔹 RDP (Remote Desktop Protocol)

* Acceso remoto a escritorio.
* ❌ Nunca exponer directamente a Internet.
* ✔ Siempre detrás de VPN + MFA + bastionado.

---

## **3️⃣ 🔐 TECNOLOGÍAS CLAVE**

* **IPsec:** Capa 3 (red). Típico en site-to-site.
* **TLS/SSL:** Capa superior. Típico en acceso remoto usuario.
* **SSH:** Acceso remoto seguro a sistemas Unix/Linux.
* **Jump Server / Bastion Host:** Punto intermedio controlado.
* **DMZ:** Zona intermedia para exponer servicios sin comprometer red interna.

---

## **4️⃣ 🛡️ CONTROLES DE SEGURIDAD IMPRESCINDIBLES**

### 🔸 Autenticación

* MFA obligatorio en accesos críticos.
* Especialmente en cuentas privilegiadas.
* Protección frente a credential stuffing.

### 🔸 Principio de mínimo privilegio

* Solo permisos estrictamente necesarios.
* Especialmente en accesos administrativos remotos.

### 🔸 Just-in-Time (JIT)

* Privilegios temporales.
* Evita cuentas admin permanentes.

### 🔸 Control de sesiones

* Timeout por inactividad.
* Reautenticación en acciones sensibles.

---

## **5️⃣ 🖥️ SEGURIDAD DEL ENDPOINT**

### 🔹 NAC (Network Access Control)

* Verifica cumplimiento de políticas antes de acceso.

### 🔹 Endpoint Security / EDR

* Antivirus avanzado.
* Monitorización comportamiento.

### 🔹 BYOD (Bring Your Own Device)

* Mayor riesgo.
* Mitigación con MDM.

### 🔹 MDM (Mobile Device Management)

* Control remoto.
* Borrado remoto.
* Aplicación de políticas.

### 🔹 VDI (Virtual Desktop Infrastructure)

* Datos permanecen en CPD.
* Reduce fuga de información.

---

## **6️⃣ 🌐 SEGMENTACIÓN Y ARQUITECTURA**

### 🔹 Segmentación de red

* Separación lógica o física.
* Reduce movimiento lateral.

### 🔹 Microsegmentación

* Aislamiento granular incluso dentro de la misma red.

### 🔹 Zero Trust

* No confiar por defecto.
* Verificación continua.
* Control basado en identidad, no en ubicación.

---

## **7️⃣ 📊 MONITORIZACIÓN Y DETECCIÓN**

### 🔹 Logging y trazabilidad

* Quién, qué, cuándo, desde dónde.
* Obligatorio en ENS medio/alto.

### 🔹 SIEM

* Correlación de eventos.
* Detección en tiempo real.
* Soporte a auditoría.

---

## **8️⃣ ⚖️ ENS Y ACCESO REMOTO**

En categoría **Media y Alta** exige:

* 🔐 Cifrado obligatorio.
* 👤 Autenticación reforzada.
* 📊 Registro de actividad.
* 🔍 Trazabilidad completa.
* 🛡️ Control reforzado en accesos privilegiados.

Medidas relacionadas:

* OP.ACC-5 (Acceso remoto)
* OP.ACC-7 (Autenticación reforzada)

---

## **9️⃣ 🚨 AMENAZAS PRINCIPALES**

* 🎭 Credential stuffing
* 🕵️ Sniffing
* 🧑‍💻 Man-in-the-Middle (MITM)
* 🔐 Robo de credenciales
* 🔄 Movimiento lateral
* 💥 RDP expuesto
* 🦠 Endpoint comprometido

---

## **🔟 ⚠️ FALSAS SEGURIDADES**

❌ Cambiar puerto RDP ≠ seguridad
❌ VPN ≠ endpoint seguro
❌ Cifrado ≠ inmunidad a DoS
❌ Estar dentro de la red ≠ estar autorizado

---

## **📌 PALABRAS CLAVE**

VPN | IPsec | TLS | Bastionado | Jump Server | DMZ | MFA | NAC | JIT | Segmentación | Zero Trust | ENS | SIEM | Trazabilidad

---

# 🎯 IDEA CLAVE PARA EXAMEN

> La VPN cifra el acceso, pero la seguridad real depende de autenticación fuerte, segmentación, mínimo privilegio y monitorización continua.

---

Si quieres, ahora puedo hacer:

* 🔥 Trampas típicas de examen del Tema 70
* 🧠 Mapa mental comparativo Tema 70 vs Tema 71
* 🎯 Simulacro combinado 70 + 71 nivel final oposición
