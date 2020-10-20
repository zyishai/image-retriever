from core.gamma import gamma

# Eq. (3) & (11)
def autocorrelogram(image, color, distance):
  pixels = image.of_color(src_color)
  numerator = gamma(pixels, distance)
  denominator = len(pixels) * 8 * distance

  return numerator / denominator

# Eq. (29)
def local_autocorrelogram(image, color, distance):
  pixels = image.of_color(src_color)
  numerator = gamma(pixels, distance)
  denominator = 8 * distance

  return numerator / denominator

def corr_contribution(sub_image, query_image):
  pass