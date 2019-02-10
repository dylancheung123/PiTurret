'''
Interface for Raider Advanced FX to control the PiTurret
@author: Dylan L. Cheung
'''
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
from evdev import InputDevice, categorize, ecodes, KeyEvent

''' Globals '''
BUTTON = 1

''' Initializing '''
joystick = InputDevice("/dev/input/event1")
print(joystick.capabilities())
kit = MotorKit()

# Code for reading from the joystick
for event in joystick.read_loop():
	print()
	print(categorize(event))
	if event.type == BUTTON:
		keyevent = categorize(event)
		if keyevent.keystate == KeyEvent.key_down:
			if keyevent.keycode[0] == 'BTN_JOYSTICK':
				if keyevent.keycode[1] == 'BTN_TRIGGER':
					print("Fire!!!")
	elif event.type == 3:
		print("ABS")
		print(event.code)
	else: 
		print("OTHER.....")	

# Code for running the motor
'''
for i in range(1000):
    kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
    kit.stepper2.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
'''
