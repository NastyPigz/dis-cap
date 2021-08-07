import discord, os

client = discord.Client()

@client.ready
async def ready_event():
  print("Running")

@client.message
async def message_event():
  print("MESSAGE CREATED")

@client.event(name="message_create", add=True)
async def message_event_replacement():
  print("HOLYYYY")

@client.event(name="socket_response", json=True)
async def socket_event(data):
  print("socket")
  print(data)

client.run(os.getenv("TOKEN"), mobile=True, debug=True)