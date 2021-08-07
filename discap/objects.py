
class ObjectBase:
  def __init__(self, id:int):
    self.id = id
  
  def fuck(self):
    print("FUCK!")

class TextChannel(ObjectBase):
  def __init__(self, id:int):
    super().__init__(id)
  
  async def delete(self):
    