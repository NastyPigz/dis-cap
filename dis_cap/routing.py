
class Route:
  def __init__(self, *, v=9, token:str):
    self.base = "https://discord.com/api/v9"
    self.baseheaders = {
      "Authorization": f"Bot {token}"
    }
  
  @property
  def fucking_URL(self):
    return "be polite"