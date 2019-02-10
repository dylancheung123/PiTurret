'''
Interface for Raider Advanced FX to control the PiTurret
@author: Dylan L. Cheung
'''

import time
import pygame
import RPi.GPIO as GPIO

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

''' Initializing '''
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

kit = MotorKit()
 
'''
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
'''
