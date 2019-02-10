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
joystick = joysticks[0]
joystick.init()
name = joysticks[0].get_name()
print("Initializing joystick: " + name)
# Usually axis run in pairs, up/down for one, and left/right for
# the other.
axes = joystick.get_numaxes()
print("Number of axes: {}".format(axes) )
      
for i in range( axes ):
	axis = joystick.get_axis( i )
	print("Axis {} value: {:>6.3f}".format(i, axis) )
                   
buttons = joystick.get_numbuttons()
print("Number of buttons: {}".format(buttons) )
for i in range( buttons ):
	button = joystick.get_button( i )
	print("Button {:>2} value: {}".format(i,button) )

done = False
        
# -------- Main Program Loop -----------
while done==False:
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")

            
kit = MotorKit()
 
'''
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
'''
