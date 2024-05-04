import numpy as np
import matplotlib.pyplot as plt

# Definir límites del espacio de configuración
x_min, x_max = -10, 10
y_min, y_max = -10, 10

# Generar una cuadrícula de puntos en el espacio de configuración
x_values = np.linspace(x_min, x_max, 100)
y_values = np.linspace(y_min, y_max, 100)
X, Y = np.meshgrid(x_values, y_values)

# Definir obstáculos
obstacle_x = [0, 5, -5]
obstacle_y = [5, -5, -5]

# Visualizar el espacio de configuración y los obstáculos
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, np.zeros_like(X), alpha=0.2, cmap='Greys')  # Espacio libre
plt.plot(obstacle_x, obstacle_y, 'ro')  # Obstáculos
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Espacio de Configuración')
plt.grid(True)
plt.axis('equal')
plt.show()
