from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(1,180):
  move(i)
  turn(2)
  color(colors[i%3])