import os
import json

# Cambia esta ruta por la que desees listar
ruta = ".."

# Lista solo archivos (no carpetas)
ficheros = [f for f in os.listdir(ruta) if os.path.isfile(os.path.join(ruta, f))]

# Guarda el array en un archivo JSON
with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(ficheros, f, ensure_ascii=False, indent=2)

print("JSON generado con los nombres de los ficheros.")