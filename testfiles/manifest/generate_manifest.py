import os
import json


# CONFIGURACIÓN
# Carpeta a listar
carpeta = ".."  # Cambia esta ruta según necesidad
# Carpeta destino para el manifest.json
carpeta_destino = ".."  # Cambia esta ruta según necesidad
# Lista de palabras prohibidas
palabras_prohibidas = ["manifest"]  # Modifica según necesidad

# Listar solo archivos (no carpetas) y filtrar por palabras prohibidas
ficheros = []
for f in os.listdir(carpeta):
    if os.path.isfile(os.path.join(carpeta, f)):
        if not any(palabra in f for palabra in palabras_prohibidas):
            ficheros.append(f)

# Crear el diccionario con el formato requerido
manifest = {
    "files": ficheros
}


# Guardar el manifest en un archivo JSON en la carpeta destino
manifest_path = os.path.join(carpeta_destino, "manifest.json")
with open(manifest_path, "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)

print(f"Manifest generado correctamente en: {manifest_path}")