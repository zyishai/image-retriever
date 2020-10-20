from core.lambda_calc import horizontal_lambda, vertical_lambda
from utils.log import log_time

# Total running complexity O(4D(N^2)) -> O(D(N^2)).
@log_time
def gamma(pixels, src_color, target_color, distance): # Eq. (10)
  sum = 0

  for pixel in pixels:
    sum += vertical_lambda(pixel, distance)
    sum += horizontal_lambda(pixel, distance)
  
  return sum