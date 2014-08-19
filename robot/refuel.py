from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                           right_side)
turn(1)
count=1
for i in range (0, 400):
  for j in range (0,3):
    look()
    if look()=='fruit':
      while touch() !='fruit':
        move()
      move()
    elif touch()=='wall':
      if right_side()=='wall':
        turn(-1)
      elif left_side()=='wall':
        turn(1)
      else:
        turn(1)
    else:
      turn(count)
      count*=-1
  move()
    
# Add your code here