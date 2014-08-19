from tealight.logo import move, turn

def chessboard():
  for i in range(0,1):
    move(80)
    turn(90)
    move(10)
    turn(90)
chessboard()