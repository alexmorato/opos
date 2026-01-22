# esquema super reducido
Estoy estudiando para Oposiciones tecnico superior TIC para el ayuntamiento de barcelona.
Dame la teoria para estudiar este tema: 29 – Gestió d’Incidents de Ciberseguretat
Primero un esquema muy reducido.
Luego conceptos clave para el examen.
Luego trampas o errores que puedan poner en el examen tipo test.
Pon algun emoji para que sea un poco visual.
Si crees necesaria algun grafico ascci.
Tiene que ser algo que pueda leer en 10 minutos.


# preguntas

Generame preguntas tipo test.
subjectid: T29
preguntas normales-dificiles no muy largas.
Preguntas trampas que puedan liar
Alguna pregunta que sea cual NO es correcta
Alguna que sea cual es la mas correcta.

Quiero que generes un JSON con estas caracteristicas.
Un array de QuestionContract.
interface QuestionContract {
  guid: string; // Genera un GUID, Identificador Único Global, una cadena de 128 bits diseñada para ser única en el mundo
  subjectId: string; // Identificador del tema o materia (por ejemplo, "T62", "T08", "Ambit1")
  difficulty: 1 ; // Identificador numerico del nivel de dificultad 1-facil, 2-medio, 3-dificil, 4-avanzado, 5-mortal
  origin: string; // Fuente o sistema de origen (por ejemplo, "OPOS19_preguntes_practic.pdf" para extracciones de ficheros o “OPOS24_gpt” para cuando las genera el chatgpt o "deepseek" cuando las genera DeepSeek)
  type: string; // Tipo de pregunta (por ejemplo, "test", “truefalse”, “fillgap”)
  question: string; // Texto de la pregunta
  answerOptions: AnswerOption[]; // Opciones de respuesta
  hint?: string; // (Opcional) pista o ayuda para el usuario
}
interface AnswerOption {
  text: string; // Texto de la opción de respuesta. No pongas A B C o D, solo el texto de la opción.
  isCorrect: boolean; // Indica si la opción es la respuesta correcta
  rationale: string; // Explicación o justificación de la opción
}
Haré copy-paste del JSON.
