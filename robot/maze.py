from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)



def walk():
  for i in range (0, 1250):
    if left_side() == None:
            turn(-1)
            move()
    if touch()=='wall':
       if left_side()=='wall':
         turn(1)
         move()
       else:
          turn(-1)
          move()
    
    else:
      move()
walk()
# Add your code here