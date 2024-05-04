import numpy as np

# Función de actualización de la estimación del estado
def state_update(x, P, z, R, H):
    K = np.dot(P, np.dot(H.T, np.linalg.inv(np.dot(H, np.dot(P, H.T)) + R)))
    x = x + np.dot(K, (z - np.dot(H, x)))
    P = np.dot((np.eye(len(x)) - np.dot(K, H)), P)
    return x, P

# Ejemplo de uso
# Configuración inicial
x = np.array([0, 0, 0])  # Posición inicial del robot
P = np.eye(3)  # Matriz de covarianza inicial
z = np.array([1, 1])  # Medida de posición
R = np.eye(2)  # Covarianza del sensor
H = np.array([[1, 0, 0], [0, 1, 0]])  # Matriz de medición

# Actualizar la estimación del estado
x, P = state_update(x, P, z, R, H)

print("Estimación del estado actualizada:", x)
