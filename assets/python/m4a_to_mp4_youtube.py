import os
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


INPUT_DIR = Path("D:/AlexPersonal/OPOS25/SETA/audios_m4a")
OUTPUT_DIR = Path("D:/AlexPersonal/OPOS25/SETA/audios_m4a/videos_mp4")


def crear_portada(texto: str, output_path: Path, size=(1280, 720)):
    """
    Crea una imagen simple tipo portada, compatible con YouTube.
    """
    img = Image.new("RGB", size, color=(20, 20, 20))
    draw = ImageDraw.Draw(img)

    # Intentar usar una fuente decente (si no, usa la default)
    try:
        font = ImageFont.truetype("arial.ttf", 48)
    except:
        font = ImageFont.load_default()

    # Cortar texto si es demasiado largo
    texto = texto.strip()
    if len(texto) > 60:
        texto = texto[:57] + "..."

    # Centrar texto
    bbox = draw.textbbox((0, 0), texto, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]

    x = (size[0] - w) // 2
    y = (size[1] - h) // 2

    draw.text((x, y), texto, font=font, fill=(240, 240, 240))

    img.save(output_path)


def convertir_m4a_a_mp4(m4a_path: Path, portada_path: Path, mp4_path: Path):
    """
    Convierte un M4A a MP4 añadiendo una imagen fija (portada).
    """
    cmd = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", str(portada_path),
        "-i", str(m4a_path),
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-pix_fmt", "yuv420p",
        "-shortest",
        str(mp4_path)
    ]

    subprocess.run(cmd, check=True)


def main():
    if not INPUT_DIR.exists():
        print(f"❌ No existe la carpeta: {INPUT_DIR}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    m4as = list(INPUT_DIR.glob("*.m4a"))
    if not m4as:
        print(f"❌ No se han encontrado .m4a en: {INPUT_DIR}")
        return

    print(f"🎧 Audios encontrados: {len(m4as)}")
    print("----")

    for m4a in m4as:
        nombre = m4a.stem

        portada = OUTPUT_DIR / f"{nombre}_cover.jpg"
        mp4 = OUTPUT_DIR / f"{nombre}.mp4"

        print(f"➡️ Procesando: {m4a.name}")

        # 1) Crear portada
        crear_portada(nombre, portada)

        # 2) Convertir a mp4
        try:
            convertir_m4a_a_mp4(m4a, portada, mp4)
            print(f"   ✅ OK -> {mp4.name}")
        except subprocess.CalledProcessError:
            print(f"   ❌ ERROR convirtiendo {m4a.name}")

    print("----")
    print("✅ Terminado.")


if __name__ == "__main__":
    main()
