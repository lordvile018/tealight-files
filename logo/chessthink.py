from tealight.logo import move, turn

def chessboard():
  for i in range(0,8):
    if i % 2 == 0:
      move(80)
      turn(90)
    else:
        move(80)
        turn(-90)
    if i % 2 == 0:
        move(10)
        turn(90)
    else:
        move(10)
        turn(-90)
  move(80)
  turn(-90)     
  for i in range(0,8):
    if i % 2 == 0:
      move(80)
      turn(90)
    else:
      move(80)
      turn(-90)
    if i % 2 == 0:
      move(-10)
      turn(90)
    else:
      move(-10)
      turn(-90)
  move(80)
  shading()
def shading():
  for i in range(0,8):
    if i % 2 == 0:
      move(10)
      turn(-90)
    else:
        move(10)
        turn(90)
    if i % 2 == 0:
        move(1)
        turn(-90)
    else:
        move(1)
        turn(90)
  move(10)
  turn(90)     
  for i in range(0,8):
    if i % 2 == 0:
      move(10)
      turn(-90)
    else:
      move(10)
      turn(90)
    if i % 2 == 0:
      move(-1)
      turn(-90)
    else:
      move(-1)
      turn(90)
  move(10)
chessboard()
