
def direction_handle_keydown(key, currentDirection):
  global Acc, currentDirection
  if key=='left':
      return currentDirection- 3
  elif key=='right':
    return currentDirection +3
def accelaration_handle_keydown(key):
  if key== 'up':
    Acc= Acc+2
  elif key== 'down':
    Acc== Acc-2
def x_handle_keyup(key):
   if key=='up':
      Acc=Acc-1
def Movement():
  global Acc
  Vel= Vel + Acc
  
  