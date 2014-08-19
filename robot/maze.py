from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def walk():
  for i in range (0, 1250):
    if touch == 'wall':
      turn(-90)
    else:
      move(1)
walk()
# Add your code here