from asyncore import read
import time
from time import sleep
import board
from analogio import AnalogIn 
from digitalio import DigitalInOut

analog_in = AnalogIn(board.A1)

while True:

   print(analog_in.value)
   time.sleep(0.1)
