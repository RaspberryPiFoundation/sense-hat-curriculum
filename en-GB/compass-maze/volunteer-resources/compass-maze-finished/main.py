#!/bin/python3

from sense_hat import *
import maze

maze.start()

sense = SenseHat()
sense.clear()

sense.set_rotation(90)

            
while True:
    
  heading = sense.get_compass()

  if heading < 45 or heading > 315:
    dir = 'north'
  elif heading < 135:
    dir = 'east'
  elif heading < 225:
    dir = 'south'
  else:
    dir = 'west'
    
  sense.show_letter(dir[0].upper(), text_colour=maze.getColour())
  
  for e in sense.stick.get_events():
    if e.action == ACTION_PRESSED and e.direction == DIRECTION_MIDDLE:
      maze.walk(dir)
      
  if maze.escaped():
    sense.clear(0, 255, 0)
    break;
        
