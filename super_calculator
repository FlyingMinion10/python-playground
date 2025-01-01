import math
import numpy as np
import matplotlib.pyplot as plt

def caida_libre():
    print("Ingresa los datos conocidos (Presiona enter si no lo sabes)")

    # Pedimos al usuario que introduzca los datos
    v0 = input("Velocidad inicial (v0) [m/s]: ")
    vf = input("Velocidad final (vf) [m/s]: ")
    a = input("Gravedad (a) [m/s^2]: ")
    s = input("Distancia (d) [m]: ")
    t = input("Tiempo (t) [s]: ")
    print()

    # Convertimos los valores que no son 'x' a float
    v0 = float(v0) if (v0 != '' and v0 != ' ') else 'x'
    vf = float(vf) if (vf != '' and vf != ' ') else 'x'
    a = -9.8 if a == '-' else 9.8
    s = float(s) if (s != '' and s != ' ') else 'x'
    t = float(t) if (t != '' and t != ' ') else 'x'


    for i in range(2):
      # Ahora, usamos las fórmulas del MRUA para despejar los valores desconocidos


      # Velocidad final con la 1ra formula
      if vf == 'x' and v0 != 'x' and a != 'x' and t != 'x':
          vf = v0 + a*t
          print('Formula 1 usada (vf)')

      # Tiempo con la 1ra formula
      if t == 'x' and v0 != 'x' and a != 'x' and vf != 'x':
          t = (vf - v0) / a
          print('Formula 1 usada (t)')

      # Distancia con la 2da formula
      if s == 'x' and v0 != 'x' and a != 'x' and t != 'x':
          s = v0*t + 0.5*a*t**2
          print('Formula 2 usada (d)')

      # Velocidaded con la 3ra formula
      if vf == 'x' and v0 != 'x' and a != 'x' and s != 'x':
          vf = (v0**2 + 2*a*s)**0.5
          print('Formula 3 usada (vf)')

      elif v0 == 'x' and vf != 'x' and a != 'x' and s != 'x':
          v0 = (vf**2 - 2*a*s)**0.5
          print('Formula 3 usada (v0)')

      # Distancia con formula de velocidad
      if s == 'x' and v0 != 'x' and vf != 'x' and t != 'x':
          s = ((vf + v0) / 2)*t
          print('Formula velocidad (d)')

      # Velocidad inicial con la 1ra formula
      if s == 'x' and v0 == 'x' and vf != 'x' and t != 'x':
          v0 = -(a*t-vf)
          print("Formula 1 usada")


    # Si hay algún valor que no se pudo calcular, se imprime 'Indeterminado'
    if vf == 'x' or v0 == 'x' or a == 'x' or s == 'x' or t == 'x':
        print("\nNo se pudieron calcular todos los valores con los datos proporcionados.")
        v0 = v0 if v0 != 'x' else "Indeterminado"
        vf = vf if vf != 'x' else "Indeterminado"
        a = a if a != 'x' else "Indeterminado"
        s = s if s != 'x' else "Indeterminado"
        t = t if t != 'x' else "Indeterminado"

    # Mostramos los resultados
    print(f"\nVelocidad inicial (v0): {v0} m/s")
    print(f"Velocidad final (vf): {vf} m/s")
    print(f"Aceleración (a): {a} m/s^2")
    print(f"Distancia (d): {s} m")
    print(f"Tiempo (t): {t} s")


def scientific_calculator():
    print("Calculadora Científica Básica")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Logaritmo base 10")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")

    option = int(input("Opción: "))

    if option == 1:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 + num2
        print(f"El resultado de la suma es: {result}")

    elif option == 2:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 - num2
        print(f"El resultado de la resta es: {result}")

    elif option == 3:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 * num2
        print(f"El resultado de la multiplicación es: {result}")

    elif option == 4:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        if num2 == 0:
            print("Error: División por cero.")
        else:
            result = num1 / num2
            print(f"El resultado de la división es: {result}")

    elif option == 5:
        base = float(input("Introduce la base: "))
        exp = float(input("Introduce el exponente: "))
        result = math.pow(base, exp)
        print(f"El resultado de {base} elevado a la {exp} es: {result}")

    elif option == 6:
        num = float(input("Introduce el número: "))
        if num < 0:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        else:
            result = math.sqrt(num)
            print(f"La raíz cuadrada de {num} es: {result}")

    elif option == 7:
        num = float(input("Introduce el número: "))
        if num <= 0:
            print("Error: El logaritmo de un número menor o igual a 0 no está definido.")
        else:
            result = math.log10(num)
            print(f"El logaritmo base 10 de {num} es: {result}")

    elif option == 8:
        angle = float(input("Introduce el ángulo en grados: "))
        result = math.sin(math.radians(angle))
        print(f"El seno de {angle} grados es: {result}")

    elif option == 9:
        angle = float(input("Introduce el ángulo en grados: "))
        result = math.cos(math.radians(angle))
        print(f"El coseno de {angle} grados es: {result}")

    elif option == 10:
        angle = float(input("Introduce el ángulo en grados: "))
        result = math.tan(math.radians(angle))
        print(f"La tangente de {angle} grados es: {result}")

    else:
        print("Opción no válida.")

def basic_calculator():
    print("Calculadora Básica")
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    option = int(input("Opción: "))

    if option == 1:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 + num2
        print(f"El resultado de la suma es: {result}")

    elif option == 2:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 - num2
        print(f"El resultado de la resta es: {result}")

    elif option == 3:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        result = num1 * num2
        print(f"El resultado de la multiplicación es: {result}")

    elif option == 4:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        if num2 == 0:
            print("Error: División por cero.")
        else:
            result = num1 / num2
            print(f"El resultado de la división es: {result}")
    else:
        print("Opción no válida.")

def tiro_de_proyectil():

    print("Ingresa los datos del tiro de proyectil")
    print("Presiona enter si no lo sabes\n")

    v0 = input("Velocidad inicial (v0) [m/s]: ")
    theta = input("Aceleración (a) [m/s^2]: ")

    vox = v0 * math.cos(math.radians(theta))
    voy = v0 * math.sin(math.radians(theta))
    g = -9.8

    print(f"\nVelocidad inicial en x (vox): {vox} m/s")
    print(f"Velocidad inicial en y (voy): {voy} m/s")

    altura_max = voy**2 / (2*abs(g))
    tiempo = 2 * voy / abs(g)
    distancia = v0**2 * math.sin(2*math.radians(theta)) / g

    print(f"Altura máxima alcanzada: {altura_max} m")
    print(f"Tiempo de vuelo: {tiempo} s")
    print(f"Distancia recorrida: {distancia} m")

def formula_general():
    print("Despeje de ecuación cuadratica")
    print("Ingresa los datos de la ecuación")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    discriminante = b**2 - 4*a*c
    raiz = math.sqrt(discriminante)

    x1 = (-b + raiz) / (2*a)
    x2 = (-b - raiz) / (2*a)

    print(f"x1 = {x1}")
    print(f"x2 = {x2}")

def pitagoras():
    print("Teorema de Pitágoras")
    print("Ingresa los datos (si no lo sabes oprime Enter)")

    a = float(input("a: "))
    b = float(input("b: "))
    c = float(input("c: "))

    a = float(a) if (a != '' and a != ' ') else 'x'
    b = float(b) if (b != '' and b != ' ') else 'x'
    c = float(c) if (c != '' and c != ' ') else 'x'


    if a == 'x':
        a = math.sqrt(c**2 - b**2)
        print(f"a = {a}")

    elif b == 'x':
        b = math.sqrt(c**2 - a**2)
        print(f"b = {b}")

    elif c == 'x':
        c = math.sqrt(a**2 + b**2)
        print(f"c = {c}")

def graficadora_funciones():
    while True:
        print("\nGraficadora de funciones")
        print("Selecciona una función:")
        print("1. Función Trigonométrica (Seno)")
        print("2. Función Exponencial")
        print("3. Función Logaritmo")
        print("4. Función Elíptica")
        print("0. Salir")

        try:
            option = int(input("Opción: "))
        except ValueError:
            print("Por favor, introduce un número válido.")
            continue

        if option == 0:
            print("Saliendo...")
            break
        elif option == 1:
            funcion_trigonometrica()
        elif option == 2:
            funcion_exponencial()
        elif option == 3:
            funcion_logaritmo()
        elif option == 4:
            funcion_eliptica()
        else:
            print("Opción no válida. Inténtalo de nuevo.")

def funcion_trigonometrica():
    try:
        min_x = float(input("Introduce el valor mínimo de x (en radianes): "))
        max_x = float(input("Introduce el valor máximo de x (en radianes): "))
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
        return

    x = np.linspace(min_x, max_x, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.title(f"Función Seno desde {min_x} hasta {max_x}")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)
    plt.show()

def funcion_exponencial():
    try:
        min_x = float(input("Introduce el valor mínimo de x: "))
        max_x = float(input("Introduce el valor máximo de x: "))
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
        return

    x = np.linspace(min_x, max_x, 100)
    y = np.exp(x)
    plt.plot(x, y)
    plt.title(f"Función Exponencial desde {min_x} hasta {max_x}")
    plt.xlabel("x")
    plt.ylabel("exp(x)")
    plt.grid(True)
    plt.show()

def funcion_logaritmo():
    try:
        min_x = float(input("Introduce el valor mínimo de x (mayor a 0): "))
        max_x = float(input("Introduce el valor máximo de x: "))
        if min_x <= 0:
            raise ValueError("El valor mínimo de x debe ser mayor a 0.")
    except ValueError as e:
        print(f"Error: {e}")
        return

    x = np.linspace(min_x, max_x, 100)
    y = np.log(x)
    plt.plot(x, y)
    plt.title(f"Función Logaritmo Natural desde {min_x} hasta {max_x}")
    plt.xlabel("x")
    plt.ylabel("log(x)")
    plt.grid(True)
    plt.show()

def funcion_eliptica():
    try:
        a = float(input("Introduce el valor de a (radio mayor): "))
        b = float(input("Introduce el valor de b (radio menor): "))
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")
        return

    theta = np.linspace(0, 2 * np.pi, 100)
    x = a * np.cos(theta)
    y = b * np.sin(theta)
    plt.plot(x, y)
    plt.title(f"Función Elíptica con a={a} y b={b}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

# Llamar a la función principal
def main():
    print("Bienvenido a la calculadora científica")
    print("Selecciona una opción:")
    print("1. Cálculo Científico")
    print("2. Cálculo Básico")
    print("3. Tiro de Proyectil")
    print("4. Caída Libre")
    print("5. Despeje de ecuación cuadrática")
    print("6. Teorema de Pitágoras")
    print("7. Graficadora de funciones")
    print("0. Salir")

    option = int(input("Opción: "))

    if option == 1:
        scientific_calculator()
    elif option == 2:
        basic_calculator()
    elif option == 3:
        tiro_de_proyectil()
    elif option == 4:
        caida_libre()
    elif option == 5:
        formula_general()
    elif option == 6:
        pitagoras()
    elif option == 7:
        graficadora_funciones()
    elif option == 0:
        print("¡Hasta luego!")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
