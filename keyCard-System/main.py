import random
from dataBase import insertUser, checkToken

print("SISTEMA DE REGISTRO DE LLAVES DE PASO")
option = None
keyDictionary = {}

def newKeyList():
    keyList = []
    for i in range(0, 10):
        key = random.randint(10000000, 99999999)
        keyList.append(key)
    print("Llaves registradas: ", keyList)
    return keyList


while option != 0:
    print("1. Ver opciones \n0. Salir")
    option = int(input("Opción: "))
    if option == 0:
        break

    print("\nQué desea hacer? \n1. Registrar llave \n2. Usar llave \n3. Ver llaves registradas \n0. Salir")
    option = int(input("Opción: "))
    if option == 1:
        name = input("Ingrese su nombre completo: ")
        keyList = newKeyList()
        keyDictionary[name] = keyList
        insertUser(name, keyList, keyList)
    elif option == 2:
        user = (input("Ingrese su nombre: "))
        currentKeys = keyDictionary[user]
        inputKey = int(input("Ingrese la llave de paso: "))
        if inputKey == currentKeys[0]:
            print("Llave correcta")
            keyDictionary[user].pop(0)
            print(keyDictionary[user])
        else:
            print("Llave incorrecta")
    elif option == 3:
        for key in keyDictionary:
            print(key, keyDictionary[key])
