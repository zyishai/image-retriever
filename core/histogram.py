from numpy import sum as np_sum, nan_to_num, minimum

# Eq. (25)-(26)
def hist_contribution(sub_image, query_image): # images should be in *histogramic* representation.
  return np_sum(minimum(nan_to_num(sub_image / query_image), 1))