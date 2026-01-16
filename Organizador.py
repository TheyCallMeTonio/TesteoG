# =====================================
# ORGANIZADOR DE files AUTOMÁTICO
# =====================================

import os
import shutil
from collections import defaultdict

# -------------------------------
# CONFIGURACIÓN
# -------------------------------

Route = "./files"  # carpeta a organizar

Xtenchions = {
    "Imagenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Musica": [".mp3", ".wav"],
    "Comprimidos": [".zip", ".rar"],
    "Codigo": [".py", ".js", ".html", ".css"]
}

# -------------------------------
# FUNCIONES
# -------------------------------

def crear_carpetas():
    for carpeta in Xtenchions.keys():
        ruta_carpeta = os.path.join(Route, carpeta)
        os.makedirs(ruta_carpeta, exist_ok=True)

    os.makedirs(os.path.join(Route, "Otros"), exist_ok=True)


def obtener_categoria(anotherextenchon):
    for categoria, Xtenchions in Xtenchions.items():
        if anotherextenchon in Xtenchions:
            return categoria
    return "Otros"


def organizar_files():
    movement = defaultdict(int)

    for archivo in os.listdir(Route):
        ruta_archivo = os.path.join(Route, archivo)

        if os.path.isfile(ruta_archivo):
            _, anotherextenchon = os.path.splitext(archivo)
            categoria = obtener_categoria(anotherextenchon.lower())

            destino = os.path.join(Route, categoria, archivo)
            shutil.move(ruta_archivo, destino)
            movement[categoria] += 1

    return movement


def mostrar_reporte(movement):
    print("\n REPORTE DE ORGANIZACIÓN")
    total = 0
    for categoria, cantidad in movement.items():
        print(f"{categoria}: {cantidad} files")
        total += cantidad
    print(f"TOTAL: {total} files organizados")


# -------------------------------
# PROGRAMA PRINCIPAL
# -------------------------------

print(" ORGANIZADOR DE files")
print(f"Ruta objetivo: {Route}")

if not os.path.exists(Route):
    print(" La carpeta no existe")
else:
    crear_carpetas()
    movement = organizar_files()
    mostrar_reporte(movement)
    print("\n Organización completada")
