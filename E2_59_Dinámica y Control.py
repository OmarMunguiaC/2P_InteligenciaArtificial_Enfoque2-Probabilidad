import numpy as np
import matplotlib.pyplot as plt

# Parámetros del robot
wheel_radius = 0.05  # Radio de las ruedas (en metros)
wheel_base = 0.2  # Distancia entre las ruedas (en metros)

# Función de control proporcional (P)
def proportional_control(target_pose, current_pose, Kp):
    error = target_pose - current_pose
    return Kp * error

# Función de simulación de la dinámica del robot
def simulate_robot_motion(initial_pose, target_pose, duration, Kp):
    num_steps = int(duration / dt)
    time = np.linspace(0, duration, num_steps)
    poses = np.zeros((2, num_steps))
    poses[:, 0] = initial_pose

    for i in range(1, num_steps):
        current_pose = poses[:, i - 1]
        control = proportional_control(target_pose, current_pose, Kp)
        poses[0, i] = current_pose[0] + wheel_radius * (control[0] + control[1]) * np.cos(current_pose[2]) * dt
        poses[1, i] = current_pose[1] + wheel_radius * (control[0] + control[1]) * np.sin(current_pose[2]) * dt
        poses[2, i] = current_pose[2] + (wheel_radius / wheel_base) * (control[1] - control[0]) * dt

    return time, poses

# Configuración de la simulación
initial_pose = np.array([0, 0, 0])  # Pose inicial del robot (x, y, theta)
target_pose = np.array([2, 2, np.pi/2])  # Pose objetivo del robot (x, y, theta)
duration = 10  # Duración de la simulación (en segundos)
dt = 0.1  # Paso de tiempo (en segundos)
Kp = np.array([1, 1])  # Ganancias del controlador proporcional

# Simulación de la dinámica y control del robot
time, poses = simulate_robot_motion(initial_pose, target_pose, duration, Kp)

# Visualización de la trayectoria del robot
plt.figure(figsize=(10, 6))
plt.plot(poses[0, :], poses[1, :], label='Trayectoria del Robot')
plt.plot(target_pose[0], target_pose[1], 'ro', label='Pose Objetivo')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')
plt.title('Simulación de Dinámica y Control de un Robot Móvil')
plt.grid(True)
plt.legend()
plt.axis('equal')
plt.show()
