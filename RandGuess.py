import random

numero_aleatorio = random.randint(1, 100)
intentos = 0
win = False

print("¡Bienvenido al juego de adivinar el número!")
print("Tienes 5 intentos para adivinar el número secreto entre 1 y 100.")

while intentos < 5:
    intento = int(input("Introduce tu número: "))
    intentos += 1

    if intento == numero_aleatorio:
        win = True

    elif intento < numero_aleatorio:
        print("El número secreto es mayor que el número que has introducido.")
        if abs(intento - numero_aleatorio) <= 10:
            print("¡Caliente!")
        else:
            print("¡Frío!")

    else:
        print("El número secreto es menor que el número que has introducido.")
        if abs(intento - numero_aleatorio) <= 10:
            print("¡Caliente!")
        else:
            print("¡Frío!")

if (win):
    print("¡Felicidades! ¡Has adivinado el número secreto!")
else:
    print("¡Has agotado tus intentos! El número secreto era:", numero_aleatorio)


