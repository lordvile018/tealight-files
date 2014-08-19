from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                           right_side)
count=1
for i in range (0, 400):
  for j in range (0,3):
    look()
    if look()=='fruit':
      while touch() !='fruit':
        move()
      move()  
    else:
      turn(count)
      count*=-1
  move()
    
# Add your code here