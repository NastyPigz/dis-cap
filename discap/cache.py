from .exceptions import *
from .guilds import *

#temp
import pprint

class Cache:
  def __init__(self, bot, data:dict):
    self.payload = data
    self.bot = bot
    self.bot_data = {}
  
  def parse_ready(self):
    if self.payload["t"] != "READY":
      raise ParseTypeError("Type was not valid 'READY'")
    self.bot_data["name"]=self.payload["d"]["user"]["username"]
    self.bot_data["id"]=self.payload["d"]["user"]["id"]
    self.bot_data["discriminator"]=self.payload["d"]["user"]["discriminator"]
    self.bot_data["avatar"]=self.payload["d"]["user"]["avatar"]
    self.bot_data["guilds"]=[]
    self.bot_data["application"]=self.payload["d"]["application"]["id"]
    return self
  
  def add_channel(self, payload:dict):
    if payload["t"] != "CHANNEL_CREATE":
      raise ParseTypeError("Type was not valid 'CHANNEL_CREATE'")
    payload = payload["d"]
    IDs = [i.id for i in self.bot_data["guilds"]]
    for i in IDs:
      if payload["guild_id"] == i:
        for r in self.bot_data["guilds"]:
          if r.id == payload["guild_id"]:
            break
        index = self.bot_data["guilds"].index(r)
        self.bot_data["guilds"][index].add_channel(payload)
    return self

  def add_guild(self, payload:dict):
    if payload["t"] != "GUILD_CREATE":
      raise ParseTypeError("Type was not valid 'GUILD_CREATE'")
    payload = payload["d"]
    IDs = [i.id for i in self.bot_data["guilds"]]
    if payload["id"] in IDs:
      index = self.bot_data["guilds"].index(i if i.id == payload["id"] else None for i in self.bot_data["guilds"])
      self.bot_data["guilds"][index]=ServerGuild(self.bot, payload)
    else:
      self.bot_data["guilds"].append(ServerGuild(self.bot, payload))
    return self
