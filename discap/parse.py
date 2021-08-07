from .cache import *
from .objects import *

class Parsing:
  def __init__(self, payload: dict, obj: Cache, tasks, loop):
    self.payload = payload
    self.object = obj
    self.tasks = tasks
    self.loop = loop
  
  def parse(self):
    received_type = self.payload["t"]
    if received_type == "GUILD_CREATE":
      object_ = self.object.add_guild(self.payload)
    elif received_type == "MESSAGE_CREATE":
      if not len(self.tasks["on_message"]) == 0:
        async def task():
          for task in self.tasks["on_message"]:
            if self.tasks["message_bool"]:
              await task("no message haha noob")
            else:
              await task()
        self.loop.create_task(task())
      object_ = self.object
    else:
      object_ = self.object
    return object_