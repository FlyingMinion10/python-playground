import numpy as np
import matplotlib.pyplot as plt

# Parámetros de entrada
velocidad_inicial = float(input("Introduce la velocidad inicial del meteorito (m/s): "))
masa_inicial = float(input("Introduce la masa inicial del meteorito (kg): "))

# Constantes
densidad_aire = 1.2  # kg/m^3, densidad del aire a nivel del mar
coef_friccion = 0.5  # Coeficiente de fricción aerodinámica
area_meteorito = 1.0  # m^2, área superficial del meteorito
gravedad = 9.81  # m/s^2, aceleración debido a la gravedad
dt = 0.01  # Intervalo de tiempo (s)
tiempo_total = 100  # Tiempo total de simulación (s)

# Inicialización de variables
velocidad = velocidad_inicial
masa = masa_inicial
tiempo = 0

# Listas para almacenar los resultados
tiempos = []
masas = []
velocidades = []

while masa > 0 and tiempo < tiempo_total:
    # Calcular la fuerza de fricción
    fuerza_friccion = 0.5 * densidad_aire * coef_friccion * area_meteorito * velocidad**2
    
    # Calcular la pérdida de masa debido a la fricción
    perdida_masa = fuerza_friccion * dt / (velocidad * 1e5)  # Factor de escala para simplificación
    
    # Actualizar masa y velocidad
    masa -= perdida_masa
    if masa < 0:  # Evitar que la masa sea negativa
        masa = 0
    
    # Actualizar velocidad considerando la pérdida de masa
    aceleracion = -fuerza_friccion / masa if masa > 0 else 0
    velocidad += aceleracion * dt
    
    # Actualizar tiempo
    tiempo += dt
    
    # Guardar los valores actuales
    tiempos.append(tiempo)
    masas.append(masa)
    velocidades.append(velocidad)

# Visualización de resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tiempos, masas, label="Masa (kg)")
plt.title("Desintegración del Meteorito")
plt.xlabel("Tiempo (s)")
plt.ylabel("Masa (kg)")
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(tiempos, velocidades, label="Velocidad (m/s)", color='red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

