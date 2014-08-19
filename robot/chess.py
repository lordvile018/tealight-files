from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
for i in range (0,700):
  if look()=='fruit':
    while touch()!= 'fruit':
      move()
    move()
  else:
    turn(1)
# Add your code here