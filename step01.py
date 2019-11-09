#!/usr/bin/env python

from time import sleep
import RPi.GPIO as GPIO

DIR = 3   # Direction GPIO Pin
STEP = 4  # Step GPIO Pin
CW = 0     # Clockwise Rotation
CCW = 1    # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CW)

step_count = SPR
delay = .0208

print("Clockwise")
for x in range(step_count):
#while True:
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CCW)
print("Counter-Clockwise")
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)

sleep(.5)
GPIO.output(DIR, CW)

step_count = SPR*3
delay = 0.1
print("Clockwise")
for x in range(step_count):
    GPIO.output(STEP, GPIO.HIGH)
    sleep(delay)
    GPIO.output(STEP, GPIO.LOW)
    sleep(delay)


GPIO.cleanup()
