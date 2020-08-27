import cv2 as cv
from core.color import Color
from core.pixel import Pixel

class Image:
  def __init__(self, path):
    self.image = cv.imread(path)
    (self.rows, self.columns, _) = self.image.shape
    # self.flat_image = self.image.reshape(-1, self.image.shape[-1])

  def size(self):
    return (self.rows, self.columns)

  def pixel_at(self, col, row) -> Pixel: # col=x, row=y
    if row >= len(self.image[0]) or col >= len(self.image) or row < 0 or col < 0:
      return None
    return Pixel(self, col, row, channels=self.image[row][col])

  # needs optimization for medium-large size images
  def of_color(self, target_color):
    pixels = []
    for row_index, row in enumerate(self.image):
      for col_index, channels in enumerate(row):
        color = Color(*channels)
        if color == target_color:
          pixels.append(Pixel(self, col_index, row_index, color=color))
    return pixels