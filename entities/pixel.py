class Pixel:
  def __init__(self, image, x, y, label):
    self.image = image
    self.x = x
    self.y = y
    self.color = label

  def __eq__(self, other):
    return (
      self.x == other.x and 
      self.y == other.y and 
      self.color == other.color
    )

  def __add__(self, pos: tuple):
    return self.image.pixel_at(self.x + pos[0], self.y + pos[1])