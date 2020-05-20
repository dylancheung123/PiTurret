from globalVariables import q, fire, t_up, t_down, r_right, r_left
import RPi.GPIO as GPIO
import time
from adafruit_motorkit import MotorKit
from adafruit_motor import stepper
import commands

''' GPIO Pins '''
TRIGGER_PIN = 17

''' Initializing '''
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.output(TRIGGER_PIN, GPIO.HIGH)

kit = MotorKit()
MOTOR_X = kit.stepper1
MOTOR_Y = kit.stepper2

MOTOR_X.release()
MOTOR_Y.release()

def run():
  print("Running turret thread")
  actions = Actions()
  global q, fire, t_up, t_down, r_right, r_left
  while True:
    # Read from queue
    if not q.empty():
      new_key = q.get()
      q.task_done()
      # print("Read task off of queue")
      if new_key == commands.FIRE:
        fire = True
      elif new_key == commands.STOP_FIRE:
        fire = False
      elif new_key == commands.RELEASE_TILT:
        t_up = t_down = False
      elif new_key == commands.TILT_UP:
        t_up = True
      elif new_key == commands.TILT_DOWN:
        t_down = True
      elif new_key == commands.RELEASE_ROTATE:
        r_right = r_left = False
      elif new_key == commands.ROTATE_RIGHT:
        r_right = True
      elif new_key == commands.ROTATE_LEFT:
        r_left = True

    # Do any actions no matter what
    if fire:
      actions.fire()
    else:
      actions.stopFire()

    if not t_up and not t_down:
      actions.releaseTilt()
    if t_up:
      actions.tiltUp()
    if t_down:
      actions.tiltDown()
    if not r_right and not r_left:
      actions.releaseRotate()
    if r_right:
      actions.rotateRight()
    if r_left:
      actions.rotateLeft()

class Actions: 
  def fire(self):
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

  def stopFire(self):
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)

  def releaseTilt(self):
    MOTOR_Y.release()

  def tiltUp(self):
    MOTOR_Y.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)			

  def tiltDown(self):
    MOTOR_Y.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)

  def releaseRotate(self):
    MOTOR_X.release()

  def rotateRight(self):
    MOTOR_X.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)

  def rotateLeft(self):
    MOTOR_X.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
