import discap, os

client = discap.Client()

@client.ready
async def ready_event():
  print("Running")

#how to make a ready event

@client.message(pass_message=True)
async def message_event(msg):
  pass

#how to make a message event

client.message(pass_message=True)

#enable pass_message manually

@client.socket_res
async def socket_event(data):
  print(data)

#how to make a socket event

@client.event(name="message_create", add=True)
async def message_event_replacement(msg):
  if msg.author.id == 824637996632113152:
    return
  if msg.content.lower() == "!help":
    await msg.send("Help is here!", embeds=[discap.Embed(title="Help Menu", description="help", fields=[discap.Field(name="bruh", value='Let go')])])
    await msg.channel.send("bahahhaha", reference=discap.MR.reply_message(msg, retry=True), allowed_mentions=discap.AM.reply(False))
    await msg.reply("<@763854419484999722>", allowed_mentions=discap.AM.no())

@client.event(name="message_create", add=True)
async def command1(msg):
  if msg.content.lower() == "!gc":
    await msg.send(msg.guild.channels)

#how to add another message event, u can add up to infinite

@client.event(name="socket_response", json=True, add=True)
async def socket_event(data):
  pass

#how to make a socket_response event and receive JSON data instead of stupid objects (using JSON kwarg)

prefix = "!"

@client.event(name="message_create", add=True)
async def commands_handler(msg):
  if msg.content.lower().startswith(prefix): # or if msg.content.lower() in prefixes if you have a list of prefix
    args = msg.content[len(prefix):].split(" ") #this is subjected to change if you are using a list of prefixes
    print(args)
    command = args.pop(0).lower()
    if command == "ping": #this will be easier with python 3.10's match and case.
      await msg.send("Pong!")

#example of a command handler.

client.run("ODI0NjM3OTk2NjMyMTEzMTUy.YFyR-w.H_I-65EswO836IcMo-Dilq9k8FA", mobile=True)

#totally was not inspired by dpy
#debug kwarg is required to be True if you want to use socket_response event