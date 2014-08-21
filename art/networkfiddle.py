from tealight.net import connect, send
connect("networkfiddle")
send ('hi')
def handle_message(message):
  print "recieved message" +message
  