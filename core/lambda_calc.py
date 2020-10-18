def vertical_lambda(pixel, distance): # like horizontal_lambda but in an imperative style.
  sum = 0
  for i in range(0, 2 * distance - 1): # 0 ... 2k-2 times
    y_index = pixel.y - distance + 1 + i
    if y_index >= len(pixel.image.source) or y_index < 0:
      continue
    if pixel.x - distance >= 0:
      sum += int(pixel.color == pixel.image.source[y_index][pixel.x - distance])
    if pixel.x + distance < len(pixel.image.source[0]):
      sum += int(pixel.color == pixel.image.source[y_index][pixel.x + distance])

  return sum

def horizontal_lambda(pixel, distance): # like horizontal_lambda but in an imperative style.
  sum = 0
  for i in range(0, 2 * distance + 1): # 0 ... 2k times
    x_index = pixel.x - distance + i
    if x_index >= len(pixel.image.source[0]) or x_index < 0:
      continue
    if pixel.y - distance >= 0:
      sum += int(pixel.color == pixel.image.source[pixel.y - distance][x_index])
    if pixel.y + distance < len(pixel.image.source):
      sum += int(pixel.color == pixel.image.source[pixel.y + distance][x_index])

  return sum