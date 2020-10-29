from core.histogram import hist_contribution
from core.correlogram import corr_contribution
from itertools import product

def locate(image, template, beta=0.5):
  tmpl_dim = template.dimensions()
  offsets = get_offsets(image, template) # shape of each element: (x, y)
  max_contribution = float('-inf')
  max_offset = (0, 0)

  for offset in offsets:
    search_image = image.get_sub_image(offset, tmpl_dim)
    search_image_hist = image.get_hist_sub_image(offset, tmpl_dim)
    c1 = hist_contribution(search_image_hist, template.histogram)
    c2 = corr_contribution(search_image, template)
    contribution = beta * c1 + (1 - beta) * c2
    if contribution > max_contribution:
      max_contribution = contribution
      max_offset = offset

  return max_contribution, max_offset

def get_offsets(source_image, query_image, step=4):
  source_width, source_height = source_image.dimensions()
  query_width, query_height = query_image.dimensions()

  x_offsets = source_width - query_width
  y_offsets = source_height - query_height

  return product(range(0, x_offsets, step), range(0, y_offsets, step)) # returns: [(x1, y1) ... (xn, yn)]