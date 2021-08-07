
class Route:
  def __init__(self, *, v=9, method:str="GET", url:str):
    self.base = f"https://discord.com/api/v{v}"
    # self.baseheaders = {
    #   "Authorization": f"Bot {token}"
    # }
    self.method = method
    self.url=url
    self.clean_url=self.base+self.url