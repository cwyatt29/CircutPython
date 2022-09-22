# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_hcsr04
import neopixel

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1

while True:
    try:
        distance = sonar.distance
        print((distance))## print dis if no error
        if (distance < 10):
            dot.fill((255, 0, 0))
        elif distance > 10 and distance < 15:
            dot.fill((0, 0, 255))
        else:
            dot.fill((0, 255, 0))
    except RuntimeError:
        print("Retrying!")## if error print dis
 
    time.sleep(0.1)