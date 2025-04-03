import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Obtener las credenciales de las variables de entorno
SCRATCH_USERNAME = "FlyON10"
SCRATCH_PASSWORD = "scratch2025"

if not SCRATCH_USERNAME or not SCRATCH_PASSWORD:
    raise Exception("Por favor, configura las variables de entorno SCRATCH_USERNAME y SCRATCH_PASSWORD.")

# Configurar las opciones de Safari
options = webdriver.SafariOptions()
options.ignore_protected_mode_settings = True  # Configuración específica si es necesario

# Iniciar el navegador Safari
driver = webdriver.Safari(options=options)

try:
    # Navegar a la página de inicio de sesión de Scratch
    driver.get('https://scratch.mit.edu/login')
    time.sleep(5)  # Espera a que la página cargue

    # Encontrar los campos de usuario y contraseña
    username_field = driver.find_element(By.ID, 'id_username')
    password_field = driver.find_element(By.ID, 'id_password')

    # Ingresar las credenciales
    username_field.send_keys(SCRATCH_USERNAME)
    password_field.send_keys(SCRATCH_PASSWORD)
    password_field.send_keys(Keys.RETURN)
    time.sleep(3)  # Espera a que inicie sesión

    # Verificar si el inicio de sesión fue exitoso
    if "scratch.mit.edu" not in driver.current_url:
        print("Inicio de sesión fallido. Verifica tus credenciales.")
        driver.quit()
        exit()

    print("Inicio de sesión exitoso.")

    # Ruta de la carpeta con los archivos .sb3
    carpeta = '/Users/juanfelipezepeda/Downloads/scratch-templates'  # Reemplaza con la ruta real

    # Iterar sobre cada archivo .sb3 en la carpeta
    for archivo in os.listdir(carpeta):
        if archivo.endswith('.sb3'):
            ruta_archivo = os.path.join(carpeta, archivo)
            print(f'Subiendo el proyecto: {archivo}')

            # Navegar a la página de creación de proyectos
            driver.get('https://scratch.mit.edu/projects/editor/')
            time.sleep(5)  # Espera a que cargue el editor

            # Subir el archivo .sb3
            # Buscar el botón de "Archivo" y seleccionar "Importar desde tu computadora"
            # La interfaz de Scratch puede cambiar, así que asegúrate de verificar los selectores

            try:
                # Haz clic en el menú "Archivo"
                archivo_menu = driver.find_element(By.XPATH, "//div[contains(@class, 'menu-bar_menu-bar-item_NKeCD menu-bar_hoverable_l9SvC')]/span[text()='Archivo']")
                archivo_menu.click()
                time.sleep(5)

                # Haz clic en "Cargar desde tu computadora"
                cargar_archivo = driver.find_element(By.XPATH, "//li[text()='Subir desde tu computador']")
                cargar_archivo.click()
                time.sleep(5)

                # Enviar el archivo al input de carga
                upload_input = driver.find_element(By.XPATH, '//input[@type="file"]')
                upload_input.send_keys(ruta_archivo)
                print(f'Archivo {archivo} seleccionado para subir.')
                time.sleep(10)  # Espera a que se procese la carga

                # Publicar el proyecto
                # Dependiendo de la interfaz, puede que necesites hacer clic en "Guardar" y luego en "Publicar"
                # Aquí un ejemplo genérico:

                # Haz clic en "Guardar ahora"
                guardar_button = driver.find_element(By.XPATH, '//button[contains(text(), "Guardar ahora")]')
                guardar_button.click()
                time.sleep(3)

                # Haz clic en "Publicar" en la ventana emergente
                publicar_button = driver.find_element(By.XPATH, '//button[contains(text(), "Publicar")]')
                publicar_button.click()
                time.sleep(5)

                print(f'Proyecto {archivo} subido y publicado exitosamente.')

            except Exception as e:
                print(f'Error al subir el proyecto {archivo}: {e}')
                continue

    print("Todos los proyectos han sido procesados.")

finally:
    # Cerrar el navegador
    driver.quit()
