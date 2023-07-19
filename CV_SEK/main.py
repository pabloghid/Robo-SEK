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

swerve1 = SwerveModule(Port.A, Port.B)
# swerve2 = SwerveModule(Port.C, Port.D)

swerve1.set_desired_state(90, 300)

time.sleep(2)
