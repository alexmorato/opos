## **Tema 44: Disseny d'una Arquitectura de Microserveis**
1. **ACID vs SAGA**  
2. **SAGA** (ejemplo funcional, si es acrónimo)  
3. **Service Façade**  
4. **Fallback** (patrón de resiliencia)  
5. **DLQ** (Dead Letter Queue)  
6. **Bulkhead Pattern**  
7. **Client Side Discovery** vs Service Discovery  
8. **Canonical Data Model (CDM)**  
9. **CDM vs DDD** (Domain-Driven Design)  
10. **Loose Coupling**  
11. **CQRS** (Command Query Responsibility Segregation)  
12. **Tracing distribuido** → Span y Trace Context  
13. **BPEL** (Business Process Execution Language)  
14. **SCA** (Service Component Architecture) en SOA  
15. **AMQP** (Advanced Message Queuing Protocol)

---

## Service Discovery vs Client-Side Discovery

**Service Discovery (concepto general)** 🧭:  
Mecanismo que permite localizar dinámicamente servicios disponibles en una arquitectura distribuida sin usar direcciones fijas.

**Client-Side Discovery** 🧩:  
Modelo de service discovery en el que el cliente consulta un registro de servicios y decide a qué instancia conectarse.

### 📝 Frase clave de examen

> **En client-side discovery el cliente localiza y selecciona directamente la instancia del servicio.**

---

## Contexto arquitectónico: Service Discovery

**Microservicios** 🧩:  
El *service discovery* (especialmente **client-side discovery**) es fundamental debido a la naturaleza dinámica, escalable y distribuida de los servicios.

**SOA** 🏢:  
La localización de servicios suele ser más estática y centralizada (ESB, endpoints conocidos), por lo que el service discovery no es un elemento clave.

### 📝 Frase clave de examen

> **El service discovery es un patrón característico de arquitecturas de microservicios, no de SOA tradicional.**

---
## ACID vs SAGA

**ACID** 🧱:  
Modelo de transacciones que garantiza Atomicidad, Consistencia, Aislamiento y Durabilidad, típico de bases de datos monolíticas y sistemas centralizados.

**SAGA** 🔄:  
Patrón de gestión de transacciones distribuidas que divide una operación en múltiples transacciones locales con acciones de compensación ante fallos.

### 📝 Frase clave de examen

> **ACID garantiza consistencia fuerte; SAGA prioriza escalabilidad y tolerancia a fallos en sistemas distribuidos.**

---
## Service Façade

**Service Façade** 🧩:  
Patrón de diseño que proporciona una interfaz simplificada y unificada frente a uno o varios servicios complejos, ocultando su lógica interna.

### 📝 Frase clave de examen

> **Service Façade simplifica el acceso a servicios complejos mediante una interfaz única.**

---
## Fallback (patrón de resiliencia)

**Fallback** 🛟:  
Patrón de resiliencia que define una respuesta alternativa cuando un servicio o dependencia falla, evitando la interrupción total del sistema.

### 🧩 Ejemplo
- El servicio de recomendaciones no responde  
- Se muestra una lista de productos genéricos o en caché en lugar de fallar la aplicación

### 📝 Frase clave de examen

> **El patrón Fallback permite degradar el servicio de forma controlada ante fallos.**

---
## DLQ (Dead Letter Queue)

**DLQ (Dead Letter Queue)** 📬:  
Cola donde se almacenan mensajes que no han podido ser procesados correctamente tras varios intentos.

### 📝 Frase clave de examen

> **La DLQ permite aislar mensajes fallidos sin bloquear el flujo normal del sistema.**

---
## Bulkhead Pattern

**Bulkhead Pattern** 🚢:  
Patrón de resiliencia que aísla componentes o recursos para evitar que el fallo de uno afecte al resto del sistema.

### 📝 Frase clave de examen

> **El patrón Bulkhead limita el impacto de fallos mediante aislamiento de recursos.**

---
## Canonical Data Model (CDM)

**Canonical Data Model (CDM)** 🧩:  
Modelo de datos común y estandarizado que permite la interoperabilidad entre sistemas heterogéneos reduciendo dependencias punto a punto.

### 📝 Frase clave de examen

> **El CDM desacopla sistemas mediante un modelo de datos común compartido.**

---
## CDM vs DDD (Domain-Driven Design)

**CDM (Canonical Data Model)** 🧩:  
Modelo de datos común y estandarizado para integrar sistemas y reducir acoplamientos punto a punto.

**DDD (Domain-Driven Design)** 🧠:  
Enfoque de diseño que modela el software a partir del dominio de negocio, usando contextos delimitados y modelos propios.

### 📝 Frase clave de examen

> **CDM busca estandarizar datos entre sistemas; DDD prioriza la autonomía del dominio y evita modelos globales.**

---
## Loose Coupling

**Loose Coupling** 🔗:  
Principio de diseño que minimiza las dependencias entre componentes para facilitar cambios, escalabilidad y mantenimiento.

### 📝 Frase clave de examen

> **El loose coupling permite evolucionar sistemas sin afectar al resto de componentes.**

---
## CQRS (Command Query Responsibility Segregation)

**CQRS** 🔀:  
Patrón arquitectónico que separa las operaciones de escritura (commands) de las de lectura (queries) en modelos distintos.

### 📝 Frase clave de examen

> **CQRS separa lectura y escritura para mejorar escalabilidad y rendimiento.**

---
## Tracing distribuido: Span y Trace Context

**Span** 🧩:  
Unidad básica de trabajo en el tracing distribuido que representa una operación concreta con inicio, fin y metadatos.

**Trace Context** 🧭:  
Información de contexto que se propaga entre servicios para correlacionar todos los spans de una misma petición.

### 📝 Frase clave de examen

> **Un trace se compone de múltiples spans correlacionados mediante el trace context.**

---
## AMQP (Advanced Message Queuing Protocol)

**AMQP** 📬:  
Protocolo estándar de mensajería que permite la comunicación asíncrona y fiable entre sistemas mediante colas y brokers.

### 📝 Frase clave de examen

> **AMQP garantiza mensajería fiable y desacoplada entre aplicaciones.**

---
## API Portal, API Manager y API Gateway

**API Gateway** 🚪:  
Componente que actúa como punto de entrada único a las APIs, gestionando enrutado, seguridad, control de tráfico y políticas.

**API Manager** 🧭:  
Herramienta de gobierno que permite gestionar el ciclo de vida de las APIs, aplicar políticas, controlar versiones y monitorizar su uso.

**API Portal** 🌐:  
Interfaz orientada a desarrolladores donde se documentan las APIs y se facilita su descubrimiento, prueba y consumo.

### 📝 Frase clave de examen

> **El API Gateway ejecuta políticas en tiempo real, el API Manager gobierna las APIs y el API Portal facilita su consumo.**

---
## Database per Service

**Database per Service** 🗄️:  
Patrón de arquitectura (típico de microservicios) donde cada servicio posee y gestiona su propia base de datos de forma independiente.

**Impacto en consistencia** ⚖️:  
Se pierde la consistencia fuerte ACID entre servicios y se adopta **consistencia eventual**, normalmente mediante eventos o patrones como SAGA.

### 📝 Frase clave de examen

> **Database per Service elimina transacciones ACID globales y favorece la consistencia eventual para mejorar desacoplamiento y escalabilidad.**

---
## Estrategias de Comunicación entre Servicios

### Comunicación Síncrona (REST / gRPC) ⏱️
Modelo en el que un servicio llama a otro y **espera la respuesta** antes de continuar.

- Bloqueante
- Ideal para consultas inmediatas del usuario
- Alto acoplamiento temporal entre servicios

### Comunicación Asíncrona (Event-Driven) 🔄
Modelo basado en **eventos y mensajería**, donde el emisor no espera respuesta directa.

- No bloqueante (“dispara y olvida”)
- El consumidor procesa cuando puede
- Mejora resiliencia y desacoplamiento
- Uso típico de **RabbitMQ, Kafka**

### 📝 Frase clave de examen

> **La comunicación síncrona es bloqueante y acoplada en el tiempo; la asíncrona es no bloqueante, resiliente y desacoplada.**

---
## UDDI (Universal Description, Discovery, and Integration)

**UDDI** 📇:  
Estándar OASIS para registro y descubrimiento de servicios web SOAP que funciona como un "directorio público" o "páginas amarillas" de servicios empresariales.

**Componentes estructurales** 🏗️:  
Organiza la información en **páginas blancas** (datos del proveedor), **páginas amarillas** (clasificación por industria) y **páginas verdes** (detalles técnicos WSDL y endpoints).

### 📝 Frase clave de examen

> **UDDI fue el intento de crear un DNS universal para servicios web SOAP, que fracasó por complejidad y falta de adopción, siendo reemplazado por registros privados y API Portals.**