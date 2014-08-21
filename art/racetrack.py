
def direction_handle_keydown(key, currentDirection):
  if key=='left':
      return {"direction": currentDirection- 3, "key": key}
  elif key=='right':
    return {"direction": currentDirection +3, "key": key}
def direction_handle_keyup(key, currentDirection):
  return {"direction": currentDirection, "key": key}

  
  