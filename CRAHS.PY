# PROGRAMA DOBLE ROJO
# PROGRAMA DOBLE ROJO
# PROGRAMA DOBLE ROJO

import random

# Define los números de la ruleta
numeros = list(range(37))

# Define los colores de los números
colores = {
    0: "verde",
    1: "rojo",
    2: "negro",
    3: "rojo",
    4: "negro",
    5: "rojo",
    6: "negro",
    7: "rojo",
    8: "negro",
    9: "rojo",
    10: "negro",
    11: "negro",
    12: "rojo",
    13: "negro",
    14: "rojo",
    15: "negro",
    16: "rojo",
    17: "negro",
    18: "rojo",
    19: "negro",
    20: "rojo",
    21: "negro",
    22: "rojo",
    23: "negro",
    24: "rojo",
    25: "negro",
    26: "rojo",
    27: "negro",
    28: "rojo",
    29: "negro",
    30: "rojo",
    31: "negro",
    32: "rojo",
    33: "negro",
    34: "rojo",
    35: "negro",
    36: "rojo",
}


def tirar_ruleta():

    numero = random.choice(numeros)
    return numero, colores[numero]

# Juega
def jugar(start):
  juegos_totales = 0
  rondas = 0
  ganancias = 0
  juegos_mpr = 0
  ronda_alta = 0
  ganancias_rel = 0

  # Jugar hasta perder
  while True:
    rondas += 1
    inversion = 0
    balance = 0
    juegos = 0
    bet = start

    # Jugar una ronda
    while balance <= 10:
      juegos += 1
      inversion += bet

      # Tira la ruleta
      numero, color = tirar_ruleta()
      if color == 'rojo':
        balance += bet
      else:
        balance -= bet

      bet *= 2

      if juegos > 30: break

    # print(f'Juegos: {juegos} Inversión: {inversion} Profit: {balance}')
    ganancias += balance
    juegos_totales += juegos
    if juegos > juegos_mpr:
      juegos_mpr = juegos
      ronda_alta = rondas
      ganancias_rel = ganancias

    if rondas == 10000000000000000:
      stopLoss = start*2**juegos_mpr
      print(f'\nJugaste {juegos_totales} veces en {rondas} rondas')
      print(f'Juegos máximos: {juegos_mpr} Stop loss: {stopLoss}')
      print(f'Ronda maxima: {ronda_alta} Ganancias relativas: {ganancias_rel}')
      print(f'\nProfit: {ganancias}')
      break

jugar(10)