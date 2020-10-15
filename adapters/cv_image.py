from cv2 import imread, imshow, waitKey, destroyAllWindows
from numpy import copy as np_copy, array as np_array, uint8
from core.image import Image
from utils.cluster import get_cluster

class OpenCVImage(Image):
  def __init__(self, path):
    self.cv_image = imread(path)
    self.cluster = get_cluster(self.cv_image, 8)
    numeric_repr = np_copy(self.cluster.labels_)
    super().__init__(numeric_repr.reshape(self.cv_image.shape[:-1]))

  def show_simplified(self):
    colors = self.cluster.cluster_centers_.astype(int)
    numeric_repr = np_copy(self.cluster.labels_)
    colored_flat_repr = np_array([
        colors[cell]
        for idx, cell in enumerate(numeric_repr)
    ], dtype=uint8)
    displayed_image = colored_flat_repr.reshape(self.cv_image.shape)
    imshow('Simplified Colored Image', displayed_image)
    waitKey(0)
    destroyAllWindows()