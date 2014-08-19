from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

turn(6)

def walk():
  for i in range (0, 1250):
    if touch()=='wall':
       
       if right_side() == None:
            turn(1)
            move()
       elif right_side()=='wall':
         turn(-1)
         move()
       else:
          turn(1)
          move()
    
    else:
      move()
walk()
# Add your code here