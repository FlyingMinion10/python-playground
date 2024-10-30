import os
from PIL import Image

def agregar_fondo(ruta_imagen):
    # Abrir la imagen original
    imagen = Image.open(ruta_imagen)

    # Importa una imagen para ser fondo de la carpeta actual
    fondo = Image.open('fondo.png')
    

    # Pegar la imagen original en la nueva imagen
    fondo.paste(imagen, mask=imagen)

    # Guardar la nueva imagen
    nombre_imagen = os.path.basename(ruta_imagen)
    fondo.save(f'new/{nombre_imagen}')

# Obtener una lista de todas las imágenes en la carpeta
ruta_carpeta_imagenes = 'images'
imagenes = [f for f in os.listdir(ruta_carpeta_imagenes) if f.endswith('.png')]

# Llamar a la función para cada imagen
for imagen in imagenes:
    agregar_fondo(f'{ruta_carpeta_imagenes}/{imagen}')