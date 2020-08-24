from correlogram.gamma import gamma

def specific_correlogram(image, src_color, target_color, distance):
  '''
    Description: calculate correlogram value for two colors and distance.
  '''
  numerator = gamma(image, src_color, target_color, distance)
  denominator = len(image.ofColor(src_color)) * 8 * distance

  return numerator / denominator

def basic_correlogram():
  pass