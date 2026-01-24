# **Tema 68. Certificados Digitales y Autenticación Electrónica - Resumen Ejecutivo** 📜🔐

## **1. 🎯 CONCEPTO BÁSICO**
Un **certificado digital** es un **documento electrónico** emitido por una **Autoridad de Certificación (AC)** que **vincula una clave pública** con una identidad (persona, empresa, servidor) y garantiza su autenticidad.

## **2. 🏛️ ELEMENTOS CLAVE (PKI - Public Key Infrastructure)**
- **📜 Certificado Digital:** Contiene: Identidad del titular, clave pública, datos de la AC, período de validez, uso (firma, autenticación).
- **🔑 Par de Claves:** **Pública** (se comparte) y **Privada** (secreta, nunca se comparte). Matemáticamente relacionadas.
- **🏢 Autoridad de Certificación (CA):** Entidad de confianza que **emite y firma** certificados (ej: FNMT, ACCV, GlobalSign).
- **📋 Autoridad de Registro (RA):** Verifica la identidad del solicitante ante la CA.
- **🗂️ Repositorio de Certificados (CRL/OCSP):** Donde se consulta la validez y revocación.

## **3. 📊 TIPOS DE CERTIFICADOS (Según titular)**
| Tipo | Para quién | Uso común |
|------|-----------|-----------|
| **Certificado de Persona Física** 👤 | Ciudadanos/empleados | Firma electrónica, autenticación, trámites (Hacienda, ayuntamiento) |
| **Certificado de Representante** 👔 | Personas que actúan por una entidad (ej: administrador) | Firmar en nombre de la organización |
| **Certificado de Persona Jurídica** 🏢 | Empresas, asociaciones, ayuntamientos | Sede electrónica, facturación electrónica |
| **Certificado de Servidor/Sitio Web** 🌐 | Servidores web (dominios) | HTTPS/SSL/TLS para webs seguras |
| **Certificado de Sello Electrónico** 🖇️ | Sistemas automáticos (no persona) | Sellado de facturas, documentos automatizados |

## **4. 🔄 CICLO DE VIDA DE UN CERTIFICADO**
1.  **Solicitud:** Generación de par de claves y CSR (Certificate Signing Request).
2.  **Verificación de Identidad:** La RA comprueba datos del solicitante.
3.  **Emisión:** La CA firma y emite el certificado.
4.  **Distribución:** Instalación en dispositivo/soporte seguro.
5.  **Uso:** Firma, autenticación, cifrado.
6.  **Revocación (si es necesario):** Por compromiso, pérdida o cambio de datos.
7.  **Renovación o Expiración:** Caducidad (normalmente 1-4 años).

## **5. ✅ AUTENTICACIÓN ELECTRÓNICA (eIDAS)**
- **¿Qué es?** Proceso de **verificar la identidad electrónica** de una persona/entidad.
- **Niveles de garantía (eIDAS):**
  - **Bajo:** Riesgo limitado (ej: contraseña simple).
  - **Substancial 🥈:** Requiere **2 factores** de categorías diferentes (posesión + conocimiento). **Equivalente a Firma Electrónica Avanzada**.
  - **Alto 🥇:** Requiere **DQSC** (Dispositivo Cualificado de Creación de Firma). **Equivalente a Firma Electrónica Cualificada**.

## **6. 🔐 MECANISMOS DE AUTENTICACIÓN**
- **🔑 Algo que SABES:** Contraseña, PIN.
- **📱 Algo que TIENES:** Certificado digital, token, móvil (app), tarjeta criptográfica.
- **👤 Algo que ERES:** Biometría (huella, facial).
- **📍 Algo que HACES/ESTÁS:** Patrón de comportamiento, ubicación.
- **➡️ Autenticación Multifactor (MFA):** Combinar ≥2 factores de DIFERENTES categorías.

## **7. 🏛️ ENTORNO ADMINISTRACIÓN PÚBLICA (Ayuntamiento Barcelona)**
- **📋 Certificados Reconocidos:** **FNMT**, **@firma**, **DNIe**, **IdCat Mòbil/IdCat Certificat**.
- **🌐 Sede Electrónica:** Autenticación con certificado para trámites.
- **⚖️ Cumplimiento Legal:** **Ley 39/2015** - derecho a relacionarse electrónicamente. **Ley 40/2015** - régimen jurídico sector público.
- **🔧 Infraestructura Propia:** Ayuntamiento puede ser **AC local** para empleados (pero debe cumplir eIDAS y ENS).
- **📞 Validación:** Sistemas deben verificar certificados (OCSP, CRL) y listas de confianza (TSL).

## **8. ⚠️ TRAMPAS Y CONFUSIONES TÍPICAS**
1.  **"Certificado = Usuario/Contraseña mejorado"** ❌  
    → **REALIDAD:** Es un **documento de identidad digital** con validez legal. Su compromiso es MUCHO más grave.

2.  **"La clave privada está en el certificado"** 🔑  
    → **TRAMPA:** **NO.** El certificado solo tiene la **clave pública**. La privada se guarda **separada y segura** (tarjeta, HSM).

3.  **"Certificado válido = Certificado de confianza"** ⚠️  
    → **REALIDAD:** Para ser de confianza, debe estar emitido por una **CA reconocida** en las TSL (Listas de Confianza) y **no revocado**.

4.  **"Autenticación con certificado = Firma electrónica"** ✍️  
    → **DIFERENCIA:** El mismo certificado puede servir para **ambas funciones**, pero son procesos distintos:  
    - **Autenticación:** "Eres quien dices ser" para **acceder**.  
    - **Firma:** "Aprobas este documento concreto" con **no repudio**.

5.  **"OCSP y CRL son lo mismo"** 🔄  
    → **OCSP:** Consulta **en tiempo real** de un certificado concreto.  
    → **CRL:** **Lista descargable** periódica con TODOS los revocados. Más lenta, puede no estar actualizada.

6.  **"DNIe ya no sirve, todo es Cl@ve"** 🆔  
    → **REALIDAD:** **DNIe sigue siendo válido** (certificado cualificado). Cl@ve es un **sistema de autenticación** (no firma) que puede usar certificado como uno de sus métodos.

7.  **"Renovar certificado = Prorrogar el mismo"** 📅  
    → **TRAMPA:** La **renovación genera un nuevo par de claves** y un nuevo certificado. No es una extensión del antiguo.

8.  **"Un certificado de servidor web (SSL/TLS) vale para firmar documentos"** 🌐  
    → **NO.** Los certificados tienen **usos definidos** (Key Usage). Uno de SSL no tiene permiso para firma.

9.  **"Backup del certificado = Backup de la clave privada"** 💾  
    → **PELIGRO:** Hacer backup de la clave privada **compromete su seguridad**. Debe hacerse solo en **HSM o soportes físicos muy seguros**.

10. **"La CA garantiza la identidad al 100%"** 🏢  
    → **LÍMITE:** La CA garantiza según el **proceso de verificación** usado (presencial, videoconferencia). Niveles de aseguramiento diferentes.

---

**📌 CLAVES PARA EL EXAMEN:**  
**PKI = CONFIANZA.**  
Certificado = **Identidad digital** con clave pública.  
Autenticación ≠ Firma (aunque usan misma tecnología).  
**Validar = Verificar firma CA + vigencia + no revocado + uso correcto.**  
En Administración: **eIDAS + ENS + TSL.**