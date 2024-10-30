"""

crear_matriz(filas, columnas)
    Entradas:
    filas: Número entero que representa la cantidad de filas de la matriz.
    columnas: Número entero que representa la cantidad de columnas de la matriz.
    Salidas:
    matriz: Una matriz (lista de listas) vacía con las dimensiones especificadas.
    Proceso/Cálculos:
    Crear una lista vacía para representar la matriz.
    Utilizar bucles anidados para inicializar cada elemento de la matriz a cero.
    Algoritmo:
    Inicializar una lista vacía llamada matriz.
    Para cada número de fila en el rango de filas:
    Crear una lista llamada fila con columnas ceros.
    Añadir fila a matriz.
    Devolver matriz.
    Casos de prueba:
    crear_matriz(2, 3) debería retornar [[0, 0, 0], [0, 0, 0]].
    crear_matriz(0, 0) debería retornar [].

imprimir_matriz(matriz)
    Entradas:
    matriz: Una matriz (lista de listas) que se desea imprimir.
    Salidas:
    Ninguna (imprime en la consola).
    Proceso/Cálculos:
    Recorrer cada fila de la matriz y imprimir sus elementos separados por espacios.
    Algoritmo:
    Para cada fila en matriz:
    Convertir los elementos de fila a cadenas y unirlos con espacios.
    Imprimir la cadena resultante.
    Casos de prueba:
    imprimir_matriz([[1, 2, 3], [4, 5, 6]]) debería imprimir:
    Copiar código
    1 2 3
    4 5 6
    imprimir_matriz([]) no debería imprimir nada o indicar que la matriz está vacía.

sumar_matrices(matriz1, matriz2)
    Entradas:
    matriz1: Primera matriz (lista de listas).
    matriz2: Segunda matriz (lista de listas).
    Salidas:
    matriz_suma: Nueva matriz resultante de la suma de matriz1 y matriz2.
    Proceso/Cálculos:
    Verificar que las dimensiones de ambas matrices sean iguales.
    Sumar elemento a elemento las matrices.
    Algoritmo:
    Verificar que el número de filas y columnas de matriz1 y matriz2 sean iguales.
    Si no lo son, lanzar un error.
    Inicializar una matriz vacía matriz_suma.
    Para cada índice de fila i:
    Inicializar una lista vacía fila_suma.
    Para cada índice de columna j:
    Calcular la suma de matriz1[i][j] y matriz2[i][j].
    Añadir el resultado a fila_suma.
    Añadir fila_suma a matriz_suma.
    Devolver matriz_suma.
    Casos de prueba:
    sumar_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]]) debería retornar [[6, 8], [10, 12]].
    sumar_matrices([[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]) debería retornar [[8, 10, 12], [14, 16, 18]].

restar_matrices(matriz1, matriz2)
    Entradas:
    matriz1: Primera matriz (lista de listas).
    matriz2: Segunda matriz (lista de listas).
    Salidas:
    matriz_resta: Nueva matriz resultante de la resta de matriz1 y matriz2.
    Proceso/Cálculos:
    Verificar que las dimensiones de ambas matrices sean iguales.
    Restar elemento a elemento las matrices.
    Algoritmo:
    Verificar que el número de filas y columnas de matriz1 y matriz2 sean iguales.
    Si no lo son, lanzar un error.
    Inicializar una matriz vacía matriz_resta.
    Para cada índice de fila i:
    Inicializar una lista vacía fila_resta.
    Para cada índice de columna j:
    Calcular la resta de matriz1[i][j] menos matriz2[i][j].
    Añadir el resultado a fila_resta.
    Añadir fila_resta a matriz_resta.
    Devolver matriz_resta.
    Casos de prueba:
    restar_matrices([[5, 7], [9, 11]], [[1, 2], [3, 4]]) debería retornar [[4, 5], [6, 7]].
    restar_matrices([[10, 20, 30], [40, 50, 60]], [[5, 10, 15], [20, 25, 30]]) debería retornar [[5, 10, 15], [20, 25, 30]].

multiplicar_escalar(matriz, escalar)
    Entradas:
    matriz: Una matriz (lista de listas).
    escalar: Número que se multiplicará por cada elemento de la matriz.
    Salidas:
    matriz_producto: Nueva matriz resultante de multiplicar cada elemento de matriz por escalar.
    Proceso/Cálculos:
    Multiplicar cada elemento de la matriz por el escalar dado.
    Algoritmo:
    Inicializar una matriz vacía matriz_producto.
    Para cada índice de fila i:
    Inicializar una lista vacía fila_producto.
    Para cada índice de columna j:
    Multiplicar matriz[i][j] por escalar.
    Añadir el resultado a fila_producto.
    Añadir fila_producto a matriz_producto.
    Devolver matriz_producto.
    Casos de prueba:
    multiplicar_escalar([[1, 2], [3, 4]], 2) debería retornar [[2, 4], [6, 8]].
    multiplicar_escalar([[0, -1], [-2, -3]], -1) debería retornar [[0, 1], [2, 3]].
    
buscar_elemento(matriz, elemento)
    Entradas:
    matriz: Una matriz (lista de listas).
    elemento: Valor a buscar dentro de la matriz.
    Salidas:
    Una tupla (fila, columna) con la posición del elemento, o None si no se encuentra.
    Proceso/Cálculos:
    Recorrer la matriz y comparar cada elemento con el valor buscado.
    Algoritmo:
    Para cada índice de fila i:
    Para cada índice de columna j:
    Si matriz[i][j] es igual a elemento:
    Devolver (i, j).
    Si no se encuentra el elemento, devolver None.
    Casos de prueba:
    buscar_elemento([[1, 2], [3, 4]], 3) debería retornar (1, 0).
    buscar_elemento([[5, 6], [7, 8]], 10) debería retornar None.

transponer_matriz(matriz)
    Entradas:
    matriz: Una matriz (lista de listas).
    Salidas:
    transpuesta: Nueva matriz transpuesta de la original.
    Proceso/Cálculos:
    Intercambiar filas por columnas.
    Algoritmo:
    Verificar si la matriz no está vacía.
    Obtener el número de filas y columnas de la matriz original.
    Inicializar una matriz vacía transpuesta con dimensiones invertidas.
    Para cada índice de columna j:
    Inicializar una lista vacía fila_transpuesta.
    Para cada índice de fila i:
    Añadir matriz[i][j] a fila_transpuesta.
    Añadir fila_transpuesta a transpuesta.
    Devolver transpuesta.
    Casos de prueba:
    transponer_matriz([[1, 2], [3, 4]]) debería retornar [[1, 3], [2, 4]].
    transponer_matriz([[1, 2, 3], [4, 5, 6]]) debería retornar [[1, 4], [2, 5], [3, 6]].
"""

from matrices import (
    crear_matriz,
    imprimir_matriz,
    sumar_matrices,
    restar_matrices,
    multiplicar_escalar,
    buscar_elemento,
    transponer_matriz
)

def mostrar_menu():
    print("\nSeleccione una opción:")
    print("1. Crear matriz")
    print("2. Imprimir matriz")
    print("3. Sumar matrices")
    print("4. Restar matrices")
    print("5. Multiplicar matriz por escalar")
    print("6. Buscar elemento en matriz")
    print("7. Transponer matriz")
    print("8. Salir")

def leer_matriz():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el elemento en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def ejecutar_programa():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            matriz = leer_matriz()
            print("Matriz creada:")
            imprimir_matriz(matriz)
        elif opcion == '2':
            if 'matriz' in locals():
                print("Imprimiendo la matriz:")
                imprimir_matriz(matriz)
            else:
                print("No hay una matriz cargada. Cree una matriz primero.")
        elif opcion == '3':
            print("Sumar matrices:")
            print("Primera matriz:")
            matriz1 = leer_matriz()
            print("Segunda matriz:")
            matriz2 = leer_matriz()
            try:
                matriz_suma = sumar_matrices(matriz1, matriz2)
                print("Resultado de la suma:")
                imprimir_matriz(matriz_suma)
            except ValueError as e:
                print(e)
        elif opcion == '4':
            print("Restar matrices:")
            print("Primera matriz:")
            matriz1 = leer_matriz()
            print("Segunda matriz:")
            matriz2 = leer_matriz()
            try:
                matriz_resta = restar_matrices(matriz1, matriz2)
                print("Resultado de la resta:")
                imprimir_matriz(matriz_resta)
            except ValueError as e:
                print(e)
        elif opcion == '5':
            print("Multiplicar matriz por escalar:")
            matriz = leer_matriz()
            escalar = float(input("Ingrese el escalar: "))
            matriz_producto = multiplicar_escalar(matriz, escalar)
            print("Resultado de la multiplicación:")
            imprimir_matriz(matriz_producto)
        elif opcion == '6':
            if 'matriz' in locals():
                elemento = float(input("Ingrese el elemento a buscar: "))
                posicion = buscar_elemento(matriz, elemento)
                if posicion:
                    print(f"Elemento encontrado en la posición {posicion}")
                else:
                    print("Elemento no encontrado.")
            else:
                print("No hay una matriz cargada. Cree una matriz primero.")
        elif opcion == '7':
            print("Transponer matriz:")
            matriz = leer_matriz()
            matriz_transpuesta = transponer_matriz(matriz)
            print("Matriz transpuesta:")
            imprimir_matriz(matriz_transpuesta)
        elif opcion == '8':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida.")

# Ejecutar el programa principal
if __name__ == "__main__":
    ejecutar_programa()


"""
Seleccione una opción:
1. Crear matriz
2. Imprimir matriz
3. Sumar matrices
4. Restar matrices
5. Multiplicar matriz por escalar
6. Buscar elemento en matriz
7. Transponer matriz
8. Salir
Ingrese una opción: 5
Multiplicar matriz por escalar:
Ingrese el número de filas: 2
Ingrese el número de columnas: 2
Ingrese el elemento en la posición (0, 0): 1
Ingrese el elemento en la posición (0, 1): 2
Ingrese el elemento en la posición (1, 0): 3
Ingrese el elemento en la posición (1, 1): 4
Ingrese el escalar: 5
Resultado de la multiplicación:
5.0 10.0
15.0 20.0

Seleccione una opción:
1. Crear matriz
2. Imprimir matriz
3. Sumar matrices
4. Restar matrices
5. Multiplicar matriz por escalar
6. Buscar elemento en matriz
7. Transponer matriz
8. Salir
Ingrese una opción: 7
Transponer matriz:
Ingrese el número de filas: 2
Ingrese el número de columnas: 3
Ingrese el elemento en la posición (0, 0): 1
Ingrese el elemento en la posición (0, 1): 2
Ingrese el elemento en la posición (0, 2): 3
Ingrese el elemento en la posición (1, 0): 4
Ingrese el elemento en la posición (1, 1): 5
Ingrese el elemento en la posición (1, 2): 6
Matriz transpuesta:
1.0 4.0
2.0 5.0
3.0 6.0

Seleccione una opción:
1. Crear matriz
2. Imprimir matriz
3. Sumar matrices
4. Restar matrices
5. Multiplicar matriz por escalar
6. Buscar elemento en matriz
7. Transponer matriz
8. Salir
Ingrese una opción: 8
Saliendo del programa.
"""