from core.pixel import Pixel

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
    pixels = []
    for row_index, row in enumerate(self.source):
      for col_index, color in enumerate(row):
        if color == target_color:
          pixels.append(Pixel(self, col_index, row_index, color))
    return pixels