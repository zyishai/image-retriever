class Pixel:
  def __init__(self, image, x, y, label):
    self.image = image
    self.x = x
    self.y = y
    self.color = label

  # these 3 methods not in use currently
  def __eq__(self, other):
    return (
      self.x == other.x and 
      self.y == other.y and 
      self.color == other.color
    )

  def __add__(self, pos: tuple):
    return self.image.pixel_at(self.x + pos[0], self.y + pos[1])

  def __getitem__(self, key):
    if key == 0:
      return self.x
    elif key == 1:
      return self.y
    else:
      raise AttributeError('Key must be 0 for x or 1 for y.')