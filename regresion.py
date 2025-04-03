import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Dx = np.array([0.37, 0.53, 0.72, 0.88, 1.07, 1.12, 1.29, 1.36, 1.41, 1.49])  # Tiempo en segundos
f = np.array([0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5])  # Posición en metros
x = np.linspace(0, 1, 100)

print(Dx)
print(f)

# Modelo de regresion A = (mean(x.*y) - mean(x)*mean(y))/(mean(x.^2) - mean(x)^2);
def regresion_lineal(x, y):
    return (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)


def regresion_lineal2(x, y):
    return (np.mean(x * y) - np.mean(x) * np.mean(y)) / (np.mean(x ** 2) - np.mean(x) ** 2)

# Plot the data
plt.scatter(Dx, f, color='red')
plt.plot(x, regresion_lineal(Dx, f) * x , color='blue')
plt.title('Dx vs f')
plt.xlabel('Dx')
plt.ylabel('f')
plt.show()
