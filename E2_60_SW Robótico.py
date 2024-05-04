import numpy as np

class Robot:
    def __init__(self, x, y, theta):
        self.x = x
        self.y = y
        self.theta = theta

    def move(self, linear_velocity, angular_velocity, duration):
        self.x += linear_velocity * np.cos(self.theta) * duration
        self.y += linear_velocity * np.sin(self.theta) * duration
        self.theta += angular_velocity * duration

robot = Robot(0, 0, 0)
robot.move(1, 0.5, 1)
print("Nueva posición del robot:", robot.x, robot.y, robot.theta)
