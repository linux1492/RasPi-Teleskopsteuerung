#!/usr/bin/env python

from evdev import InputDevice, list_devices
devices = map(InputDevice, list_devices())
eventX="nothing"
for dev in devices:
    if dev.name == "usb gamepad":
        eventX = dev.fn
    print dev.fn,dev.name
print eventX
