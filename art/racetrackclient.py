from tealight.net import connect, send
import tealight.utils
import random
userId= int(tealight.utils.now()) +random.randint()
connect("racetracktest")
send("connected")
def regisrtation_handler(message):
  for i in range (0, carNumber):
  #call draw car function and increment placement
  #horizontally? also change colour
send (userId)