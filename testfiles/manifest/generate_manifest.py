import os
import json
import sys


# CONFIGURACIÓN
# Lista de palabras prohibidas
palabras_prohibidas = ["manifest"]  # Modifica según necesidad

# Leer carpeta desde parámetros
if len(sys.argv) != 2:
    print("Uso: python generate_manifest.py <ruta_carpeta>")
    sys.exit(1)

carpeta = sys.argv[1]
carpeta_destino = carpeta  # Carpeta y destino son iguales

if not os.path.isdir(carpeta):
    print(f"Error: La carpeta '{carpeta}' no existe")
    sys.exit(1)

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