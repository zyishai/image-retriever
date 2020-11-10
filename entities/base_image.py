from numpy import where, asarray

class BaseImage:
  def __init__(self, source):
    self.source = source

  def of_color(self, target_color):
    temp = where(self.source == target_color)
    return asarray(temp).T # [(y1, x1) ... (yn, xn)]

  def flatten(self):
    if not hasattr(self, '_flat'):
      self._flat = self.source.reshape(-1)
    return self._flat