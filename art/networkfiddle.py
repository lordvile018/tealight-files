from tealight.net import connect, send
connect("networkfiddle2")
send ('hi' )
def handle_message(message):
  print message
  