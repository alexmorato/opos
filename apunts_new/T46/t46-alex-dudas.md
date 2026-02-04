## **Tema 46: Arquitectura basada en serveis (SOA)**
1. **Orquestación de servicios en SOA**  
2. **API Gateway, API Manager, API Portal**  
3. **WS-Reliable Messaging**  
4. **WS-Security, WS-Addressing, WS-Coordination**  
5. **Idempotency Key**  
6. **UDDI** (Universal Description, Discovery, and Integration)  
7. **ESB en SOA** (Enterprise Service Bus)  
8. **EAI** (Enterprise Application Integration)  
9. **Loose Coupling** (principio en SOA)  
10. **BPEL** (lenguaje de orquestación)  
11. **SCA** (modelo de componentes)  
12. **UDDI** (registro de servicios)

---
## BPEL (Business Process Execution Language)

**BPEL** 🔄:  
Lenguaje estándar basado en XML para definir y orquestar procesos de negocio mediante la composición de servicios web.

### 📝 Frase clave de examen

> **BPEL se utiliza para orquestar servicios web en procesos de negocio, especialmente en arquitecturas SOA.**

---
## UDDI (Universal Description, Discovery, and Integration)

**UDDI** 📇:  
Estándar OASIS para registro y descubrimiento de servicios web SOAP que funciona como un "directorio público" o "páginas amarillas" de servicios empresariales.

**Componentes estructurales** 🏗️:  
Organiza la información en **páginas blancas** (datos del proveedor), **páginas amarillas** (clasificación por industria) y **páginas verdes** (detalles técnicos WSDL y endpoints).

### 📝 Frase clave de examen

> **UDDI fue el intento de crear un DNS universal para servicios web SOAP, que fracasó por complejidad y falta de adopción, siendo reemplazado por registros privados y API Portals.**
---
## WS-Security

**WS-Security** 🔐:  
Estándar OASIS que añade seguridad a nivel de mensaje SOAP mediante tokens de seguridad, firmas digitales y cifrado XML.

**Mecanismos clave** 🛡️:  
Proporciona **integridad** (XML-Signature), **confidencialidad** (XML-Encryption), **autenticación** (UsernameToken, SAML) y **autorización** en cabeceras SOAP.

### 📝 Frase clave de examen

> **WS-Security extiende SOAP para proporcionar seguridad de extremo a extremo a nivel de mensaje, independiente del transporte subyacente.**

---

## WS-Addressing

**WS-Addressing** 🎯:  
Estándar W3C que añade metadatos de direccionamiento a las cabeceras SOAP para habilitar mensajería asíncrona y enrutamiento complejo.

**Elementos principales** 📍:  
Define `wsa:To` (destino), `wsa:ReplyTo` (respuesta), `wsa:MessageID` (identificador único) y `wsa:Action` (operación a ejecutar).

### 📝 Frase clave de examen

> **WS-Addressing permite mensajería asíncrona y enrutamiento avanzado en SOAP desacoplando el direccionamiento lógico del transporte físico.**

---

## WS-Coordination

**WS-Coordination** 🤝:  
Estándar OASIS que proporciona un framework para coordinar transacciones distribuidas entre múltiples servicios web.

**Arquitectura coordinadora** 🔄:  
Define un **Coordination Service** central que gestiona contextos de transacción y protocolos como **WS-AtomicTransaction** (ACID distribuido) y **WS-BusinessActivity** (transacciones largas compensables).

### 📝 Frase clave de examen

> **WS-Coordination establece un servicio central para coordinar transacciones distribuidas entre servicios, soportando tanto transacciones atómicas como actividades de negocio de larga duración.**
---
## WS-Reliable Messaging

**WS-Reliable Messaging** 📨:  
Estándar OASIS que garantiza la entrega fiable de mensajes SOAP entre servicios, asegurando entrega exactamente una vez, en orden y sin pérdidas.

**Mecanismos de fiabilidad** ✅:  
Implementa **secuenciación**, **acuses de recibo (ACKs)**, **reenvíos automáticos** y **detección de duplicados** para tolerar fallos de red o sistemas.

### 📝 Frase clave de examen

> **WS-Reliable Messaging proporciona garantías de entrega para SOAP similar a TCP/IP pero a nivel de aplicación, esencial para transacciones críticas en entornos no fiables.**
---
## Idempotency Key

**Idempotency Key** 🔑:  
Identificador único enviado por el cliente para garantizar que una operación no se ejecute más de una vez, incluso si la petición se repite por reintentos o fallos de red.

### 📝 Frase clave de examen

> **La Idempotency Key permite reintentos seguros en APIs no idempotentes por diseño, evitando efectos secundarios no deseados mediante el almacenamiento de respuestas por clave única.**
---
## Loose Coupling

**Loose Coupling** 🧩:  
Principio de diseño donde los componentes de un sistema tienen dependencias mínimas entre sí, interactuando mediante interfaces estables sin conocer detalles internos de implementación.

### 📝 Frase clave de examen

> **Loose Coupling reduce el impacto de cambios locales en el sistema global, facilitando la evolución independiente de componentes mediante contratos bien definidos y comunicación mediada.**