def handle_keydown(key):
  if key='left':
    currentDirection= currentDirection- 3
  elif key='right':
    currentDirection= currentDirection +3
  elif key= 'up':
    Acc= Acc+2
  elif key= 'down':
    Acc= Acc-2
def handle_keyup(key):
   if key='up':
      Acc=Acc-1
Vel= Vel + Acc