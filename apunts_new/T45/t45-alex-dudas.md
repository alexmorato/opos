### **Calidad/Pruebas**
1. **Flaky tests**  
2. **E2E en CI**  
3. **Test Oracle**  
4. **MC/DC**  
5. **Criterios entrada/salida pruebas**

---
| 🧪 **Tipus** | 🎯 **Objectiu** | 📌 **Exemple** |
|------------|----------------|---------------|
| 🧩 **Unitàries** | Validar mòduls o funcions individuals | Provar una funció que calcula l’IVA |
| 🔗 **Integració** | Verificar la interacció entre mòduls | Comprovar que la base de dades comunica bé amb l’API |
| 🖥️ **Sistema** | Validar el sistema complet | Test *end-to-end* d’un flux complet |
| ✅ **Acceptació (UAT)** | Confirmar que compleix les expectatives de l’usuari | L’usuari valida que pot generar un informe |
| 🔁 **Regressió** | Reexecutar proves després de canvis per assegurar que no s’han introduït nous errors | Després d’una actualització de l’API |
| 🚀 **Rendiment (Performance)** | Comprovar temps de resposta, càrrega i estrès | 1000 usuaris simultanis |
| 🔐 **Seguretat** | Avaluar vulnerabilitats i accessos no autoritzats | Proves d’injecció SQL o XSS |
| 👥 **Usabilitat** | Verificar la facilitat d’ús | Test amb usuaris reals |

---
## Test Oracle

**Test Oracle** 🧾:  
Fuente o mecanismo que determina si el resultado de una ejecución de prueba es correcto o incorrecto, proporcionando el resultado esperado para la comparación.

📝 **Frase clave** de examen:

> **Un Test Oracle actúa como criterio de verificación para decidir el éxito o fracaso de un test, siendo especialmente crítico en sistemas complejos donde no existe un resultado obvio.**
---

## MC/DC (Modified Condition/Decision Coverage)

**MC/DC** ✅:  
Criterio de cobertura de pruebas que garantiza que cada condición individual dentro de una decisión afecte independientemente al resultado, usado en sistemas de alta criticidad.

📝 **Frase clave** de examen:

> **MC/DC es un criterio riguroso de cobertura de condiciones que requiere que cada entrada lógica muestre un efecto independiente en la salida, clave para certificación en sectores como aeronáutica (DO-178C).**
---

## Criterios de entrada y salida en fases de prueba

**Criterios de entrada** 🟢:  
Condiciones que deben cumplirse antes de iniciar una fase de pruebas (ej: código estable, entorno preparado, casos diseñados).

**Criterios de salida** 🔴:  
Condiciones que deben cumplirse para finalizar una fase de pruebas (ej: cobertura alcanzada, defectos críticos resueltos, rendimiento validado).

📝 **Frase clave** de examen:

> **Los criterios de entrada garantizan que las pruebas comiencen en condiciones adecuadas, mientras que los de salida definen cuándo pueden considerarse completas con calidad aceptable.**
---

## Flaky Test

**Flaky Test** 🎲:  
Prueba que produce resultados inconsistentes (pasa o falla) ejecutando el mismo código sin cambios, erosionando la confianza en el pipeline de CI/CD.

📝 **Frase clave** de examen:

> **Los Flaky Tests son pruebas no deterministas que indican dependencias externas, problemas de timing o estado compartido, y deben abordarse rápidamente para mantener la fiabilidad del proceso de testing.**
---

## SAST (Static Application Security Testing)

**SAST (Static Application Security Testing)** 🔍:  
Análisis de seguridad que examina el código fuente sin ejecutarlo para encontrar vulnerabilidades, malas prácticas y debilidades de seguridad.

📝 **Frase clave** de examen:

> **SAST permite detectar vulnerabilidades de seguridad en fases tempranas del desarrollo (shift-left) analizando el código estático, complementando con DAST para cobertura completa.**
---

## QA vs QC

**QA (Quality Assurance)** 🛡️:  
Enfoque proactivo que garantiza procesos para desarrollar software con calidad mediante estándares, auditorías y mejora continua.

**QC (Quality Control)** ✅:  
Enfoque reactivo que verifica el producto mediante pruebas, inspecciones y validaciones para encontrar y corregir defectos.

📝 **Frase clave** de examen:

> **QA se centra en prevenir defectos mejorando los procesos, mientras que QC se enfoca en detectar defectos en el producto entregable; ambos son complementarios para la calidad total.**
---

## Validación vs Verificación

**Validación** 🎯:  
Proceso de comprobar que "se construye el producto correcto", evaluando si satisface las necesidades reales del usuario.

**Verificación** ✅:  
Proceso de comprobar que "se construye el producto correctamente", evaluando el cumplimiento de especificaciones y estándares.

📝 **Frase clave** de examen:

> **La verificación responde a '¿Lo hacemos bien?' (cumplimiento de especificaciones), mientras que la validación responde a '¿Hacemos lo correcto?' (utilidad para el usuario).**
---

## FMEA en calidad de software

**FMEA (Failure Mode and Effects Analysis)** ⚠️:  
Método sistemático y proactivo para identificar modos de fallo potenciales, sus causas y efectos, priorizando riesgos mediante RPN (Risk Priority Number).

📝 **Frase clave** de examen:

> **FMEA en software es un análisis preventivo que cuantifica riesgos mediante Severidad × Ocurrencia × Detección (RPN), priorizando mitigaciones antes de que ocurran fallos en producción.**
---

## E2E en CI

**E2E en CI** 🧪:  
Integración de pruebas End-to-End dentro del pipeline de Integración Continua para validar flujos completos de usuario en cada cambio de código.

📝 **Frase clave** de examen:

> **Incluir pruebas E2E en CI valida el sistema completo en entornos similares a producción, pero requiere gestión cuidadosa de su fragilidad y coste computacional para mantener la velocidad del pipeline.**
---