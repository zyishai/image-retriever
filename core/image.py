import cv2 as cv
from core.color import Color
from core.pixel import Pixel

class Image:
  def __init__(self, path):
    self.image = cv.imread(path)
    (self.rows, self.columns, _) = self.image.shape
    self.flat_image = self.image.reshape(-1, self.image.shape[-1])

  def size(self):
    return (self.rows, self.columns)

  def pixelAt(self, col, row): # col=x, row=y
    if row >= len(self.image[0]) or col >= len(self.image) or row < 0 or col < 0:
      return None
    return Pixel(self, col, row, *self.image[row][col])

  # needs optimization for medium-large size images
  def ofColor(self, color):
    pixels = []
    for i, point in enumerate(self.flat_image):
      if Color(*point) == color:
        (row, col) = divmod(i, len(self.image[0]))
        pixels.append(Pixel(self, col, row, *point))
    return pixels