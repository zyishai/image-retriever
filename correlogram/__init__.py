from correlogram.gamma import gamma

def specific_correlogram(image, src_color, target_color, distance):
  '''
    Description: calculate correlogram value for two colors and distance.
  '''
  pixels = image.of_color(src_color)
  numerator = gamma(pixels, src_color, target_color, distance)
  denominator = len(pixels) * 8 * distance

  return numerator / denominator

def basic_correlogram():
  pass