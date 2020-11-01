from numpy import where, asarray

class Image:
  def __init__(self, img):
    self.source = img

  # def pixel_at(self, col, row): # col=x, row=y
  #   if row >= len(self.source) or col >= len(self.source[0]) or row < 0 or col < 0:
  #     return None
  #   return self.source[row][col]

  def of_color(self, target_color):
    temp = where(self.source == target_color)
    return asarray(temp).T # [(y1, x1) ... (yn, xn)]

  def flatten(self):
    if not hasattr(self, '_flat'):
      self._flat = self.source.reshape(-1)
    return self._flat