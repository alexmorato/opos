# **🚫 Versiones de TLS que NO se deben usar**

## **📌 TLS PROHIBIDOS / INSECUROS**
| Versión | Estado | Razón Principal | Fecha Obsolescencia |
|---------|--------|----------------|---------------------|
| **SSL 1.0** | ❌ PROHIBIDO | Vulnerabilidades graves, nunca seguro | 1996 (desaparecido) |
| **SSL 2.0** | ❌ PROHIBIDO | Débil, vulnerabilidades conocidas | 2011 (RFC 6176) |
| **SSL 3.0** | ❌ PROHIBIDO | Vulnerable a POODLE attack | 2015 (RFC 7568) |
| **TLS 1.0** | ❌ **NO USAR** | Vulnerable a BEAST, RC4 inseguro | 2020 (PCI DSS 3.2.1) |
| **TLS 1.1** | ❌ **NO USAR** | No tiene mejoras críticas, vulnerable | 2020 (junto con TLS 1.0) |

## **⚠️ TLS 1.0 y 1.1 - PROHIBICIÓN TOTAL**
- **PCI DSS 3.2.1 (2020):** Prohibido para transacciones de pago.
- **NIST SP 800-52 Rev. 2:** No usar en sistemas federales USA.
- **ENS (Esquema Nacional de Seguridad):** **Rechazados explícitamente**.
- **BANCO DE ESPAÑA:** Prohibido para entidades financieras.
- **Motivos:** Vulnerabilidades como **BEAST**, **CRIME**, **RC4 inseguro**.

## **✅ TLS PERMITIDOS / SEGUROS**
| Versión | Estado | Recomendación |
|---------|--------|--------------|
| **TLS 1.2** | ✅ **MÍNIMO ACEPTABLE** | Configuración segura (cifrados fuertes) |
| **TLS 1.3** | ✅ **RECOMENDADO** | Más rápido, más seguro (sin negociación) |

## **🔧 Configuración SEGURA de TLS 1.2 (si es necesario)**
- **Cifrados FUERTES:**
  - **AES-GCM** (128/256 bits) 
  - **ECDHE** para intercambio de claves
  - **SHA-256/SHA-384** para autenticación
- **Evitar:**
  - ❌ RC4 (totalmente roto)
  - ❌ CBC mode vulnerable
  - ❌ MD5, SHA-1 (hash débiles)
  - ❌ RSA key exchange (sin Forward Secrecy)

## **🏛️ CONTEXTO ADMINISTRACIÓN PÚBLICA (Ayuntamiento)**
- **ENS Nivel ALTO:** **TLS 1.2 mínimo**, preferible TLS 1.3.
- **Catálogo de STIC (CCN):** Solo cifrados aprobados.
- **Servicios Públicos:** **Deben deshabilitar TLS 1.0/1.1**.
- **Monitorización:** Detectar intentos de uso inseguro.

## **📋 CHECKLIST de IMPLEMENTACIÓN**
1. ❌ **Deshabilitar** TLS 1.0 y TLS 1.1 en TODOS servidores.
2. ✅ **Habilitar** TLS 1.2 (configuración segura) y TLS 1.3.
3. 🔧 **Configurar cifrados fuertes** (ECDHE, AES-GCM).
4. 📜 **Usar certificados válidos** (SHA-256/RSA 2048+ o ECC).
5. 🔄 **Actualizar librerías** (OpenSSL, Schannel, etc.).
6. 🧪 **Testear** con herramientas (SSL Labs, nmap).

## **🎯 PARA EL EXAMEN - REGLA MNEMOTÉCNICA**
> **"TODO lo anterior a TLS 1.2 está MUERTO"**
> - SSL (todos) → ❌ PROHIBIDO
> - TLS 1.0 y 1.1 → ❌ NO USAR
> - TLS 1.2 → ✅ MÍNIMO ACEPTABLE  
> - TLS 1.3 → ✅ IDEAL

---

**⚠️ RECUERDA:** En el **Ayuntamiento de Barcelona**, según **ENS nivel alto**, la **configuración segura de TLS es obligatoria** y se audita periódicamente.