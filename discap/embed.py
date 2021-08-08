import datetime

class Embed:
    def __init__(self, *, title:str=None, description:str=None, url:str=None, timestamp:datetime.datetime=None, color:int=None, footer:dict=None, fields:list=None):
        self.url = url
        self.timestamp=timestamp
        self.title = title
        self.color = color
        self.footer = footer
        self.fields = [i.to_dict() for i in fields]
        self.description=description
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "color": self.color,
            "footer": self.footer,
            "fields": self.fields,
            "timestamp": self.timestamp,
            "url": self.url
        }

class Field:
    def __init__(self, *, name:str, value:str, inline:bool=False):
        self.name = name
        self.value = value
        self.inline=inline
    
    def to_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "inline": self.inline
        }
