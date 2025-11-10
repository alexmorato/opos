// localstorage-utils.js

// Claves usadas en localStorage
const LS_KEYS = {
  PREGUNTA_POSITION: 'sTICdOpos_preguntaPosition',
  PREGUNTES_BARREJADES: 'sTICdOpos_preguntesBarrejades',
  ANSWERS: 'sTICdOpos_answers',
  CRONOMETRO: 'sTICdOpos_cronometro',
  PREGUNTES: 'sTICdOpos_preguntes',
  HISTORIAL_FALLOS: 'sTICdOpos_historialFallos',
  USER: 'oposTest_user',
  USER_GUID: 'user_guid',
  USER_ID: 'user_id',
};

// Método para borrar el estado guardado de estudio
function borrarEstudioGuardado() {
  localStorage.removeItem(LS_KEYS.PREGUNTES_BARREJADES);
  localStorage.removeItem(LS_KEYS.ANSWERS);
  localStorage.removeItem(LS_KEYS.CRONOMETRO);
  localStorage.removeItem(LS_KEYS.PREGUNTA_POSITION);
}
