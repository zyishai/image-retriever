class Color:
  def __init__(self, *channels):
    self.blue = channels[0]
    self.green = channels[1]
    self.red = channels[2]
  
  def unpack(self, format="bgr"):
    color_format_dict = {
      'r': self.red,
      'g': self.green,
      'b': self.blue
    }
    
    result = []
    for channel in format:
      result.append(color_format_dict[channel])
    
    return tuple(result)

  def __eq__(self, other):
    return (
      self.red == other.red and
      self.green == other.green and
      self.blue == other.blue
    )