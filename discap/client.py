import aiohttp, asyncio, json, typing, datetime
from .cache import *
from .parse import *
from .exceptions import *

class Client:
  """
  The intents is maximum at default so too bad if you don't have presences or guild_members intents LMFAOOO go use a calculator noob
  """
  def __init__(self, *, intents:int=32767):
    self.payload = {
      'op': 2,
      "d": {
        "token": None,
        "properties": {
            "$os": "windows", # ios
            "$browser": "chrome", # Discord iOS
            "$device": 'pc' # stuff
        },
        "intents": intents
      }
    }
    self.DATA = {}
    self.ready_task = None
    self.client_tasks = {
      "on_message": [],
      "on_socket": [],
      "socket_json": False,
      "message_bool": False
    }
    self.session = aiohttp.ClientSession()
  
  def kill(self):
    exit(0)

  def get_guild(self, id:int):
    for guild in self.DATA.bot_data["guilds"]:
      if int(guild.id) == int(id):
        return guild
    return None

  def get_channel(self, id:int):
    for guild in self.DATA.bot_data["guilds"]:
      for channel in guild.channels:
        if int(channel.id) == int(id):
          return channel
    return None

  async def request(self, route: Route, *, json:dict):
    headers = {
      "Authorization": "Bot %s" % self.token
    }
    if route.method == "POST":
      response = await self.session.post(route.clean_url, json=json, headers=headers)
    elif route.method == "GET":
      response = await self.session.get(route.clean_url, json=json, headers=headers)
    try:
      respons = await response.json()
      try:
        global_rate = respons["global"]
        if global_rate:
          raise GlobalRateLimit("You are being rate limited globally. Please try again later")
        else:
          retry_after = respons["retry_after"]
          if retry_after > 119:
            print("A Request was Cancelled due to client being rate limited for more than 2 minutes.")
            return response
          await asyncio.sleep(retry_after)
          await self.request(route, json=json)
      except:
        return response
    except:
      raise Exception(f"So the response wasn't json format, it was {response}")

  def message(self, *, pass_message:bool=False):
    if pass_message:
      self.client_tasks["message_bool"]=pass_message
    def message(coro):
      self.client_tasks["on_message"]=[coro]
    return message

  def socket_res(self, coro):
    self.client_tasks["on_socket"]=[coro]

  def delete_event(self, *, name:str, order:int=0):
    if name == "message_create":
      actual_name = "on_message"
    elif name == "socket_response":
      actual_name = "on_socket"
    else:
      raise InvalidEvent(f"{name} is not a valid event!")
    try:
      self.client_tasks[actual_name].pop(order)
    except:
      raise EventIndexFailure(f"{order} out of range of registered {name} events")

  def event(self, *, name:str, add:bool=False, json:bool=False):
    if name == "message_create":
      if add:
        def add_message_task(coro):
          self.client_tasks["on_message"].append(coro)
      else:
        def add_message_task(coro):
          self.client_tasks["on_message"] = [coro]
      return add_message_task
    elif name == "socket_response":
      self.client_tasks["socket_json"]=json
      if add:
        def add_message_task(coro):
          self.client_tasks["on_socket"].append(coro)
      else:
        def add_message_task(coro):
          self.client_tasks["on_socket"] = [coro]
      return add_message_task

  def ready(self, coro):
    self.ready_task = coro

  def run(self, token:str, *, mobile:bool=False, debug:bool=False):
    self.token=token
    loop=asyncio.get_event_loop()
    loop.create_task(self.main_task(token, mobile=mobile, debug=debug))
    self.loop=loop
    loop.run_forever()

  async def main_task(self, token:str, *, mobile:bool=False, debug:bool=False):
    session = self.session
    ws = await session.ws_connect('wss://gateway.discord.gg/?v=9&encording=json')
    msg = await ws.receive()
    data = msg.json()
    heartbeat_interval = data['d']['heartbeat_interval'] / 1000
    self.loop.create_task(self.send_heart_beat(heartbeat_interval, ws,heartbeat=debug))
    payload = self.payload
    payload["d"]["token"]=str(token)
    if mobile:
      payload["d"]["properties"]={
        "$os": "ios",
        "$browser": "Discord iOS",
        "$device": 'discord.py'
      }
    await ws.send_json(self.payload)
    while True:
      data = await ws.receive()
      try:
        loads = data.json()
        if loads.get('t') == "READY":
          ready_msg = data
          break
      except TypeError:
        if data.extra == "Authentication failed.":
          await self.session.close()
          raise InvalidToken("Not a Valid Token")
    self.DATA = Cache(self, ready_msg.json()).parse_ready()
    if not self.ready_task is None:
      await self.ready_task()
    presence_payload = {
      "op": 3,
      "d": {
        "since": datetime.datetime.utcnow().timestamp(),
        "activities": [{
          "name": "MY ACTIVITY",
          "type": 0
        }],
        "status": "dnd",
        "afk": True
      }
    }
    await ws.send_json(presence_payload)
    while True:
      msg = await ws.receive()
      if debug:
        if len(self.client_tasks["on_socket"]) != 0:
          for task in self.client_tasks["on_socket"]:
            if not self.client_tasks["socket_json"]:
              await task(msg)
            else:
              try:
                await task(msg.json())
              except:
                await task(msg)
      try:
        self.DATA = Parsing(msg.json(), self.DATA, self.client_tasks, self.loop, self).parse()
      except Exception as e:
        print(e, "In Client, Parsing")
        raise e
        continue
  
  async def send_heart_beat(self, interval, session, *, heartbeat:bool=False):
    if heartbeat:
      print("%s is Heartbeat!" % interval)
    while True:
      try:
        await asyncio.sleep(interval)
        heartbeatJSON = {
            "op": 1,
            "d": "null"
        }
        if heartbeat:
          print("Heartbeat Sent!")
        await session.send_json(heartbeatJSON)
      except:
        break
    return True