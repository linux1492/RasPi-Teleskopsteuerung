# RasPi-Teleskopsteuerung
Ein 3D-gedrucktes Newton-Teleskop soll eine Montierung samt Motorsteuerung erhalten. Die Steuerung soll per Gamepad gesteuert werden.
Das Projekt befindet sich noch in verschiedenen Phasen, die alle irgendwie noch nicht druckreif sind. Deswegen liegt hier nur eine grobe Projektstruktur mit einigen Anmerkungen und Links vor. Mit der Zeit soll sich das aendern.
Projektstruktur
1) 3D-gedrucktes Newtown-Teleskop mit Raspberry Pi Kamera wie unter https://www.hackster.io/news/pikon-a-3d-printed-raspberry-pi-powered-telescope-608d1abfc9f1 beschrieben
2) Steuerung von Schrittmotoren via Retro Nintendo USB Gamepad. Diese Retro Gamepads sind fuer unter einem Euro in China erhaeltlich und somit fuer Makerprojekte gut geeignet. Siehe als Beispiel: https://www.alibaba.com/product-detail/Best-Price-USB-Port-Gamepad-for_60447434885.html?spm=a2700.7724857.normalList.262.29137396A6WtDm . Als Schrittmotor verwenden wir einen Nema 17 12V 30 Ohm, 0,4 A Schrittmotor den es zum Beispiel bei Amazon oder bekannten Elektronik-Versandhaeusern zu kaufen gibt: https://www.amazon.de/Quimat-Schrittmotor-Stepping-36-8oz-Haltemoment/dp/B06XRFCP3X/ref=sr_1_6?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=nema+17+schrittmotor+12+volt+30+ohm&qid=1573311720&sr=8-6
Bei dem in diesen Projekt verwendeten Treiber handelt es sich um einen DRV 8825 der unter https://www.az-delivery.com/products/drv8825-schrittmotor-treiber-modul-mit-kuhlkorper?_pos=1&_sid=6f95f54ab&_ss=r zu beziehen ist.
3) Azimutale Montierung wie fuer Dobson-Teleskope ueblich aber mit der Motorsteuerung
4) GUI zur Steuerung des Teleskopes 
5) GoTo-Steuerung des Teleskopes bzw. Anbindung an die Software Stellarium. Stellarium ist unter https://stellarium.org/ im Internet fuer Linux, Mac und WinDoof kostenlos (fuer private Nutzung) als OpenSource zu erhalten.

HINWEIS: Die genannten Links zu Materialquellen sind keine Reklame fuer die Laeden, sondern sollen nur als Link zu einer von vielen moeglichen Bezugsquellen gesehen werden. Es gibt sicherlich auch noch bessere, preisguenstigere oder anderweitig bessere Bezugsquellen. Deswegen versuchen wir in diesem Projekt auch immer, so weit moeglich, immer so viele verschiedene Bezugsquellen wie moeglich anzugeben!
