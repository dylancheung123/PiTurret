'''
Interface for Raider Advanced FX to control the PiTurret
@author: Dylan L. Cheung
'''
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

''' Initializing '''
joystick = InputDevice("/dev/input/event1")
print(joystick.capabilities())
kit = MotorKit()

# Code for reading from the joystick
for event in joystick.read_loop():
	print()
	print(categorize(event)
	
	if event.type == BUTTON:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode[0] == 'BTN_JOYSTICK':
				if keyevent.keycode[1] == 'BTN_TRIGGER':
					print("Fire!!!")

	elif event.type == AXIS:
		if event.code == ABS_X:
			print("ABS_X")
		elif event.code == ABS_Y:
			print("ABS_Y")
		elif event.code == ABS_RZ:
			print("ABS_RZ"):
		elif eventcode == ABS_THROTTLE:
			print("ABS_THROTTLE")
		elif event.code == ABS_HAT0X:
			print("ABS_HAT0X")
		elif eventcode == ABS_HAT0Y:
			print("ABS_HAT0Y")

	else: 
		print("OTHER.....")	

# Code for running the motor
'''
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
'''
