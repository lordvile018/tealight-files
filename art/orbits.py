from tealight.art import (color, line, spot, circle, box, image, text, background)

x = 600
y = 400
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3
grav=0.2
mu=0.1
def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    ax = -power
  elif key == "right":
    ax = power
  elif key == "up":
    ay = (-power)+ (grav)
  elif key == "down":
    ay = power + grav

def handle_keyup(key):
  global ax, ay
  
  if key == "left" or key == "right":
    while ax!=0:
      if key=='left':
        ax = ax + mu
        if ax > 0:
          ax=0
      if key=='right':
        ax = ax - mu
        if ax < 0:
          ax=0
    
  elif key == "up" or key == "down":
    ay = grav
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  