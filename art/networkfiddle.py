from tealight.net import connect, send
connect("networkfiddle")
send ('hi', echo= False)
def handle_message(message):
  print "recieved message" +message
  