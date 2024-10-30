import random

def elegir_palabra():
    with open('palabras.txt', 'r') as file:
        palabras = file.read().splitlines()
    return random.choice(palabras)

def mostrar_ahorcado(intentos):
    etapas = ["""
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     / /
                  ---
                """,
                """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |     / 
                  ---
                """,
                """
                   --------
                   |      |
                   |      O
                   |    --|--
                   |      |
                   |      
                  ---
                """,
                """
                   --------
                   |      |
                   |      O
                   |    --|
                   |      |
                   |     
                  ---
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                """]
    return etapas[intentos]

def jugar():
    palabra = elegir_palabra()
    completado = "_" * len(palabra)
    adivinado = False
    letras_adivinadas = set()
    intentos = 6

    print("¡Vamos a jugar al Ahorcado!")
    print(mostrar_ahorcado(intentos))
    print(completado + "\n")
    
    while not adivinado and intentos > 0:
        adivinanza = input("Por favor, adivina una letra: ").lower()
        if len(adivinanza) == 1 and adivinanza.isalpha():
            if adivinanza in letras_adivinadas:
                print("Ya has adivinado la letra", adivinanza)
            elif adivinanza not in palabra:
                print(adivinanza, "no está en la palabra.")
                intentos -= 1
                letras_adivinadas.add(adivinanza)
            else:
                print("¡Buen trabajo,", adivinanza, "está en la palabra!")
                letras_adivinadas.add(adivinanza)
                palabra_como_lista = list(completado)
                indices = [i for i, letra in enumerate(palabra) if letra == adivinanza]
                for indice in indices:
                    palabra_como_lista[indice] = adivinanza
                completado = "".join(palabra_como_lista)
                if "_" not in completado:
                    adivinado = True
        else:
            print("Entrada no válida. Por favor, añade una única letra alfabética.")
        
        print(mostrar_ahorcado(intentos))
        print(completado + "\n")
        
    if adivinado:
        print("¡Felicidades, adivinaste la palabra! ¡Ganaste!")
    else:
        print("Lo siento, te has quedado sin intentos. La palabra era " + palabra + ". ¡Quizás la próxima vez!")

if __name__ == "__main__":
    jugar()
