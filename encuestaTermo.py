import random
import pandas as pd

# Opciones para cada pregunta del formulario
opciones_funcion = [
    "Ver la temperatura",
    "Ver la capacidad",
    "Qué se caliente",
    "GPS",
    "Recordatorio para tomar agua",
    "Other"  # Se usará para asignar una respuesta personalizada
]

# Opciones personalizadas para el caso "Other"
otras_opciones = [
    "Conexión Bluetooth",
    "Aplicación móvil integrada",
    "Notificaciones inteligentes",
    "Recordatorio de calentamiento personalizado"
]

opciones_precio = [
    "$300 - $700",
    "$700 - $1200",
    "+ $1200"
]

opciones_edad = [
    "-18",
    "18-24",
    "24-30",
    "+30"
]

opciones_genero = [
    "Hombre",
    "Mujer"
]

# Número de respuestas a generar (puedes modificar este valor)
num_respuestas = 100

# Lista para almacenar cada respuesta
datos = []

for i in range(num_respuestas):
    # Seleccionar aleatoriamente la función del termo
    funcion = random.choice(opciones_funcion)
    if funcion == "Other":
        # Si se elige "Other", se selecciona una opción personalizada
        funcion = random.choice(otras_opciones)
    
    precio = random.choice(opciones_precio)
    edad = random.choice(opciones_edad)
    genero = random.choice(opciones_genero)
    
    # Agregar la respuesta simulada al conjunto de datos
    datos.append({
        "ID": i + 1,
        "Funcion_Termo": funcion,
        "Rango_Precio": precio,
        "Edad": edad,
        "Genero": genero
    })

# Crear un DataFrame de pandas y exportarlo a CSV
df = pd.DataFrame(datos)
df.to_csv("encuesta_termo.csv", index=False, encoding="utf-8-sig")

print("Base de datos generada: 'encuesta_termo.csv'")
 