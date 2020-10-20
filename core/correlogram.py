from core.gamma import gamma

# Eq. (11)
def specific_correlogram(image, src_color, target_color, distance):
  '''
    Description: calculate correlogram value for two colors and distance.
  '''
  pixels = image.of_color(src_color)
  numerator = gamma(pixels, src_color, target_color, distance)
  denominator = len(pixels) * 8 * distance

  return numerator / denominator

# Eq. (3)
def autocorrelogram(image, color, distance):
  return specific_correlogram(image, color, color, distance)

# Eq. (29)
def local_autocorrelogram(image, color, distance):
  pixels = image.of_color(src_color)
  numerator = gamma(pixels, color, color, distance)
  denominator = 8 * distance

  return numerator / denominator