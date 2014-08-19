from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(2,130):
  move(i)
  turn(73)
  color(colors[i%4])