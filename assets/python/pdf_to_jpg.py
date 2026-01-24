import os
import sys
import fitz  # PyMuPDF

def pdf_to_jpg_and_delete(pdf_path, dpi=150):
    # Validación básica
    if not os.path.isfile(pdf_path):
        raise FileNotFoundError(f"No existe el fichero: {pdf_path}")

    if not pdf_path.lower().endswith(".pdf"):
        raise ValueError("El fichero no es un PDF")

    folder = os.path.dirname(pdf_path)
    if folder == "":
        folder = "."

    # Conversión
    # Abrir el PDF
    pdf_document = fitz.open(pdf_path)
    
    # Calcular zoom para el DPI deseado (72 es el DPI por defecto)
    zoom = dpi / 72
    mat = fitz.Matrix(zoom, zoom)
    
    # Convertir cada página a imagen
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap(matrix=mat)
        
        output_path = os.path.join(folder, f"img_{page_num + 1}.jpg")
        pix.save(output_path, "jpeg", jpg_quality=75)
    
    pdf_document.close()

    # Borrado del PDF original
    os.remove(pdf_path)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python pdf_to_jpg.py <ruta_pdf>")
        sys.exit(1)

    pdf_path = sys.argv[1]
    pdf_to_jpg_and_delete(pdf_path)
