from swerve_module import SwerveModule
from constants import *

class Drive:
    def __init__(self):
        self.left_module = SwerveModule(SWERVE_LEFT_DRIVING_PORT, SWERVE_LEFT_STEERING_PORT)
        self.right_module = SwerveModule(SWERVE_RIGHT_DRIVING_PORT, SWERVE_RIGHT_STEERING_PORT)
    
    def set_module_angles(self, angle):
        self.left_module.set_angle(angle)
        self.right_module.set_angle(angle)

    def set_module_speeds(self, speed):
        self.left_module.set_speed(speed)
        self.right_module.set_speed(speed)

    def drive_towards_angle(self, angle, speed):
        self.stop();
        self.set_module_angles(angle)
        while (not self.left_module.steering_done) or (not self.right_module.steering_done):
            pass
        self.set_module_speeds(speed)

    def stop(self):
        self.left_module.stop()
        self.right_module.stop()
