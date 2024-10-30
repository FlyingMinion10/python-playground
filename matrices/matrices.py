def crear_matriz(filas, columnas):
    matriz = []
    for _ in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        print(' '.join(map(str, fila)))

def sumar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or any(len(f1) != len(f2) for f1, f2 in zip(matriz1, matriz2)):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")
    matriz_suma = []
    for i in range(len(matriz1)):
        fila_suma = []
        for j in range(len(matriz1[0])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila_suma.append(suma)
        matriz_suma.append(fila_suma)
    return matriz_suma

def restar_matrices(matriz1, matriz2):
    if len(matriz1) != len(matriz2) or any(len(f1) != len(f2) for f1, f2 in zip(matriz1, matriz2)):
        raise ValueError("Las matrices deben tener las mismas dimensiones.")
    matriz_resta = []
    for i in range(len(matriz1)):
        fila_resta = []
        for j in range(len(matriz1[0])):
            resta = matriz1[i][j] - matriz2[i][j]
            fila_resta.append(resta)
        matriz_resta.append(fila_resta)
    return matriz_resta

def multiplicar_escalar(matriz, escalar):
    matriz_producto = []
    for fila in matriz:
        fila_producto = [elemento * escalar for elemento in fila]
        matriz_producto.append(fila_producto)
    return matriz_producto

def buscar_elemento(matriz, elemento):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == elemento:
                return (i, j)
    return None

def transponer_matriz(matriz):
    if not matriz or not matriz[0]:
        return []
    filas = len(matriz)
    columnas = len(matriz[0])
    transpuesta = []
    for j in range(columnas):
        fila_transpuesta = []
        for i in range(filas):
            fila_transpuesta.append(matriz[i][j])
        transpuesta.append(fila_transpuesta)
    return transpuesta
