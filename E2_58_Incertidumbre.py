import numpy as np
import matplotlib.pyplot as plt

# Posición real del robot
x_real = 10

# Desviación estándar de la incertidumbre en la medición de la posición
std_dev = 0.5

# Generar mediciones simuladas con ruido (incertidumbre)
num_measurements = 1000
measurements = np.random.normal(x_real, std_dev, num_measurements)

# Histograma de las mediciones simuladas
plt.figure(figsize=(8, 6))
plt.hist(measurements, bins=30, density=True, color='b', alpha=0.6)
plt.axvline(x=x_real, color='r', linestyle='--', label='Posición Real del Robot')
plt.title('Simulación de Incertidumbre en la Medición de la Posición')
plt.xlabel('Posición Medida')
plt.ylabel('Densidad de Probabilidad')
plt.legend()
plt.grid(True)
plt.show()
