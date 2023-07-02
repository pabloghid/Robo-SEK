from pybricks.ev3devices import Motor
from pybricks.parameters import Port

class ModuloSwerve:
    def __init__(self, motor_drive: Port, motor_steering: Port):
        self.motor_drive = Motor(motor_drive)
        self.motor_steering = Motor(motor_steering)
