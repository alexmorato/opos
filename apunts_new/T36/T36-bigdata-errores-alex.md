Perfecto.
Aquí tienes la **lista final consolidada del Tema 36 – Big Data y Data Lake**, con:

* 🔹 Concepto
* 🔹 Descripción breve
* 🔹 Frase clave de examen

Ya está estructurada para repaso rápido pre-examen.

---

# 📋 TEMA 36 – BIG DATA (LISTA FINAL CONSOLIDADA)

---

## 1️⃣ ETL

**Descripción:** Transformar antes de cargar (BI tradicional).
**Frase clave:** ETL limpia antes de cargar.

---

## 2️⃣ ELT

**Descripción:** Cargar primero y transformar dentro (Data Lake / cloud).
**Frase clave:** ELT guarda todo y transforma después.

---

## 3️⃣ CDC

**Descripción:** Captura solo cambios (insert/update/delete).
**Frase clave:** CDC copia solo lo que cambia.

---

## 4️⃣ Arquitectura Lambda

**Descripción:** Batch + Speed Layer.
**Frase clave:** Lambda divide histórico y tiempo real.

---

## 5️⃣ Arquitectura Kappa

**Descripción:** Solo streaming.
**Frase clave:** Kappa unifica todo en streaming.

---

## 6️⃣ Apache Storm

**Descripción:** Motor de streaming distribuido en tiempo real.
**Frase clave:** Storm procesa eventos en tiempo real continuo.

---

## 7️⃣ Apache Spark

**Descripción:** Motor generalista (batch + micro-batch).
Execution model lazy + DAG.
**Frase clave:** Spark es versátil y ejecuta al lanzar una action.

---

## 8️⃣ Apache Flink

**Descripción:** Streaming nativo evento a evento.
**Frase clave:** Flink procesa evento a evento.

---

## 9️⃣ Azure Databricks

**Descripción:** Servicio gestionado Spark en Azure.
**Frase clave:** Spark en Azure = Databricks.

---

## 🔟 DAMA-DMBOK

**Descripción:** Marco de gobernanza del dato.
**Frase clave:** DAMA gobierna el dato como activo.

---

## 1️⃣1️⃣ Roles de gobernanza

### Data Owner

Responsable estratégico.

### Data Steward

Calidad y coherencia diaria.

### Data Custodian

Infraestructura y seguridad técnica.

### DPO

Cumplimiento normativo.

**Frase clave global:**
Steward calidad, Custodian protección, Owner responsabilidad, DPO normativa.

---

## 1️⃣2️⃣ Hadoop Ecosystem

* HDFS → almacena
* MapReduce → procesa
* YARN → gestiona recursos
* Hadoop Common → librerías base

**Frase clave:** Hadoop distribuye almacenamiento y procesamiento.

---

## 1️⃣3️⃣ YARN

**Descripción:** Gestor de recursos del clúster.
**Frase clave:** YARN reparte recursos, no procesa datos.

---

## 1️⃣4️⃣ Parquet

**Descripción:** Formato columnar optimizado para analítica.
**Frase clave:** Parquet = columnas = consultas eficientes.

---

## 1️⃣5️⃣ Avro

**Descripción:** Formato binario orientado a filas.
**Frase clave:** Avro = filas = intercambio eficiente.

---

## 1️⃣6️⃣ Apache NiFi

**Descripción:** Orquestación y automatización de flujos de datos.
**Frase clave:** NiFi mueve y orquesta datos.

---

## 1️⃣7️⃣ TensorFlow

**Descripción:** Librería de Machine Learning.
**Frase clave:** TensorFlow entrena modelos.

---

## 1️⃣8️⃣ Apache Atlas

**Descripción:** Gobernanza y catalogación de metadatos.
**Frase clave:** Atlas cataloga y gobierna metadatos.

---

## 1️⃣9️⃣ Apache Hudi

**Descripción:** Updates, deletes y time travel en Data Lake.
**Frase clave:** Hudi añade transacciones y versionado al Data Lake.

---

## 2️⃣0️⃣ NoSQL – Documento

**Descripción:** Ideal para estructura flexible (JSON).
**Frase clave:** Documento = esquema flexible.

---

## 2️⃣1️⃣ 3 niveles de analítica

* Descriptiva → pasado
* Predictiva → futuro
* Prescriptiva → decisión

**Frase clave:** De describir a decidir.

---

## 2️⃣2️⃣ 4V del Big Data

* Volumen
* Velocidad
* Variedad (formatos, no fuentes)
* Veracidad

**Frase clave:** Variedad es formato, no origen.

---

## 2️⃣3️⃣ Big Data vs BI

**Descripción:** Big Data no es obligatorio en todo BI.
**Frase clave:** BI analiza; Big Data escala.

---

## 2️⃣4️⃣ Medallion Architecture

* Bronze → dato bruto
* Silver → dato limpio
* Gold → dato de negocio

**Frase clave:** Bronze guarda, Silver limpia, Gold genera valor.

---

## 🎯 Patrón global del Tema 36

Las preguntas se resuelven diferenciando:

* Batch vs Streaming
* Columnar vs Filas
* Gobernanza vs Procesamiento
* Orquestación vs Machine Learning
* Arquitectura clásica vs Lakehouse
* BI tradicional vs Big Data

---

# 📌 Frase estratégica final del tema 36

> Big Data se domina diferenciando arquitectura, motor de procesamiento, formato de datos y modelo de gobernanza.

---

Si quieres, ahora podemos hacer un **simulacro difícil solo de Tema 36** para cerrar bloque.
