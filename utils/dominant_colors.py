import numpy as np

col_range = (256, 256, 256)

def get_dominant_colors(image, quantity):
    '''
      Description: get the top <quantity> rgb colors of the given image
    '''
    a1D = np.ravel_multi_index(image.flat_image.T, col_range)

    count_array = np.bincount(a1D)
    
    top_n = np.argpartition(count_array, -quantity)[-quantity:]

    return [np.unravel_index(n, col_range) for n in top_n]

