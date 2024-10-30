# # Crea un codigi de 64 bits a partir de una imagen
# # """

# import base64
# from PIL import Image
# import pyperclip

# def image_to_base64(image_path):
#     try:
#         with open(image_path, "rb") as image_file:
#             encoded_string = base64.b64encode(image_file.read())
#     except FileNotFoundError:
#         print("Error: Image file not found.")
#     except Exception as e:
#         print(f"Error: {str(e)}")
#     else:
#         print("Image encoded successfully.")
#     return encoded_string

# def base64_to_image(encoded_string, output_path):
#     decoded_string = base64.b64decode(encoded_string)
#     with open(output_path, "wb") as output_file:
#         output_file.write(decoded_string)

# image_path = "assets/etiqueta.jpg"
# encoded_string = image_to_base64(image_path)

# # # Copiar el string codificado al portapapeles
# # pyperclip.copy(encoded_string)

# # Crea una url para enviar la imagen a un endpoint
# url = "https://my-backend-production.up.railway.app/api/openai/weight/get"
# full_url = f"{url}?image={encoded_string}"

# # Copia la url al portapapeles
# pyperclip.copy(full_url)

import base64
import json
import requests

def send_image_to_api(image_path, completion):
    try:
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
    except FileNotFoundError:
        print("Error: Image file not found.")
        return
    except Exception as e:
        print(f"Error: {str(e)}")
        return

    base64_image = base64.b64encode(image_data).decode('utf-8')
    url = "https://my-backend-production.up.railway.app/api/openai/weight/get"
    headers = {"Content-Type": "application/json"}
    payload = json.dumps({"image": "data:image/jpeg;base64,"+base64_image})

    # Depuración: Imprimir la URL, los encabezados y el payload
    print(f"Headers: {headers}")
    print(f"URL: {url}")
    print(f"Payload: {payload[:50]}...")  # Mostrar solo los primeros 20 caracteres del payload

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()
        json_response = response.json()
        weight = json_response.get("weight")
        if weight:
            completion(weight)
        else:
            print("Error: 'weight' not found in response.")
    except requests.exceptions.RequestException as e:
        print(f"Error sending request: {str(e)}")
        print(f"Response content: {e.response.content}")
    except json.JSONDecodeError as e:
        print(f"Error parsing response: {str(e)}")

# Ejemplo de uso
def completion(weight):
    print(f"Weight: {weight}")

image_path = "assets/etiqueta.jpg"
send_image_to_api(image_path, completion)