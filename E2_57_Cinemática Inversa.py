import numpy as np

# Función de cinemática inversa
def inverse_kinematics(x, y, l1, l2):
    # Calcular el ángulo del primer eslabón (q1)
    q1 = np.arctan2(y, x)
    
    # Calcular la distancia entre el punto (x, y) y el origen del robot
    r = np.sqrt(x**2 + y**2)
    
    # Calcular el ángulo del segundo eslabón (q2)
    cos_q2 = (r**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sin_q2 = np.sqrt(1 - cos_q2**2)
    q2 = np.arctan2(sin_q2, cos_q2)
    
    return q1, q2

# Ejemplo de uso
x_target, y_target = 5, 5  # Posición deseada del extremo del efector
l1, l2 = 3, 3  # Longitudes de los eslabones

q1, q2 = inverse_kinematics(x_target, y_target, l1, l2)
print("Ángulos de las articulaciones (q1, q2):", np.degrees(q1), np.degrees(q2))
