from fast_histogram import histogram1d
from numpy import uint

def ratio_histogram(image, query_image, color):
  Q = histogram_for(query_image)[color]
  I = histogram_for(image)[color]
  return min(Q / I, 1)

def histogram_for(image):
  # NOTE: `bins` and `range` hardcoded!
  return histogram1d(image, bins=8, range=[0,7]).astype(uint) / image.size