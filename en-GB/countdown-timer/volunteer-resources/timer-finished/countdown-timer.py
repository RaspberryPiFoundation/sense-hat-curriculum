#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

secs = 5

for i in range(0,secs+1):
  sense.show_letter(str(secs-i), text_colour=[0, 255, 0])
  sleep(1)
