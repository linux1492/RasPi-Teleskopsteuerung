#!/usr/bin/env python

#============================================#
# Autor Dr. Michael Danielides               						 #	 
# Datum 26.10.2019                           						 #
# Nutzung: Mit Gamepad Schalten von NEMA 17 Schrittmotor      	 #
# ======== "Right Buttom" schaltet PIN 4 ein und dreht den Motor#
#                     im Uhrzeigersinn um ca. 90 Grad.				 #
#     	       "Left Button" aendert PIN 3 und dreht den Motor gegen#
#			den Uhrzeigersinn um 90 Grad.				  #
#                     Cursor Pfeile "rechts/links" bewegen den Motor um     #
#                     Schritt im Uhrzeigersinn oder dagegen,			 #
#			Mit "SELECT" wird das 					         #
#                      Programm beendet.                 				         #
# Test USB-Port: Tippe die folgende Befehltszeile ein:                        #
# python /usr/local/lib/python2.7/dist-packages/evdev/evtest.py    #
#============================================#

#import evdev
from evdev import InputDevice, categorize, ecodes, list_devices
import RPi.GPIO as GPIO
import time
import string
from time import sleep

devices = map(InputDevice, list_devices())

eventX="nothing name"
nameX ="usb gamepad           "

for dev in devices:
     if dev.name == nameX:
        eventX=dev.fn
#        print dev.name
	print('Controller found and activated. Press any controler button to start. Press SELECT to stop the program.')
#        print('Your control device is called ',dev.name,' and uses the device port ',dev.fn,'.')
#print eventX

DIR = 3       # Direction GPIO Pin
STEP = 4    # Step GPIO Pin
SLEEP = 2    # Sleep High -> um Befehle fuer Motor anzunehmen
CW = 0       # Clockwise Rotation
CCW = 1     # Counterclockwise Rotation
SPR = 48   # Steps per Revolution (360 / 7.5)
vfak = 0.5  # rotation velocity factor

#GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#GPIO.setup(18,GPIO.OUT)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(SLEEP, GPIO.OUT)
#GPIO.output(DIR, CW)

step_count = SPR
delay = .0208

#cree un objet gamepad | creates object gamepad
#gamepad = InputDevice('/dev/input/event9')
gamepad = InputDevice(eventX)

#affiche la liste des device connectes | prints out device info at start
#print(gamepad)

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291
lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

GPIO.output(SLEEP, GPIO.LOW)

#affiche les codes interceptes |  display codes
for event in gamepad.read_loop():
    #Boutons | buttons 
    if event.type == ecodes.EV_KEY:
        #print(event)
        if event.value == 1:
            if event.code == xBtn:
                print("X")
            elif event.code == bBtn:
                print("B")
            elif event.code == aBtn:
#               GPIO.output(18,GPIO.LOW)
                print("A")
#    		GPIO.output(STEP, GPIO.LOW)
            elif event.code == yBtn:
#                GPIO.output(18,GPIO.HIGH)
                print("Y")
            elif event.code == lBtn:
                print("LEFT --> Counter-Clockwise")
		GPIO.output(DIR, CCW)
                GPIO.output(SLEEP, GPIO.HIGH)
		for x in range(step_count):
    		  GPIO.output(STEP, GPIO.HIGH)
    		  sleep(delay)
    		  GPIO.output(STEP, GPIO.LOW)
    		  sleep(delay)
            elif event.code == rBtn:
                print("RIGHT -> Clockwise")
		GPIO.output(DIR, CW)
                GPIO.output(SLEEP, GPIO.HIGH)
		for x in range(step_count):
  		  GPIO.output(STEP, GPIO.HIGH)
  		  sleep(delay)
    		  GPIO.output(STEP, GPIO.LOW)
   		  sleep(delay)
            elif event.code == selBtn:
                print("Select --> Stop now!")
                break
            elif event.code == staBtn:
                print("Start")
        elif event.value == 0:
          print("Relache | Release")

    #Gamepad analogique | Analog gamepad
    elif event.type == ecodes.EV_ABS:
        absevent = categorize(event)
        #print ecodes.bytype[absevent.event.type][absevent.event.code], absevent.event.value
        if ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_X":
             if absevent.event.value == 0:
                print("Left --> Counter-Clockwise")
		GPIO.output(DIR, CCW)
    		GPIO.output(STEP, GPIO.HIGH)
    		sleep(delay*vfak)
    		GPIO.output(STEP, GPIO.LOW)
    		sleep(delay*vfak)
             elif absevent.event.value == 255:
                print("Right  --> Motor Clockwise")
		GPIO.output(DIR, CW)
    		GPIO.output(STEP, GPIO.HIGH)
    		sleep(delay*vfak)
    		GPIO.output(STEP, GPIO.LOW)
    		sleep(delay*vfak)
             elif absevent.event.value == 127:
                print("Centre | Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == 0:
                print("Haut | Up")
             elif absevent.event.value == 255:
                print("Bas | Down")
             elif absevent.event.value == 127:
                print("Centre | Center")

    GPIO.output(SLEEP, GPIO.LOW)

