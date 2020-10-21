from cv2 import imread, imshow, waitKey, destroyAllWindows
from numpy import copy as np_copy, array as np_array, uint8, isnan
from fast_histogram import histogram1d
from entities.image import Image
from utils.cluster import get_cluster, apply_cluster

class OpenCVImage(Image):
  def __init__(self, path, cluster = None):
    self.cv_image = imread(path) # load image from disk.

    numeric_repr = self._set_cluster(cluster) # flat.
    
    super().__init__(numeric_repr.reshape(self.cv_image.shape[:-1])) # initialize parent class.

    self._set_histogram() # calculate `histogram` property. 2d array.

  def _set_cluster(self, cluster=None):
    if cluster is None:
      self.cluster = get_cluster(self.cv_image, 8)
      return np_copy(self.cluster.labels_)
    else:
      self.cluster = cluster
      return apply_cluster(self.cv_image, self.cluster)
    
  def _set_histogram(self):
    hist_values = histogram1d(self.source, bins=8, range=[0, 8])
    def to_hist_value(color):
      return hist_values[color]

    self.histogram = np_array(to_hist_value(self.source))

  def get_hist_sub_image(self, offset, width, height):
    x, y = offset
    return self.histogram[y:y+height, x:x+width]

  def get_sub_image(self, offset, width, height):
    x, y = offset
    return Image(self.source[y:y+height, x:x+width])

  def show_simplified(self):
    colors = self.cluster.cluster_centers_.astype(uint8)
    def to_color(cell):
      return colors[cell]

    displayed_image = to_color(self.source)
    imshow('Simplified Colored Image', displayed_image)
    waitKey(0)
    destroyAllWindows()