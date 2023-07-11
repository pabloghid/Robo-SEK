from pybricks.ev3devices import Motor
from pybricks.parameters import Port

class SwerveModule:
    def __init__(self, drive_motor: Port, steering_motor: Port):
        self.drive_motor = Motor(drive_motor)
        self.steering_motor = Motor(steering_motor)
