#!/bin/python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

y = [255, 255, 0]
x = [0, 0, 0]
b = [0, 0, 255]

charx = 0
chary = 0

path = [
  y,y,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,x,x,x,x,x,
  x,x,y,y,y,y,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,x,x,y,x,
  x,x,x,x,y,y,y,x,
  x,x,x,x,y,x,x,x
]

while True:
  sense.set_pixels(path)
  sense.set_pixel(charx, chary, b)

  pitch = sense.get_orientation()['pitch']
  roll = sense.get_orientation()['roll']

  print('Pitch:', pitch)
  print('Roll:', roll)

  if 270 < pitch < 315 and charx < 7:
    charx += 1

  if 45 < pitch < 90 and charx > 0:
    charx -= 1

  if 45 < roll < 90 and chary < 7:
    chary += 1

  if 270 < roll < 315 and chary > 0:
    chary -= 1

  current = sense.get_pixel(charx, chary)
  if current == x:
    charx = 0
    chary = 0

  sleep(0.4)
