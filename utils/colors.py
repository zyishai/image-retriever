import numpy as np
from entities.image import Image

def get_unique_colors(image: Image):
    flat_image = image.source.reshape(-1)
    return np.unique(flat_image)