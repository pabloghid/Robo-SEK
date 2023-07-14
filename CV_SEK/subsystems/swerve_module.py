from pybricks.ev3devices import Motor
from pybricks.parameters import Port

class SwerveModule:
    def __init__(self, driving_motor: Port, steering_motor: Port):
        self.driving_motor = Motor(driving_motor)
        self.steering_motor = Motor(steering_motor)
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
            delta2_inv = (360-abs(delta1)) * (-1 if delta1 > 0 else 1)

            delta_result = delta1_inv if delta1_inv < delta2_inv else delta2_inv
        else:
            delta_result = delta1 if delta1 < delta2 else delta2

        self.steering_motor.track_target(self.steering_motor.get_angle + delta_result)

    def set_desired_state(self, desired_angle, desired_speed):
        angle = desired_angle
        self.set_desired_angle(angle)