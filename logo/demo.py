from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(180):
  move(i)
  turn(360)
  color(colors[i%3])