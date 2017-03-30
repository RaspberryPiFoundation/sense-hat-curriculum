---
title: Compass Maze
description: Use the Sense HAT as a compass and navigate out of a maze. 
notes: "Treasure - notes.md"
layout: project
new: true
---

#Introduction:  { .intro}

In this project you will use the the Sense HAT as a compass to navigate out of a maze of colourful rooms. You will need to point the Sense HAT in the direction you want to move and then press the button in the middle of the joystick to make a move. 

<div class="trinket">
<iframe src="https://trinket.io/embed/python/79ac6a377d?outputOnly=true&start=result" width="600" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen>
</iframe>
<img src="images/compass-final.png">
</div>

To play the game press Run and read the text that appears in the trinket output window.

Your current compass direction will appear on the Sense HAT display (N, S, E or W.) You can change direction by moving the Sense HAT in the emulator. The easiest way to do this is to drag the 'yaw' slider. 

When you are facing in the direction you want to go, press the middle button on the joystick by pressing enter on the keyboard. 


#Step 1: Finding the compass direction{ .activity}

The Sense HAT contains a magnetometer that can be used to work out which direction is North. 

## Activity Checklist { .check}

In the emulator North corresponds to the top of your screen. 

Here's a reminder of the points of a compass:

   ![screenshot](images/compass-compass.png)

+ Open the Compass Maze Starter Trinket: <a href="http://jumpto.cc/compass-go" target="_blank">jumpto.cc/compass-go</a>. 

+ Add the following code to show the compass heading:
    
    ![screenshot](images/treasure-starter.png)
    
  This tells you how many degrees you are from facing north. 
  
  Make sure all your sliders are set to zero. 
  
  The Sense HAT is facing north.
  
  Notice that the Raspberry is the right way up. 
  
+ Drag the 'yaw' slider to the middle to rotate the Sense HAT 180 degrees. 

  Now the Sense HAT is facing south, towards the bottom of your screen. 
  
+ Drag the 'yaw' slider to 90. Now the Sense HAT is facing 90 degrees (clockwise) from north. This is east. 

+ And finally drag the 'yaw' slider to 270. The Sense HAT is facing west. 

    ![screenshot](images/compass-compass.png)
       
+ Try setting the 'yaw' slider to different values and make sure you understand which way the Sense HAT is facing. 


#Step 2: Showing the compass direction{ .activity}

Next let's show the compass direction on the Sense HAT screen. 

## Activity Checklist { .check}

+ First let's show an N on the screen when the Sense HAT is facing north. 

    ![screenshot](images/compass-north.png)
    
+ Now let's show an E on the screen when the Sense HAT is facing east. 


+ Complete the code for S and W. 

+ Your code should look like this:

+ Test your code by dragging the yaw slider. 

    You've made a Sense HAT compass. 
    

#Step 3: Navigating the maze { .activity}

Now let's use the compass to navigate around a maze.  

## Activity Checklist { .check}
    
+ The code for creating a simple adventure game (like the one in the RPG project) is in maze.py in your project. 

    You'll need to import `maze.py` to use it:

    ![screenshot](images/compass-import.png)
    
    `maze.py` includes some functions to help you write a maze game:
    
    + `maze.start()` - starts the game
    + `maze.escaped()` - tells you whether the player has escaped the maze
    + `maze.walk(dir)` - moves the player in the given direction  
    
+ Start the game with `maze.start()`:

    ![screenshot](images/compass-start.png)
    
#Step 4: Add colours { .activity}
It would be better if you could tell which room you were in just by looking at the Sense HAT. 

Let's display the compass letter in the colour of the current room. 

If you're in the Blue room and facing South you should see a blue letter S.

## Activity Checklist { .check}

+ First create a dictionary of colours for the rooms. 

   ![screenshot](images/compass-start.png)
   
+ Now use the colour of the current room when you display the compass letter:

   ![screenshot](images/compass-start.png)
   
+ Test your code and you should find that you can tell which room you're in from the colour of the letter. 
 
## Challenge: Reward the player

Can you reward the player with a cool display on the Sense HAT when they manage to escape? 
 
## Challenge: Create your own maze { .challenge}

Create your own colourful maze and get a friend to try and find their way out. 

    You'll need to:

    + Edit the rooms dictionary in maze.py
    + Add new colours the colours dictionary

