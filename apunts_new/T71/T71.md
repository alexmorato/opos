# **Tema 71. Ciberseguridad Aplicada al Cloud - Resumen Ejecutivo** ☁️🔒

## **1. 🏗️ MODELOS DE SERVICIO (Responsabilidad Compartida)**
| Modelo | Qué gestiona el Proveedor (Cloud) | Qué gestiona el Cliente (Tú/Ayuntamiento) | Ejemplo |
|--------|-----------------------------------|------------------------------------------|---------|
| **IaaS** (Infraestructura) | Hardware, Red, Virtualización | SO, Apps, Datos, Configuración | AWS EC2, Azure VMs |
| **PaaS** (Plataforma) | IaaS + SO, Middleware, Runtime | Aplicación y Datos | Google App Engine, Azure App Service |
| **SaaS** (Software) | Casi todo (App, Infraestructura) | Datos, Configuración de Usuario | Office 365, Salesforce |

**⚠️ REGLA DE ORO:** "El cliente es **siempre responsable** de la seguridad **EN** la nube. El proveedor es responsable **DE** la nube."

## **2. 🌍 MODELOS DE DESPLIEGUE**
- **Pública ☁️:** Multi-tenant, eficiente, escalable. Menor control. (Ej: AWS, Azure).
- **Privada 🏢:** Infraestructura exclusiva (on-premise o alojada). Mayor control y coste.
- **Híbrida 🔀:** Combina pública y privada. Permite *cloud bursting*. Complejidad de seguridad.
- **Comunitaria 🤝:** Varias organizaciones con necesidades comunes comparten infraestructura.

## **3. 🚨 AMENAZAS PRINCIPALES (Top CSA)**
1.  **💥 Filtración de Datos** (Amenaza #1).
2.  **👥 Gestión débil de Identidad y Acceso** (IAM).
3.  **🌐 Interfaces/APIs Inseguras.**
4.  **🐛 Vulnerabilidades del Sistema.**
5.  **🎭 Secuestro de Cuentas.**
6.  **👨‍💼 Amenazas Internas.**
7.  **🔍 APTs (Amenazas Persistentes Avanzadas).**
8.  **📉 Pérdida de Datos.**
9.  **🔎 Falta de Diligencia Debida.**
10. **🛠️ Abuso del Servicio Cloud.**

## **4. 🛡️ PILARES DE SEGURIDAD CLOUD**
- **🔐 Cifrado:** **En tránsito** (TLS 1.2+) y **en reposo** (AES-256). Gestión de claves (BYOK/HYOK - Bring/Hold Your Own Key).
- **👤 IAM (Gestión de Identidad y Acceso):** Principio de **mínimo privilegio**, **MFA obligatorio**, SSO, roles bien definidos (Azure AD, AWS IAM).
- **🌐 Seguridad de Red:** **Segmentación** (VPC/VNet), **Firewalls** (WAF, NGFW), **Conexiones Privadas** (AWS Direct Connect, Azure ExpressRoute), Protección DDoS.
- **📊 Gobernanza y Cumplimiento:**
    - **CSPM (Cloud Security Posture Management):** Herramientas para **detectar y corregir configuraciones erróneas** (la causa #1 de incidentes).
    - **CASB (Cloud Access Security Broker):** Puente de seguridad entre usuarios y servicios cloud. Controla sombra (Shadow IT).
    - **Cumplimiento Normativo:** **ENS (Esquema Nacional de Seguridad)** para ayuntamientos, GDPR, ISO 27001.
- **💾 Resiliencia y Backup:** Estrategia **3-2-1** (3 copias, 2 medios, 1 externa), **DRaaS** (Recuperación ante Desastres como Servicio), Alta Disponibilidad entre Zonas/Regiones.

## **5. 🏛️ CONSIDERACIONES ESPECÍFICAS PARA ADMINISTRACIÓN PÚBLICA**
- **🗺️ Soberanía de Datos:** Los datos **deben residir en la UE/España** (Atención a cláusulas de contratos).
- **⚖️ Cumplimiento ENS:** Nivel **ALTO** para sistemas críticos. Requiere medidas específicas de cifrado, registro, control de acceso y auditoría.
- **🏢 Proveedores Cualificados:** Preferencia por proveedores con **certificaciones del CCN** (STIC) o que garanticen cumplimiento ENS.
- **📑 Contratación Pública:** Pliegos técnicos deben especificar: **Localización de datos, propiedad, portabilidad, seguridad, procedimientos de borrado seguro.**
- **📈 Monitorización Centralizada:** **SIEM en cloud** para correlacionar logs de diferentes servicios (necesario para ENS nivel alto).

## **6. ✅ BUENAS PRÁCTICAS IMPRESCINDIBLES**
1.  **📋 Inventariar y Clasificar** datos **antes** de migrar (Públicos, Restringidos, Confidenciales).
2.  **🔧 "Secure by Default":** Activar cifrado, MFA, logging **desde el despliegue**.
3.  **🚫 Configuraciones Erróneas:** Usar **CSPM** para escaneo continuo. Revisar permisos de almacenamiento (S3 buckets, Blob Storage).
4.  **🧪 Pruebas de Seguridad:** Pentesting autorizado en entornos cloud. Uso de *Infrastructure as Code* (IaC) con escaneo de seguridad (Terraform, CloudFormation).
5.  **🔄 Formación Continua:** Equipos de ops y desarrollo en **seguridad cloud (DevSecOps).**

## **7. 🔄 PATRONES DE ARQUITECTURA SEGURA**
- **Zero Trust Network (ZTNA):** "Nunca confíes, siempre verifica". Acceso basado en identidad, no en red.
- **Microsegmentación:** Aislamiento de cargas de trabajo incluso dentro de la misma red.
- **Cloud-Native Security:** Uso de servicios nativos del proveedor (AWS Security Hub, Azure Security Center, Google Security Command Center).

---

**📌 PALABRAS CLAVE RESPONSABILIDAD COMPARTIDA | IAM & MFA | CIFRADO | CONFIGURACIÓN ERRÓNEA | ENS & SOBERANÍA DE DATOS | CSPM | RESILIENCIA**

# **🚨 Trampas y confusiones comunes en Ciberseguridad Cloud**

## **⚠️ FALSAS SEGURIDADES (Errores Graves)**
1.  **"La nube es inherentemente segura"** ❌  
    → **REALIDAD:** Solo la infraestructura base. Tu configuración y datos son tu responsabilidad.

2.  **"Mi proveedor hace backup automático"** 🔄  
    → **REALIDAD:** Backup ≠ Recuperación. Probarlo periódicamente. Proveedor no garantiza recuperación de *tus* datos borrados por error.

3.  **"Cifrado = Seguridad total"** 🔐  
    → **REALIDAD:** Cifrar sin gestionar bien las claves (acceso, rotación) es como dejar la lluja bajo el felpudo.

## **🔄 CONFUSIONES TÉCNICAS**
4.  **"Alta Disponibilidad (HA) = Tolerancia a Fallos (DR)"** ⚠️  
    → **HA:** Resistencia a fallos técnicos (ej: una zona cae).  
    → **DR:** Recuperación tras desastre mayor (ej: región entera cae). Necesitas **ambos**.

5.  **"IAM solo es para usuarios humanos"** 👤  
    → **REALIDAD:** Las **identidades de servicio** (máquinas, apps) son igual de críticas y deben tener permisos mínimos.

6.  **"Contenedores (Docker) = Máquinas Virtuales seguras"** 🐳  
    → **REALIDAD:** Comparten kernel del host. Escape de contenedor = acceso total al host. Seguridad diferente.

## **🏛️ ERRORES EN ADMINISTRACIÓN PÚBLICA**
7.  **"Cumplir ENS local = Cumplir ENS en cloud"** 📋  
    → **REALIDAD:** ENS en cloud requiere **medidas específicas** (ej: cifrado en reposo SIEMPRE, trazabilidad completa, TIC cualificadas).

8.  **"El proveedor gestiona el cumplimiento normativo por mí"** ⚖️  
    → **REALIDAD:** Ellos ofrecen herramientas, **tú** debes configurarlas y demostrar el cumplimiento (auditorías).

9.  **"Los datos en la UE cumplen soberanía"** 🇪🇺  
    → **TRAMPA:** Algunos proveedores pueden replicar a países extracomunitarios o usar subcontratistas no aprobados. **Verificar cláusulas contractuales**.

## **🔧 FALLOS OPERATIVOS COMUNES**
10. **"Configuración por defecto es segura"** ⚙️  
    → **REALIDAD:** NO. Buckets S3/Blobs públicos, puertos abiertos, logging desactivado... Revisar TODO.

11. **"Shadow IT no existe en administración"** 👻  
    → **REALIDAD:** Departamentos usan SaaS no autorizado (Google Drive, Dropbox) para agilidad, exponiendo datos.

12. **"Cloud es más barato siempre"** 💰  
    → **TRAMPA:** Costes ocultos por: tráfico de salida, APIs llamadas, almacenamiento no optimizado, licencias.

## **🎯 CONFUSIÓN CLAVE PARA EL EXAMEN**
13. **"Responsabilidad compartida = Responsabilidad dividida 50/50"** ⚖️  
    → **REALIDAD:** Modelo de **capas**. Según el servicio (IaaS/PaaS/SaaS), tu responsabilidad **aumenta o disminuye**.  
    **SIEMPRE tuyo:** Datos, identidades, dispositivos cliente.  
    **NUNCA tuyo:** Seguridad física del data center.

14. **"CSPM y CASB son lo mismo"** 🔍  
    → **CSPM:** Protege **la infraestructura** cloud (configuraciones erróneas).  
    → **CASB:** Protege **el uso** del cloud (shadow IT, acceso de usuarios).

15. **"Zero Trust es solo para acceso remoto"** 🛡️  
    → **REALIDAD:** Es un **modelo arquitectónico completo**: microsegmentación interna, verificación continua, mínimo privilegio en TODAS las capas.

---

**✅ RECUERDA:** El mayor riesgo en cloud es **LA CONFIGURACIÓN ERRÓNEA**.  
La mayor confusión es pensar que **"cloud es solo otro data center"**.  
El cambio de mentalidad a **"cloud-native security"** es crucial.