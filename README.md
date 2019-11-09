# RasPi-Teleskopsteuerung
Ein 3D-gedrucktes Newton-Teleskop soll eine Montierung samt Motorsteuerung erhalten. Die Steuerung soll per Gamepad gesteuert werden.
Das Projekt befindet sich noch in verschiedenen Phasen, die alle irgendwie noch nicht druckreif sind. Deswegen liegt hier nur eine grobe Projektstruktur mit einigen Anmerkungen und Links vor. Mit der Zeit soll sich das aendern.
Projektstruktur

1) 3D-gedrucktes Newtown-Teleskop mit Raspberry Pi Kamera wie unter https://www.hackster.io/news/pikon-a-3d-printed-raspberry-pi-powered-telescope-608d1abfc9f1 beschrieben

2) Steuerung von Schrittmotoren via Retro Nintendo USB Gamepad. Diese Retro Gamepads sind fuer unter einem Euro in China erhaeltlich und somit fuer Makerprojekte gut geeignet. Siehe als Beispiel: https://www.alibaba.com/product-detail/Best-Price-USB-Port-Gamepad-for_60447434885.html?spm=a2700.7724857.normalList.262.29137396A6WtDm . Als Schrittmotor verwenden wir einen Nema 17 12V 30 Ohm, 0,4 A Schrittmotor den es zum Beispiel bei Amazon oder bekannten Elektronik-Versandhaeusern zu kaufen gibt: https://www.amazon.de/Quimat-Schrittmotor-Stepping-36-8oz-Haltemoment/dp/B06XRFCP3X/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=nema+17+schrittmotor+12+volt+30+ohm&qid=1573311720&sr=8-6
Bei dem in diesen Projekt verwendeten Treiber handelt es sich um einen DRV 8825 der unter https://www.az-delivery.com/products/drv8825-schrittmotor-treiber-modul-mit-kuhlkorper?_pos=1&_sid=6f95f54ab&_ss=r zu beziehen ist.

2.1) Vorbereiten der Gamepad Steuerung auf dem Raspberry Pi:

Unserer Code wurde fuer Python Version 2.7.13 geschrieben. Mit den folgenden Befehl findest Du heraus, ob Deine Python Version aelter ist als 2.7.13:

python --version
Python 2.7.13

Solltest Du eine aeltere Version haben koenntest Du diese auffrischen mit:

sudo apt-get update
sudo apt-get upgrade

Um die Treiber Software "evdev"fuer das Gamepad zu installieren, benoetigast Du PIP. Das erhalst Du mit dem Kommando

sudo apt-get install python-pip

Danach kannst Du mit dem Kommando

sudo pip install evdev

die Treiber Software installieren. Dann kannst Du mit der folgenden Befehlszeile pruefen, ob Dein Gamepad angeschlossen ist:

python /usr/local/lib/python2.7/dist-packages/evdev/evtest.py

In unserem Fall sieht das Ergebnis so aus:

ID  Device               Name                                Phys                                Uniq
---------------------------------------------------------------------------------------------------------------------
0   /dev/input/event0    USB OPTICAL MOUSE                   usb-3f980000.usb-1.1.3/input0           
1   /dev/input/event1    USB OPTICAL MOUSE  Keyboard         usb-3f980000.usb-1.1.3/input1           
2   /dev/input/event2    USB OPTICAL MOUSE  Consumer Control usb-3f980000.usb-1.1.3/input1           
3   /dev/input/event3    HAILUCK CO.,LTD USB KEYBOARD        usb-3f980000.usb-1.3/input0             
4   /dev/input/event4    HAILUCK CO.,LTD USB KEYBOARD Mouse  usb-3f980000.usb-1.3/input1             
5   /dev/input/event5    HAILUCK CO.,LTD USB KEYBOARD System Control usb-3f980000.usb-1.3/input1             
6   /dev/input/event6    HAILUCK CO.,LTD USB KEYBOARD Consumer Control usb-3f980000.usb-1.3/input1             
7   /dev/input/event7    HAILUCK CO.,LTD USB KEYBOARD Wireless Radio Control usb-3f980000.usb-1.3/input1             
8   /dev/input/event8    usb gamepad                         usb-3f980000.usb-1.1.2/input0 

Select devices [0-8]: 8

Das gesuchte Gamepad liegt auf der Adresse "event8". Tippt man jetzt eine "8" ein so kann man die verschiedenen Buttoms des Gamepads testen. in unserem Beispiel sieht das fuer das Druecken des Y-Buttoms so aus:

Listening for events (press ctrl-c to exit) ...
time 1573314302.61    type 4 (EV_MSC), code 4    (MSC_SCAN), value 589828
time 1573314302.61    type 1 (EV_KEY), code 291  (BTN_TOP), value 1
time 1573314302.61    --------- SYN_REPORT --------
time 1573314302.69    type 4 (EV_MSC), code 4    (MSC_SCAN), value 589828
time 1573314302.69    type 1 (EV_KEY), code 291  (BTN_TOP), value 0
time 1573314302.69    --------- SYN_REPORT --------

Beenden kann man diesen Test mit STR-C.

Gut nun ist der Gamepad-Treiber installiert und das Pythonprogramm "joy.py" kann ausprobiert werden. Obwohl man immer alle Python-Scripte aus Python aufrufen kann, ist es schoener diese ausfuerbar zu machen und sich viel Tipperei zu sparen. Deswegen muss man zuerst die folgende Befehlszeile einmalig ausfuehren:

chmod u+x joy.py

Von nun an laesst sich dieser Python-Code einfach mit

./joy.py 

ausfuehren. Wenn Du Pech hast erhaelltst Du aber folgende Ausgabe:

Traceback (most recent call last):
  File "./joy.py", line 7, in <module>
    gamepad = InputDevice('/dev/input/event9')
  File "/usr/local/lib/python2.7/dist-packages/evdev/device.py", line 127, in __init__
    fd = os.open(dev, os.O_RDONLY | os.O_NONBLOCK)
OSError: [Errno 2] No such file or directory: '/dev/input/event9'

Das haengt damit zusammen, dass Du die Anschrift Deines Gamepad nicht korrekt gesetzt hast. In unserem Fall ist das Gamepad auf "event8" und nicht auf "event9". Deswegen muss das in Zeile 7 veraendert werden:

gamepad = InputDevice('/dev/input/event8')

Wenn wir jetzt ./joy.py ausfuehren dann erhalten wir fuer das Druecken der Buttoms "X","B","A" und "X":

device /dev/input/event8, name "usb gamepad           ", phys "usb-3f980000.usb-1.1.2/input0"
event at 1573315008.814635, code 291, type 01, val 01
event at 1573315008.854655, code 291, type 01, val 00
event at 1573315012.342644, code 290, type 01, val 01
event at 1573315012.422653, code 290, type 01, val 00

Das gibt uns die benoetigten Kodes fuer unsere spaeteren Python-Skripte an.

Was hier noch fehlt ist eine automatische Abfrage auf welcher Adresse der Gamepad liegt.

3) Azimutale Montierung wie fuer Dobson-Teleskope ueblich aber mit der Motorsteuerung

4) GUI zur Steuerung des Teleskopes 

5) GoTo-Steuerung des Teleskopes bzw. Anbindung an die Software Stellarium. Stellarium ist unter https://stellarium.org/ im Internet fuer Linux, Mac und WinDoof kostenlos (fuer private Nutzung) als OpenSource zu erhalten.

HINWEIS: 

1) Die genannten Links zu Materialquellen sind keine Reklame fuer die Laeden, sondern sollen nur als Link zu einer von vielen moeglichen Bezugsquellen gesehen werden. Es gibt sicherlich auch noch bessere, preisguenstigere oder anderweitig bessere Bezugsquellen. Deswegen versuchen wir in diesem Projekt auch immer, so weit moeglich, immer so viele verschiedene Bezugsquellen wie moeglich anzugeben!

2) Natuerlich werden in diesem Projekt viele Dinge vorgestellt, die vorher auch schon im Internet veroeffentlich wurden. Wir werden versuchen im Laufe des Projektes die Quellen ordentlich anzugeben. Im Moment befindet sich das Projekt noch im Entwicklungsstatus.
