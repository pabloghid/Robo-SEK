from pybricks.ev3devices import Motor
from pybricks.parameters import Port
import time

class SwerveModule:
    def __init__(self, driving_motor: Port, steering_motor: Port):
        self.driving_motor = Motor(port=driving_motor)
        self.steering_motor = Motor(port=steering_motor, gears=[8,56])
        self.speed_multiplier = 1;

    def get_angle(self):
        angle = self.steering_motor.angle() % 360
        if angle < 0:
            angle += 360
        return angle

    def set_angle(self, desired_angle):
        current_angle = self.get_angle()

        delta1 = desired_angle - current_angle
        delta2 = (360-abs(delta1)) * (-1 if delta1 > 0 else 1)

        if (abs(delta1) > 90) and (abs(delta2) > 90):
            self.speed_multiplier *= -1
            desired_angle_inv = (desired_angle + 180) % 360
            delta1_inv = desired_angle_inv - current_angle
            delta2_inv = (360-abs(delta1_inv)) * (-1 if delta1_inv > 0 else 1)

            delta_result = delta1_inv if abs(delta1_inv) < abs(delta2_inv) else delta2_inv
        else:
            delta_result = delta1 if abs(delta1) < abs(delta2) else delta2

        self.steering_motor.track_target(self.steering_motor.angle() + delta_result)
    
    def set_speed(self, speed):
        self.driving_motor.run(speed*self.speed_multiplier)

    def stop(self):
        self.steering_motor.hold();
        self.driving_motor.stop();

    def steering_done(self):
        return self.steering_motor.control.done()