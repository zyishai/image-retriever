from core.image import Image

# recursive approach
def horizontal_lambda(pixel, color, distance): # O(N) where distance=N
  if pixel is None:
    return 0
  if distance == 0:
    return int(pixel.color == color)

  return horizontal_lambda(pixel, color, distance - 1) + horizontal_lambda(pixel + (distance, 0), color, 0)

# iterative approach
def vertical_lambda(pixel, color, distance): # like horizontal_lambda but in an imperative style.
  sum = 0
  for d in range(distance + 1): # runs between 0 to distance inclusive
    if pixel is None:
      continue
    p = pixel + (0, d)
    if p is None:
      continue
    if p.color == color:
      sum += 1

  return sum