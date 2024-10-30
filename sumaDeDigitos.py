def suma_digitos(numero):
    suma = 0
    while numero > 0:
        digito = numero % 10
        suma += digito
        numero //= 10
    return suma


numero = float(input("Ingresa un número entero positivo: "))
while (numero < 0) or (numero % 1 != 0) :
    print("\nPor favor, ingresa un número natural valido.")
    numero = float(input("Ingresa un número entero positivo: "))


resultado = suma_digitos(numero)
numero = int(numero)
resultado = int(resultado)
print(f"La suma de los dígitos de {numero}, es: {resultado}")
