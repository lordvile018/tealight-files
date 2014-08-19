from tealight.logo import move, turn

def chessboard():
  for i in range(0,1):
    move(80)
    turn(90)
    if i % 2 == 0:
        move(10)
        turn(90)
    else:
        move(10)
        turn(-90)
        
chessboard()