from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
def walk():
  for i in range (0, 1250):
    if touch()=='wall':
       
       if right_side() == None:
            turn(45)
            move()
       elif right_side()=='wall':
         turn(-45)
         move()
       else:
          turn(45)
          move()
    
    else:
      move()
walk()
# Add your code here