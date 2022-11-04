# Engineering 3 Notebook 2022 Q1



## Table of Contents
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [Ultrasonic Sensor](#Ultrasonic_Sensor)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [Intro to CAD](#introtocad)
* [Swing Arm](#swingarm)
* [Multi-Part Studio](#multi-partstudio)
* [Pumpkin](#pumpkin)
---
## *DISCLAIMER*

README.MD (FOR THE CODE CRAP) belonged to [Josie Muss](https://github.com/jmuss07) but I made edits and deleted the work that wasnt mine. ALL CAD DOCUMENTATION IS ORIGINAL!!!! 

*P.S.*

The documentation has both the Code work and the CAD work in the same repository. I prefer to have it like this because I can edit all my work in one place. I also think that it looks better and is easier for a reader because all of my work is in one place. I personally think that github is very user-unfriendly and that it sucks for people who don't know what their doing.




# **CircuitPython**





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
This was my Favorite thing that we did the whole time. Was mad easy but my sensor was busted and I had done it right but the sensor was buggin. Got a new sensor and It worked right away




## CircuitPython_LCD

### Description & Code
  
``` python


```
### Evidence
I dont have any vids lmao
### Wiring

### Reflection
This was fun I never got it to print on the screen because I hate looking for the libarys but I got it to fully function (to my standards) in the serial monitor.
<<<<<<< HEAD

## Motor Control 

### Description & Code

``` python

import time
from time import sleep
import board
import simpleio
from analogio import AnalogIn 
import pwmio  

analog_in = AnalogIn(board.A1) #potentionmeter pin
pin_out = pwmio.PWMOut(board.D8,duty_cycle=65535,frequency=5000)

while True:

  sensor_value = analog_in.value
  # Map the sensor's range from 0<=sensor_value<=255 to 0<=sensor_value<=1023
  mapped_value = int(simpleio.map_range(sensor_value, 0, 65535, 0, 255))
  
  pin_out.duty_cycle = sensor_value
  print("mapped sensor value: ", sensor_value)
  time.sleep(0.1)

```

### Evidence
![Evidence_Gif](https://github.com/cwyatt29/Engineering_3_Notebook/blob/master/Images/Motor_Control.gif?raw=true)

### Wiring 

![Wiring_Pictures](https://github.com/cwyatt29/Engineering_3_Notebook/blob/master/Images/Fritzing.PNG?raw=true)

### Reflection

# **CAD**


## Intro_To_CAD

### Description
The goal was to design a Spinner toy that would launch into the air when a key is pulled. I used tools that were new to me such as the helix and sweep. I was responsible for making the spinner part and the propeller part.

The Model consists of 5 main parts the key, ring, spinner, body, and prop. All the parts are made out of ABS plastic. The prop is suprisingly light and the outer support ring is only 2mm thick.

### Evidence and Pics
Weight: 10.522 g

![Spinner](/Images/Spinner.PNG)

*https://cvilleschools.onshape.com/documents/73d7010c7540dad2063afac7/w/665c6b0b34cbec05f29edf63/e/21e07fdbfcc43ec13b791f6b*


### Reflection
I liked this assignment because I got to do the more chalenging role which taught me how to use new commands. the commands are going to be useful in the future to make spinning and geared objects.I think that one think that wouldve been useful to know before hand is to not get ahead of the instructions because if you do something that isnt supposed to be done until later it can mess up 





## Swing_Arm

### Description
Replicated the provided design using the images provided whilst not relying on only dimensions. I heavily used tools like equal, parallel, and symmetric.

There is only one part in the assignment but the part is very complex and has holes, filets and, chamfers on every single plane.

### Evidence and Pics
Weight: 2355.7 g

![Swing_Arm](/Images/Swing%20Arm.PNG)
*https://cvilleschools.onshape.com/documents/a5fd8d22b575fddb2bdee574/w/76f65086d2b77c85ffe6fc60/e/afefe01db5f326c914c81df6*

### Reflection

The original image was black and white so it was hard to see what the final should look like. Also it was really easy to try to use dimensions on everything but it will save you so much time if you use constrains that change as needed but will also keep the structure of the shape better.




## Multi-Part_Studio

### Description

Replicated the provided design using the images provided whilst not relying on only dimensions. I heavily used tools like equal, parallel, and symmetric. I also used the section veiw tool which essentially let you see the part if it was cut in half. This is useful for making sure all of your parts are in the correct place. It is also good to occcacsionly use the check interfernce tool to make sure
nothing is to big.


### Evidence and Pics
Weight: 2856.13 g

![Multi-Part_Studio](/Images/Multipart%20Studio.PNG)
*https://cvilleschools.onshape.com/documents/70205c568136983cceef3de1/w/f7eb5c01c69e37fd72611c13/e/ca8e036bd565a6607f8a4e05* 




### Reflection

Using the design intents you gain so much information on how the final project should work. Also make sure you read the fine print and change the materials if necessary.



## Pumpkin

### Description
Use all the tools available to your knowlegde to creat a pumpkin and then make a slide show presenting the pumpkin in order to win a contest


The pumpkin is made of bronze and the baseplate its attached to is made of steel which is why its so heavy. The cut out face is the face of infamous youtuber Dream. Dream has been active online since 2014, but did not gain substantial popularity until 2019 and 2020. He is well known for his YouTube series "Minecraft Manhunt" and was also well known for his Minecraft speedruns, in which he was accused of cheating in late 2020. Dream later admitted to using game modifications, but maintained that he used them unintentionally during his single-player speedruns, intending for them to only apply during his multiplayer "challenge videos" Content created in the Dream SMP, Dream's invite-only survival multiplayer (SMP) Minecraft server that stars content creators engaged in roleplay, has also attracted considerable attention and a popular fandom. He also has come under controversy for multiple grooming allegations.

*https://en.wikipedia.org/wiki/Dream_(YouTuber)*


### Evidence and Pics
Weight: 7.285 lbs

![Pumpkin](/Images/Drumpkin.PNG) 

*https://cvilleschools.onshape.com/documents/a7955c3dd0322a3ef6f1c2e3/w/9b4b64cb12b972a4d351a598/e/7dcb0c9bd76b4a67b95b970e*
### Reflection
It was fun to mess around with the image overlay tool. These tools also have practical aspects that would help when making something that has to attach to something that doesnt exist in CAD. like if you needed to make something to mount to a fixed mounting peice.
