
def direction_handle_keydown(key, currentDirection):
  if key=='left':
      return {"direction": currentDirection- 3, "key": key}
  elif key=='right':
    return {"direction": currentDirection +3, "key": key}
def acceleration_handle_keydown(key, Acc):
  if key== 'up':
    return Acc+2
  elif key== 'down':
    return Acc-2
def acceleration_handle_keyup(key, Acc):
   if key=='up':
      return Acc-1

  
  