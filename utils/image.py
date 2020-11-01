from cv2 import rectangle, imshow, waitKey, destroyAllWindows
from numpy import unique

def get_unique_colors(image): # image is an `Image` entity
    return unique(image.flatten())

def draw_rect(image, offset, dimensions, title="Result", borderColor=(0,0,255), borderWidth=2): # image is an `open cv` image
  width, height = dimensions
  end = (offset[0] + width, offset[1] + height)
  rectangle(image, offset, end, borderColor, borderWidth)
  imshow(title, image)
  waitKey(0)
  destroyAllWindows()