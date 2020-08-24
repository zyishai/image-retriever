class Color:
  def __init__(self, *colors):
    self.red = colors[0]
    self.green = colors[1]
    self.blue = colors[2]
  
  def unpack(self):
    return (self.red, self.green, self.blue)
  
  def __eq__(self, other):
    return (
      self.red == other.red and
      self.green == other.green and
      self.blue == other.blue
    )