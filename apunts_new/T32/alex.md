# **TEMA 32 · POWER BI - RESUMEN DISPARO**

## **¿QUÉ ES?**
- **Herramienta de Microsoft** para análisis y visualización de datos
- **Business Intelligence en autoservicio** (self-service BI)

## **TRES PARTES CLAVE**
1. **Power BI Desktop** → Crear informes (gratis)
2. **Power BI Service** → Publicar y compartir en web (nube)
3. **Power BI Mobile** → Ver en móvil/tablet

## **¿CÓMO FUNCIONA?**
```
Conectar datos → Transformar → Modelar → Visualizar → Compartir
```

## **4 COMPONENTES TÉCNICOS**
1. **Power Query** → Limpiar y preparar datos (ETL)
2. **Power Pivot** → Modelo de datos y relaciones
3. **DAX** → Lenguaje de fórmulas (como Excel avanzado)
4. **Visualizaciones** → Gráficos interactivos y dashboards

## **CASOS USO AYUNTAMIENTO**
- **Cuadros de mando** de servicios municipales
- **Análisis presupuestario** y gasto público
- **Indicadores sociales** por distritos
- **Transparencia** con datos abiertos (Open Data BCN)
- **Seguimiento ODS** (Objetivos Desarrollo Sostenible)

## **VENTAJAS CLAVE**
- **Integración total** con Microsoft (Excel, SharePoint, Azure)
- **Actualización automática** de datos
- **Colaboración** y compartición segura
- **Mobile-friendly** (acceso desde cualquier dispositivo)
- **Escalable** de pequeño a gran volumen

## **PALABRAS CLAVE EXAMEN**
- **ETL**: Extraer, Transformar, Cargar
- **DAX**: Data Analysis Expressions
- **Dashboard**: Cuadro de mando interactivo
- **Self-service BI**: Usuarios finales crean sus informes
- **Refresh**: Actualización automática de datos

**ESENCIA**: Transforma datos municipales en información visual para tomar mejores decisiones.

## **Dataset (Power BI / Data Analytics)**

**Dataset**:  
Conjunto estructurado de datos que sirve como fuente principal para la creación de informes, análisis y visualizaciones en herramientas como Power BI. Incluye tablas, relaciones, medidas y metadatos.

> 📝 **Frase clave**: Un dataset es la materia prima organizada a partir de la cual Power BI genera informes y cuadros de mando interactivos.

---

## **ECOSISTEMA POWER BI - 4**

1. **Power BI Desktop** → Herramienta de escritorio gratuita para crear informes, modelos de datos y visualizaciones.
2. **Power BI Service (SaaS en la nube)** → Plataforma online donde se publican, comparten y colaboran en los informes y dashboards.
3. **Power BI Mobile** → Aplicaciones móviles para iOS y Android que permiten acceder y visualizar los dashboards desde cualquier lugar.
4. **Power BI Report Server** → Solución on-premise para organizaciones que necesitan alojar informes en su propia infraestructura, manteniendo control total sobre los datos.

> 📝 **Frase clave**: El ecosistema completo de Power BI abarca la creación (Desktop), la publicación en la nube (Service) o local (Report Server), y el consumo móvil (Mobile).

---
# **MODELADO DE DATOS EN POWER BI**

## **Conceptos Clave de Modelado**

### **1. Modelo de Datos**
- **Estructura relacional** entre tablas (similar a base de datos)
- **Relaciones** (uno a uno, uno a muchos, muchos a muchos)
- **Optimizado para consultas rápidas** (motor columnar VertiPaq)

### **2. Jerarquías**
- **Niveles organizados** para drill-down/up
- **Ejemplo municipal**:
  ```
  Distrito → Barrio → Sección censal
  Año → Trimestre → Mes → Día
  Categoría → Subcategoría → Producto
  ```

### **3. Tablas de Hechos vs Dimensiones**
- **Tablas de hechos**: Datos transaccionales (ventas, incidencias)
- **Tablas de dimensiones**: Datos descriptivos (tiempo, ubicación, categorías)

### **4. Columnas Calculadas vs Medidas**
- **Columnas calculadas**: Se agregan al modelo (se almacenan)
- **Medidas (DAX)**: Se calculan en tiempo de ejecución

## **Buenas Prácticas de Modelado**

### **1. Estrella vs Copo de Nieve**
- **Modelo estrella**: Una tabla de hechos + múltiples dimensiones
- **Modelo copo**: Dimensiones normalizadas (subdimensiones)

### **2. Optimización**
- **Eliminar columnas innecesarias**
- **Usar tipos de datos apropiados**
- **Crear relaciones correctas**
- **Tablas de fecha unificadas**

### **3. DAX Esencial para Modelado**
```dax
-- Medidas comunes
Ventas Totales = SUM(Ventas[Monto])
Promedio Móvil = AVERAGEX(DATESINPERIOD(...))
Ratio = DIVIDE([Numerador], [Denominador])
```

> 📝 **Frase clave**: Un buen modelado en Power BI es la base para informes rápidos, precisos y mantenibles. Define cómo se relacionan los datos y cómo se pueden analizar.