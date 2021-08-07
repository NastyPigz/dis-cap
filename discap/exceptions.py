
class InvalidToken(Exception):
  """
  Get ya stupid token
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class GlobalRateLimit(Exception):
  """
  Smh stop spamming
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class ParseTypeError(Exception):
  """
  TypeError during Parsing !!1!!
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class InvalidEvent(Exception):
  """
  Our events are kool!1! you mess it up
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

class EventIndexFailure(Exception):
  """
  You never registered this many events
  """
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)