#a dictionary linking a room to other room positions
rooms = {
            'Blue' : { 
                  'south' : 'Red',
                  'west'  : 'Yellow',
                },        

            'Red' : { 
                  'north' : 'Blue',
                },
                
            'Yellow' : { 
                  'east'  : 'Blue',
                  'south' : 'Green',
                },
                
            'Green' : {    
                }

         }
         
colours = { 'Blue' : [0, 0, 255], 
            'Red' : [255, 0, 0],
            'Yellow' : [255, 255, 0],
            'Green' : [0, 255, 0] 
          }

def start():
  #print a main menu and the commands
  print('Find the green room to escape.')
  showStatus()

def showStatus():
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom + ' room')
  print("---------------------------")
  
  if(currentRoom != 'Green'):
    print("Exits: ")
    print(*rooms[currentRoom].keys(), sep=', ')
  
def getColour():
  return colours[currentRoom]

#start the player in the middle
currentRoom = 'Blue'

def walk(dir):
  global currentRoom
  if dir in rooms[currentRoom]:
  #set the current room to the new room
    currentRoom = rooms[currentRoom][dir]
    print("You walk", dir)
  #there is no door (link) to the new room
  else:
    print('You can\'t go that way!')
    
  showStatus()
    
  return currentRoom
  
def escaped():
  return currentRoom == 'Green'
