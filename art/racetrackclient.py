from tealight.net import connect, send
import tealight.utils
import random
userId= int(tealight.utils.now()) +random.randint(0,1000000)
connect("racetracktest")
send("connected")
#def regisrtation_handler(message):
  #for i in range (0, carNumber):
  #call draw car function and increment placement
  #horizontally? also change colour
def authenticated_send(data, to, type):
  data = {"to": to, "type": type, "payload": data, "user_id": userId}
  send(data)
  print "Just sent", data
  
  
authenticated_send(userId, "nope", "registration")
def handle_frame():
  authenticated_send(tealight.utils.now(), "server", "heartbeat")