
def direction_handle_keydown(key, currentDirection):
  if key=='left':
      return currentDirection- 3
  elif key=='right':
    return currentDirection +3
def acceleration_handle_keydown(key, Acc):
  if key== 'up':
    return Acc+2
  elif key== 'down':
    return Acc-2
def acceleration_handle_keyup(key, Acc):
   if key=='up':
      return Acc-1

  
  