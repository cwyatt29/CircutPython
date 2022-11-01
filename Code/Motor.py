import time
from time import sleep
import board
import simpleio
from analogio import AnalogIn 
from digitalio import DigitalInOut

analog_in = AnalogIn(board.A0) #potentionmeter pin
digital_out = DigitalInOut(board.D8)
while True:

  sensor_value = analog_in.value
  # Map the sensor's range from 0<=sensor_value<=255 to 0<=sensor_value<=1023
  mapped_value = simpleio.map_range(sensor_value, 0, 65520, 0, 255)
  print("mapped sensor value: ", mapped_value)
  time.sleep(0.1)
  mapped_value = digital_out
  



