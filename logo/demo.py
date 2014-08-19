from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(2,200):
  move(i)
  turn(73)
  color(colors[i%3])