
# ☁️ TEMA 43 – DESARROLLO DE APLICACIONES NATIVAS EN EL NÚVOL

¡Por supuesto! Aquí tienes la lista de conceptos con su **frase clave** para que los recuerdes fácilmente y puedas explicarlos de forma clara y concisa.

### **1. Fundamentos y Arquitectura**

| Concepto | Frase Clave (¿Qué es?) |
| :--- | :--- |
| **Aplicación Nativa de Cloud** | Diseñada **desde el inicio para la nube**, aprovechando su elasticidad y modelos de servicio. |
| **Arquitectura Monolítica** | Todo en uno: una sola base de código y despliegue. Acoplamiento total. |
| **Arquitectura de Microservicios** | Muchas piezas pequeñas e independientes que colaboran para formar una aplicación. |
| **Escalabilidad (Escalado)** | **Capacidad planificada** para manejar más carga. Crecer. |
| **Elasticidad** | **Adaptación automática** en tiempo real a la demanda. Estirar y encoger. |
| **Escalado Vertical** | Más potencia a la misma máquina (un camión más grande). |
| **Escalado Horizontal** | Más máquinas trabajando en equipo (más coches en la carretera). |

### **2. Pilares Tecnológicos**

| Concepto | Frase Clave (¿Qué es?) |
| :--- | :--- |
| **Contenedor** | **Unidad estándar de software** que empaqueta código y dependencias para ejecutarse de forma rápida y fiable. |
| **Máquina Virtual (VM)** | Emulación completa de un ordenador, con su propio sistema operativo. Más pesada y aislada. |
| **Dockerfile** | La **receta** o el plano para construir una imagen. |
| **Imagen (Docker)** | La **plantilla** inmutable y ejecutable, construida a partir del Dockerfile. |
| **Contenedor (Docker)** | La **instancia en ejecución** de una imagen. El proceso vivo. |
| **Orquestación (Kubernetes)** | El **sistema operativo del clúster** que automatiza el despliegue, escalado y gestión de contenedores. |
| **Rolling Update** | Actualización gradual y sin caída del servicio. |
| **Blue/Green Deployment** | Dos entornos idénticos (azul el actual, verde el nuevo); se cambia el tráfico de golpe. |
| **Canary Release** | Lanzamiento para un grupo reducido de usuarios como prueba, antes del despliegue masivo. |
| **Serverless** | Ejecuta código sin preocuparte por los servidores. Paga solo por el tiempo de ejecución. |
| **gRPC** | Marco de trabajo de RPC moderno y de alto rendimiento, mucho más rápido que JSON. |
| **Bases de Datos Distribuidas** | Bases de datos que se ejecutan en múltiples servidores para ofrecer escalabilidad y alta disponibilidad. |

### **3. Metodologías y Herramientas**

| Concepto | Frase Clave (¿Qué es?) |
| :--- | :--- |
| **Los Doce Factores** | Metodología con las mejores prácticas para construir aplicaciones como servicio. |
| **CI/CD (Integración/Despliegue Continuo)** | **Automatización total** de la construcción, prueba y despliegue del código. |
| **IaC (Infraestructura como Código)** | Gestionar servidores y redes con el mismo rigor que el código de la aplicación (versionado, revisión). |
| **DevSecOps** | Integrar la **seguridad desde el principio** en todo el ciclo de vida del desarrollo, no al final. |

### **4. Frameworks de Desarrollo**

| Concepto | Frase Clave (¿Qué es?) |
| :--- | :--- |
| **Spring Boot / Express.js** | Frameworks tradicionales muy potentes, adaptados a la nube, pero con mayor consumo de recursos. |
| **Quarkus / Micronaut** | Frameworks **nativos de nube**: arranque ultrarrápido y memoria mínima para optimizar contenedores y serverless. |

### **5. Ecosistema y Conceptos Avanzados (CNCF)**

| Concepto | Frase Clave (¿Qué es?) |
| :--- | :--- |
| **CNCF (Cloud Native Computing Foundation)** | La **fundación que alberga los proyectos estrella** del mundo cloud-native (Kubernetes, etc.). |
| **ROOK** | **Orquestador de almacenamiento** que convierte Kubernetes en tu propia plataforma de almacenamiento. |
| **CNI (Container Network Interface)** | El **estándar** que usa Kubernetes para conectar contenedores en red. |
| **Calico** | Un **plugin de red** (implementa CNI) que también proporciona políticas de seguridad para los contenedores. |
| **Docker Hub** | El **registro público por defecto** para imágenes de contenedores. |
| **Harbor** | Un **registro privado y empresarial** para tus propias imágenes, con seguridad y control avanzados. |
| **Helm** | El **gestor de paquetes de Kubernetes**. Un "apt-get" o "yum" para tu clúster. |
| **Helm Chart**| Un **paquete predefinido** con todos los archivos YAML de una aplicación para desplegarla fácilmente. |
| **GitOps** | Usar Git como la **única fuente de verdad** para la configuración y los despliegues en el clúster. |

¡Espero que esta lista te sea de gran ayuda para estudiar y repasar!