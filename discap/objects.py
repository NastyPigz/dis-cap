
class ObjectBase:
  def __init__(self, id:int):
    self.id = id
    self.Route

class TextChannel(ObjectBase):
  def __init__(self, id:int):
    super().__init__(id)
  
  async def remove(self):
    pass