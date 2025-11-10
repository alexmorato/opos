// localstorage-utils.js

// Claves usadas en localStorage
const LS_KEYS = {
  TEMAS: 'sTICdOpos_temas',
  TIPO_PREGUNTA: 'sTICdOpos_tipoPregunta',
  DIFICULTAT: 'sTICdOpos_dificultat',
  ORIGIN: 'sTICdOpos_origin',
  FITXER: 'sTICdOpos_fitxer',
  PREGUNTA_POSITION: 'sTICdOpos_preguntaPosition',
  PREGUNTES_BARREJADES: 'sTICdOpos_preguntesBarrejades',
  ANSWERS: 'sTICdOpos_answers',
  CRONOMETRO: 'sTICdOpos_cronometro',
  PREGUNTES: 'sTICdOpos_preguntes',
  HISTORIAL_FALLOS: 'sTICdOpos_historialFallos',
  USER_NAME: 'sTICdOpos_userName',
  USER_PASS: 'sTICdOpos_userPass',
};

// Método para borrar el estado guardado de estudio
function borrarEstudioGuardado() {
  localStorage.removeItem(LS_KEYS.PREGUNTES_BARREJADES);
  localStorage.removeItem(LS_KEYS.ANSWERS);
  localStorage.removeItem(LS_KEYS.CRONOMETRO);
  localStorage.removeItem(LS_KEYS.PREGUNTA_POSITION);
}
