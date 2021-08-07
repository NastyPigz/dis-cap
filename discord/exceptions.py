

class ParseTypeError(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class InvalidEvent(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class EventIndexFailure(Exception):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)