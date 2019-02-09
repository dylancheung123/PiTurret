"""Simple test for using adafruit_motorkit with a stepper motor"""
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper

kit = MotorKit()
 
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    #kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)

