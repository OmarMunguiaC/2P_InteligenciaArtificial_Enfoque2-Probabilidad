from pyfirmata import Arduino, util
import time

# Configurar la conexión con Arduino
board = Arduino('/dev/ttyUSB0')  # Cambia '/dev/ttyUSB0' por el puerto COM correcto en Windows
it = util.Iterator(board)
it.start()

# Configurar el pin del motor
motor_pin = board.get_pin('d:9:p')  # Pin digital 9 como salida PWM

# Función para controlar el motor
def control_motor(speed):
    motor_pin.write(speed)

# Ejemplo de uso
try:
    while True:
        control_motor(0.5)  # Encender el motor a la mitad de la velocidad máxima
        time.sleep(2)
        control_motor(0)  # Apagar el motor
        time.sleep(2)
finally:
    board.exit()
