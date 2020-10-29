from numpy import concatenate, where, maximum, isin

# Total running complexity O(4D(N^2)) -> O(D(N^2)).
def gamma(pixels, distance_set):
  dist = concatenate(list(map(lambda pixel: abs(pixels - pixel), pixels)))
  return len(where(isin(maximum(dist[:, 0], dist[:, 1]), distance_set))[0])