from scipy.spatial.distance import cdist
from numpy import isin

# Total running complexity O(4D(N^2)) -> O(D(N^2)).
def gamma(pixels, distance_set):
  distances = cdist(pixels, pixels, metric='chebyshev')
  return len(distances[isin(distances, distance_set)])