# CircuitPython

## DISCLAIMER

README.MD belonged to [Josie Muss](https://github.com/jmuss07) but I made edits and deleted the work that wasnt mine

## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Ultrasonic Sensor](#Ultrasonic_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)




---

## Hello_CircuitPython

### Description & Code
The code makes the Neopixel on the Metro Express flash a random color from a list of rainbow colors. It's looped so that every 0.1 seconds it chooses a different color from the same list.

```python

import board
import neopixel
import time
import random

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

red = [255, 0, 0]
orange = [255, 50, 0]
yellow = [200, 100, 0]
green = [0, 230, 0]
blue = [0, 0, 255]
purple = [146, 0, 199]
color_list = [red, orange, yellow, green, blue, purple]
print("Make it disco!!!")
dot.brightness = 0.1
while True:
    random_color = random.choice(color_list)
    dot.fill((random_color))
    time.sleep(0.1)


```

lk
### Evidence


![Look at it go!! So many random colors...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Random_Color.gif?raw=true)

Image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection
Neopixel looks nice and has lots of differnt color capibilities not any real applicable use. 


## CircuitPython_Servo

### Description & Code
Servo rotates back and forth

```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
import digitalio 
from adafruit_motor import servo
from digitalio import DigitalInOut, Direction, Pull

btn1 = DigitalInOut(board.D5)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(board.D6)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.A1, duty_cycle=2 ** 15, frequency=50)
# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while (btn1.value==True):
    for angle in range(0, 180, 5):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

if (btn2.value==True):       
    for angle in range(180, 0, -5): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)

```

### Evidence

NOT MY VIDEO

![...And the serial moniter showing its rotations!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Servo_Code_GIF.gif?raw=true)

Image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)
### Wiring
Simple servo wiring!

![Simple servo wiring!](https://github.com/jmuss07/Circuit-Python/blob/main/Images/servo.png?raw=true)

Image credit goes to [Josie Muss](https://github.com/jmuss07/Circuit-Python)

### Reflection
I did this shit wrong I didnt know what capictive touch was so I just ape brained it. But I couldve got it working if I put in better effort and actully took the time to read the page.

## Ultrasonic_Sensor

### Description & Code
This code powers an HCSR04 ultrasonic sensor. As the distance changes, the built in LED (the neopixel) on a Metro Express gradually shifts in colors in a range from red to green.

```python

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
```

### Evidence
It works!

(https://github.com/inovotn04/CircuitPython/raw/main/Images/DistanceSensorEvidence.gif?raw=true)

Image credit goes to [Ian Novotne](https://github.com/inovotn04/CircuitPython)

### Wiring
Ultrasonic sensor wiring

![Ultrasonic sensor wiring!](https://github.com/Jhouse53/CircuitPython/raw/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true)

Image credit goes to [Benton House](https://github.com/Jhouse53/CircuitPython)
### Reflection
This was my Favorite thing that we did the whole time. Joint was mad easy but my fucking sensor was busted and I had done it right but the sensor was buggin. Got a new sensor and It worked right away




## CircuitPython_LCD

### Description & Code
  
``` python


```
### Evidence
I dont have any vids lmao
### Wiring

### Reflection
This was fun I never got it to print on the screen because I hate looking for the libarys but I got it to fully function (to my standards) in the serial monitor.
