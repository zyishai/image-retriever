from entities.pixel import Pixel
from numpy import where

class Image:
  def __init__(self, img):
    self.source = img
    (self.rows, self.columns) = self.source.shape

  def size(self):
    return (self.rows, self.columns)

  def pixel_at(self, col, row) -> Pixel: # col=x, row=y
    if row >= len(self.source) or col >= len(self.source[0]) or row < 0 or col < 0:
      return None
    return Pixel(self, col, row, self.source[row][col])

  def of_color(self, target_color):
    temp = where(self.source == target_color)
    indices = zip(temp[1], temp[0]) # [(x1, y1) ... (xn, yn)]
    return map(lambda index: Pixel(self, index[0], index[1], target_color), indices)

  def flatten(self):
    if not hasattr(self, '_flat'):
      self._flat = self.source.reshape(-1)
    return self._flat