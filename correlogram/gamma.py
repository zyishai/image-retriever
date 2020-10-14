from correlogram.lambda_calc import horizontal_lambda, vertical_lambda

# Total running complexity O(4D(N^2)) -> O(D(N^2)). read ahead to understand why.
def gamma(image, src_color, target_color, distance):
  sum = 0
  pixels = image.of_color(src_color)

  for pixel in pixels: # O(N^2) if image size is NxN. Generally, NxM.
    # O(D) for each sum+=... line, where distance=D
    sum += vertical_lambda(pixel + (-distance, -distance + 1), target_color, 2 * distance - 2)
    sum += horizontal_lambda(pixel + (-distance, -distance), target_color, 2 * distance)
    sum += horizontal_lambda(pixel + (-distance, distance), target_color, 2 * distance)
    sum += vertical_lambda(pixel + (distance, -distance + 1), target_color, 2 * distance - 2)
  
  return sum