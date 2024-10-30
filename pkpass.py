import os
import zipfile

def create_pkpass_from_folder(pass_dir, output_path):
    # Crear el archivo .pkpass como un archivo ZIP
    with zipfile.ZipFile(output_path, 'w') as zf:
        # Recorrer todos los archivos en la carpeta y añadirlos al ZIP
        for file_name in os.listdir(pass_dir):
            file_path = os.path.join(pass_dir, file_name)
            if os.path.isfile(file_path):
                zf.write(file_path, file_name)

    print(f"Archivo .pkpass creado en: {output_path}")

if __name__ == "__main__":
    pass_dir = "/Users/juanfelipezepeda/Downloads/pass"  # Reemplaza con la ruta a tu carpeta
    output_path = "/Users/juanfelipezepeda/Downloads/pass.pkpass"  # Reemplaza con la ruta donde deseas guardar el archivo .pkpass

    create_pkpass_from_folder(pass_dir, output_path)
