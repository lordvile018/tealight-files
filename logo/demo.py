from tealight.logo import (move, 
                           turn, 
                           color)

colors = ["red", "green", "blue"]

for i in range(1,360):
  move(i)
  turn(20)
  color(colors[i%3])