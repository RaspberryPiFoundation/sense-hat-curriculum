#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 255, 0]  # green
R = [255, 0, 0] # red
X = [0, 0, 0]  # off

secs = 10
timer = [ G for i in range(secs)] + [ X for j in range(64 - secs) ]

sense.set_pixels(timer)

# 30 second timer
for i in range(0, secs):
  sleep(1)
  timer[i] = R
  sense.set_pixels(timer)

for i in range(0, 10):
  sense.clear()
  sleep(0.1)
  sense.set_pixels(timer)
  sleep(0.1)
