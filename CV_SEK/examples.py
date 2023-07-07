from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from ModuloSwerve import ModuloSwerve
from DetectorCor import detecta_cor
import time

# Create your objects here.
ev3 = EV3Brick()

# modulo = ModuloSwerve(Port.A, Port.B)
motor = Motor(Port.A)

## sensor_s1 = ColorSensor(Port.S1)
sensor_s2 = UltrasonicSensor(Port.s2)

## girar motor até achar a cor
while detecta_cor(sensor_s1) != Color.RED:
    motor.run(90)
    print(detecta_cor(sensor_s1))
print(detecta_cor(sensor_s1))

## sensor ultrasonico
while True:
    print(sensor_s2.distance())
    if sensor_s2.distance() < 100:
        print("distancia maenor que 100")
        ev3.speaker.beep()
        break