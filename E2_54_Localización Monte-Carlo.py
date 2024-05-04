import numpy as np

# Función para la actualización de la creencia basada en la observación
def observation_update(belief, likelihood):
    return belief * likelihood / np.sum(belief * likelihood)

# Función para la predicción de la creencia basada en el movimiento
def motion_prediction(belief, motion_model):
    return np.roll(np.dot(belief, motion_model), 1)

# Configuración inicial
belief = np.array([0.2, 0.2, 0.2, 0.2, 0.2])  # Creencia uniforme
likelihood = np.array([0.6, 0.1, 0.1, 0.1, 0.1])  # Probabilidades de observación
motion_model = np.array([[0.1, 0.8, 0.1, 0.0, 0.0],  # Modelo de movimiento
                         [0.0, 0.1, 0.8, 0.1, 0.0],
                         [0.0, 0.0, 0.1, 0.8, 0.1],
                         [0.1, 0.0, 0.0, 0.1, 0.8],
                         [0.8, 0.1, 0.0, 0.0, 0.1]])

# Actualizar la creencia después de la observación
belief = observation_update(belief, likelihood)

# Predecir la creencia después del movimiento
belief = motion_prediction(belief, motion_model)

print("Creencia actualizada después de la observación:", belief)
