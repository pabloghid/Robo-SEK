#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from subsystems.swerve_module import SwerveModule
from color_detection_utils import detecta_cor
import time

# Create your objects here.
ev3 = EV3Brick()

# modulo = ModuloSwerve(Port.A, Port.B)
motor = Motor(Port.A)

sensor_s1 = ColorSensor(Port.S1)
sensor_s2 = ColorSensor(Port.S2)
sensor_s3 = ColorSensor(Port.S3)
sensor_s4 = ColorSensor(Port.S4)


motor.track_target(180)
time.sleep(1)
print(motor.angle())
motor.track_target(360)
time.sleep(1)
print(motor.angle())
motor.track_target(180)
time.sleep(1)
print(motor.angle())

ev3.speaker.beep()