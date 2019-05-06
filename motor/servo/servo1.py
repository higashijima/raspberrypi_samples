import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)

gpOut = 12
GPIO.setup(gpOut, GPIO.OUT)

servo = GPIO.PWM(gpOut, 50)


while True:
  print("befor start")
  servo.start(0)
  print("after start")
  for turn in [2.5, 7.25]:
    print("Duty={}".format(turn))
    servo.ChangeDutyCycle(turn)
    print("changed")
    time.sleep(2)
    print("after sleep")

servo.stop()
GPIO.cleanup(gpOut)

