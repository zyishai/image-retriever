from utils.image import get_unique_colors
from core.gamma import gamma
from utils.decorators import memoize

# Eq. (3) & (11)
@memoize
def autocorrelogram(image, color, distance_set):
  pixels = image.of_color(color) # (y, x)
  if len(pixels) == 0:
    return 0
  numerator = gamma(pixels, distance_set)
  denominator = len(pixels) * 8 * sum(distance_set)

  return numerator / denominator

# Eq. (29)
def local_autocorrelogram(image, color, distance_set):
  pixels = image.of_color(color) # (y, x)
  if len(pixels) == 0:
    return 0
  numerator = gamma(pixels, distance_set)
  denominator = 8 * sum(distance_set)

  return numerator / denominator

def corr_contribution(sub_image, query_image, distance_set=(1, 3, 5)):
  result = 0;
  colors = get_unique_colors(sub_image)
  for color in colors:
    a = autocorrelogram(query_image, color, distance_set)
    b = local_autocorrelogram(sub_image, color, distance_set)
    result += (a - b)
  return result