import discap, os

client = discap.Client()

@client.ready
async def ready_event():
  print("Running")

#how to make a ready event

@client.message(pass_message=True)
async def message_event(msg):
  print(msg)
  print("MESSAGE CREATED")

#how to make a message event

@client.socket_res
async def socket_event():
  print("BIRUHEWQURHWUQER")

#how to make a socket event

@client.event(name="message_create", add=True)
async def message_event_replacement():
  print("HOLYYYY")

#how to add another message event

@client.event(name="socket_response", json=True)
async def socket_event(data):
  print("socket")
  print(data)

#how to make a socket_response event and receive JSON data instead of stupid objects 

client.run(os.getenv("TOKEN"), mobile=True)

#totally was not inspired by dpy
#debug kwarg is required to be True if you want to use socket_response event