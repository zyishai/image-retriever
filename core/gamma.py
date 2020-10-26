from numpy import concatenate, where, maximum
from utils.log import log_time

# Total running complexity O(4D(N^2)) -> O(D(N^2)).
# @log_time
def gamma(pixels, distance):
  dist = concatenate(list(map(lambda pixel: abs(pixels - pixel), pixels)))
  return len(where(maximum(dist[:, 0], dist[:, 1]) == distance))