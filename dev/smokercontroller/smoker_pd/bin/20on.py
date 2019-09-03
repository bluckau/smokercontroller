#!/usr/bin/env python
import Stubs.RPi.GPIO as GPIO

THRESHOLD = 80
SWING = 1

METRIC=False
MODE=0 #0 is cool 1 is heat
INTERVAL = 5

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20, GPIO.OUT)
print(GPIO.input(20))
print("Turn On!")
GPIO.output(20, GPIO.HIGH)
print(GPIO.input(20))
