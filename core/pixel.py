from cv2 import rectangle as cv_rect, imshow, waitKey
from core.color import Color

class Pixel:
  def __init__(self, image, x, y, **opts):
    self.image = image
    self.x = x
    self.y = y
    self.color = opts.get('color') if 'color' in opts else Color(*opts.get('channels'))

  def DEBUG_display_on_image(self, title="Image"):
    start_point = (self.x - 5, self.y - 5)
    end_point = (self.x + 5, self.y + 5)
    imshow(title, cv_rect(self.image.image, start_point, end_point, (0, 0, 0), 5))
    waitKey(0)

  def __eq__(self, other):
    return (
      self.x == other.x and 
      self.y == other.y and 
      self.color == other.color
    )

  def __add__(self, pos: tuple):
    return self.image.pixel_at(self.x + pos[0], self.y + pos[1])