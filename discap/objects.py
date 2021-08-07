from .routing import *

class Message:
  def __init__(self, bot, payload):
    self.channel = None #insert get_channel shit here
    self.bot = bot
    self.payload = payload
    self.content = payload["content"]
    self.author = MessageAuthor(payload)

  async def send(self, content:str):
    channel_id = self.payload["channel_id"]
    response = await self.bot.request(
      Route(method="POST", url=f"/channels/{channel_id}/messages"),
      json={
        "content": content
      }
    )
    return response

class MessageAuthor:
  def __init__(self, payload):
    npd = payload["author"]
    self.id = int(npd["id"])
    self.avatar = npd["avatar"]
    self.discriminator= npd["discriminator"]
    self.name = npd["username"]

class User:
  def __init__(self, payload):
    npd = payload["user"]
    self.id = int(npd["id"])
    self.avatar = npd["avatar"]
    self.discriminator= npd["discriminator"]
    self.name = npd["username"]

class Member(User):
  def __init__(self, payload):
    super().__init__(payload)
    self.roles = payload["roles"]
    self.joined_at = payload["joined_at"]
    self.nickname = None if not payload["nick"] else payload["nick"]

class DiscordChannel:
  def __init__(self, payload):
    self.payload = payload
    self._type = payload["type"]
    self.id = int(payload["id"])
    self.name = payload["name"]
    if self._type == 4:
      self.type=CategoryChannel
    elif self._type == 0:
      self.type=TextChannel
    elif self._type == 2:
      self.type=VC
    elif self._type == 1:
      self.type=PrivateMessage
    elif self._type == 3:
      self.type="Unavailable #GroupDM"
    elif self._type == 5:
      self.type="Unavailable #NEWS"
    elif self._type == 6:
      self.type="Unavailable #STORE"
    elif self.type == 10 or self.type == 11 or self.type == 12:
      self.type=Thread

class Thread(DiscordChannel):
  pass

class PrivateMessage(DiscordChannel):
  pass

class VC(DiscordChannel):
  pass

class TextChannel(DiscordChannel):
  pass

class CategoryChannel(DiscordChannel):
  pass
