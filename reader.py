'''
Interface for Raider Advanced FX to control the PiTurret
@author: Dylan L. Cheung
'''
from globalVariables import q
import commands
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

joystick = InputDevice("/dev/input/event0")
print(joystick)
print(joystick.capabilities(verbose=True))

def run():
  print("Running reader thread")
  global q
  for event in joystick.read_loop():
    print()
    # print(categorize(event))
    if event.type == BUTTON:
      keyevent = categorize(event)
      if keyevent.keycode[0] == commands.JOYSTICK:
        if keyevent.keycode[1] == commands.TRIGGER:
          if keyevent.keystate == keyevent.key_down:
            print("Fire")
            q.put(commands.FIRE)
          elif keyevent.keystate == keyevent.key_up:
            print("Release fire")
            q.put(commands.STOP_FIRE)
    elif event.type == AXIS:
      if event.code == ABS_X:
        print("ABS_X with value: ", event.value)
        # Do nothing here
        # Panning functionality?
      elif event.code == ABS_Y:
        print("ABS_Y with value: ", event.value)
        if event.value == 127:
          print("Releasing Tilt")
          q.put(commands.RELEASE_TILT)
        elif event.value > 127:
          print("Tilting up")
          q.put(commands.TILT_UP)
        elif event.value < 127:
          print("Tilting down")
          q.put(commands.TILT_DOWN)
      elif event.code == ABS_RZ:
        print("ABS_RZ with value: ", event.value)
        if event.value == 127:
          print("Releasing Rotate")
          q.put(commands.RELEASE_ROTATE)
        elif event.value > 127:
          print("Rotating right")
          q.put(commands.ROTATE_RIGHT)
        elif event.value < 127:
          print("Rotating left")
          q.put(commands.ROTATE_LEFT)
      elif event.code == ABS_THROTTLE:
        print("ABS_THROTTLE with value: ", event.value)
        # Do nothing
        # Sensitivity setting?
      elif event.code == ABS_HAT0X:
        print("ABS_HAT0X with value: ", event.value)
        # Do nothing
      elif event.code == ABS_HAT0Y:
        print("ABS_HAT0Y with value: ", event.value)
        # Do nothing
