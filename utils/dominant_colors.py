from sklearn.cluster import KMeans
import numpy as np
from core.image import Image

def get_cluster(image: np.ndarray, quantity):
    # reshaping to a list of pixels
    pixels = image.reshape((-1, 3))

    kmeans = KMeans(quantity)
    kmeans.fit(pixels)

    return kmeans

def get_unique_colors(image: Image):
    flat_image = image.source.reshape(-1)
    return np.unique(flat_image)