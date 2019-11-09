#!/usr/bin/env python

#============================================#
# Autor Dr. Michael Danielides               # 
# Datum 26.10.2019                           #
# Nutzung: Mit Gamepad Schalten von LED      #
# ======== "Y" schaltet PIN 18 ein und "A"   #
#          wieder aus. Mit "SELECT" wird das #
#          Programm beendet.                 #
#============================================#

#import evdev
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

#cree un objet gamepad | creates object gamepad
gamepad = InputDevice('/dev/input/event9')

#affiche la liste des device connectes | prints out device info at start
print(gamepad)

aBtn = 289
bBtn = 290
xBtn = 288
yBtn = 291
lBtn = 292
rBtn = 293
selBtn = 296
staBtn = 297

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
                GPIO.output(18,GPIO.LOW)
                print("A --> LED off")
            elif event.code == yBtn:
                GPIO.output(18,GPIO.HIGH)
                print("Y --> LED on")
            elif event.code == lBtn:
                print("LEFT")
            elif event.code == rBtn:
                print("RIGHT")
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
                print("Gauche | Left")
             elif absevent.event.value == 255:
                print("Droite | Right")
             elif absevent.event.value == 127:
                print("Centre | Center")
        elif ecodes.bytype[absevent.event.type][absevent.event.code] == "ABS_Y":
             if absevent.event.value == 0:
                print("Haut | Up")
             elif absevent.event.value == 255:
                print("Bas | Down")
             elif absevent.event.value == 127:
                print("Centre | Center")
