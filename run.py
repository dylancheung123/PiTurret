'''
Interface for Raider Advanced FX to control the PiTurret
@author: Dylan L. Cheung
'''
import RPi.GPIO as GPIO
import time

from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from evdev import InputDevice, categorize, ecodes, KeyEvent

''' Globals Types'''
BUTTON = 1
AXIS = 3

''' Global Codes '''
ABS_X = 0
ABS_Y = 1

ABS_RZ = 5
ABS_THROTTLE = 6

ABS_HAT0X = 16
ABS_HAT0Y = 17

''' GPIO Pins '''
TRIGGER_PIN = 11

''' Initializing '''
GPIO.setup(TRIGGER_PIN, GPIO.OUT)

joystick = InputDevice("/dev/input/event1")
print(joystick.capabilities())

kit = MotorKit()
MOTOR_X = kit.stepper1
MOTOR_Y = kit.stepper2

# Code for reading from the joystick
for event in joystick.read_loop():
	if event.type == BUTTON:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode[0] == 'BTN_JOYSTICK':
				if keyevent.keycode[1] == 'BTN_TRIGGER':
					print("Fire!!!")
					GPIO.output(TRIGGER_PIN, GPIO.HIGH)
					time.sleep(1)
					GPIO.output(TRIGGER_PIN, GPIO.LOW)
	elif event.type == AXIS:
		if event.code == ABS_X:
			print("ABS_X with value: ", event.value)
		elif event.code == ABS_Y:
			print("ABS_Y with value: ", event.value)
			if event.value > 127:
				print("Tilting up")
				MOTOR_Y.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)			
			elif event.value < 127:
				print("Tilting down")
				MOTOR_Y.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
		elif event.code == ABS_RZ:
			print("ABS_RZ with value: ", event.value)
			if event.value > 127:
				print("Rotating right")
				MOTOR_X.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
			elif event.value < 127:
				print("Rotating left")
				MOTOR_X.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
		elif event.code == ABS_THROTTLE:
			print("ABS_THROTTLE with value: ", event.value)
		elif event.code == ABS_HAT0X:
			print("ABS_HAT0X with value: ", event.value)
		elif event.code == ABS_HAT0Y:
			print("ABS_HAT0Y with value: ", event.value)

# Code for running the motor
'''
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
'''
