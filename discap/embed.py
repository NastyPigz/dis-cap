
class Embed:
    def __init__(self, *, title:str=None, description:str=None):
        self.title = title
        self.description=description
    
    def to_dict(self):
        return self