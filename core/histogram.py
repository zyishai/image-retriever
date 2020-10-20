from itertools import product
from numpy import sum as np_sum, nan_to_num
from entities.image import Image

def get_offsets(source_image: Image, query_image: Image):
  source_height, source_width = source_image.source.shape
  query_height, query_width = query_image.source.shape

  x_offsets = source_width - query_width
  y_offsets = source_height - query_height

  return product(range(x_offsets), range(y_offsets)) # returns: [(x1, y1) ... (xn, yn)]

def hist_contribution(sub_image, query_image): # images should be in *histogramic* representation.
  return np_sum(nan_to_num(sub_image / query_image))