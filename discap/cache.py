from .exceptions import *

class Cache:
  def __init__(self, data:dict):
    self.payload = data
    self.bot_data = {}
  
  def parse_ready(self):
    if self.payload["t"] != "READY":
      raise ParseTypeError("Type was not valid 'READY'")
    self.bot_data["name"]=self.payload["d"]["user"]["username"]
    self.bot_data["id"]=self.payload["d"]["user"]["id"]
    self.bot_data["discriminator"]=self.payload["d"]["user"]["discriminator"]
    self.bot_data["avatar"]=self.payload["d"]["user"]["avatar"]
    guilds = self.payload["d"]["guilds"]
    for guild in guilds:
      index = guilds.index(guild)
      guilds[index].pop("unavailable")
    self.bot_data["guilds"]=guilds
    self.bot_data["application"]=self.payload["d"]["application"]["id"]
    return self
  
  def add_guild(self, payload:dict):
    if payload["t"] != "GUILD_CREATE":
      raise ParseTypeError("Type was not valid 'GUILD_CREATE'")
    payload = payload["d"]
    IDs = [i["id"] for i in self.bot_data["guilds"]]
    if payload["id"] in IDs:
      # print(payload)
      pass
    else:
      self.bot_data["guilds"].append({
        "id": payload["id"]
      })
    return self
