import numpy as np
import cv2
from sklearn.cluster import KMeans

col_range = (256, 256, 256)


def get_dominant_colors(image, quantity):
    '''
      Description: get the top <quantity> rgb colors of the given image
    '''
    cv_image = image.image

    # reshaping to a list of pixels
    pixels = cv_image.reshape((image.rows * image.columns, 3))

    kmeans = KMeans(quantity)
    kmeans.fit(pixels)

    colors = kmeans.cluster_centers_.astype(int)

    result = []
    for i in range(kmeans.n_clusters):
      indexes = np.where(kmeans.labels_ == i)[0]
      c_pixels = np.array([pixels[idx] for idx in indexes])

      mins = c_pixels.min(axis=0)
      maxes = c_pixels.max(axis=0)

      result.append(dict(
        mins=mins,
        maxes=maxes,
        center=colors[i]
      ))
    return result

#  rest of the page for DEBUG only
def sort_hsvs(hsv_list):
    """
    Sort the list of HSV values
    :param hsv_list: List of HSV tuples
    :return: List of indexes, sorted by hue, then saturation, then value
    """
    bars_with_indexes = []
    for index, hsv_val in enumerate(hsv_list):
        bars_with_indexes.append((index, hsv_val[0], hsv_val[1], hsv_val[2]))
    bars_with_indexes.sort(key=lambda elem: (elem[1], elem[2], elem[3]))
    return [item[0] for item in bars_with_indexes]


def make_bar(height, width, color):
    """
    Create an image of a given color
    :param: height of the image
    :param: width of the image
    :param: BGR pixel values of the color
    :return: tuple of bar, rgb values, and hsv values
    """
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv_bar[0][0]
    return bar, (red, green, blue), (hue, sat, val)


def display_colors(colors):
  # finally, we'll output a graphic showing the colors in order
  bars = []
  bars_with_range = []
  hsv_values = []
  for index, rows in enumerate(colors):
      bar, rgb, hsv = make_bar(100, 100, rows.get('center'))
      min_bar, min_rgb, min_hsv = make_bar(100, 30, rows.get('mins'))
      max_bar, max_rgb, max_hsv = make_bar(100, 30, rows.get('maxes'))

      print(f'Bar {index + 1}')
      print(f'  RGB values: {rgb}')
      print(f'  HSV values: {hsv}')
      hsv_values.append(hsv)
      bars.append(bar)
      bars_with_range.append(min_bar)
      bars_with_range.append(bar)
      bars_with_range.append(max_bar)

  # sort the bars[] list so that we can show the colored boxes sorted
  # by their HSV values -- sort by hue, then saturation
  sorted_bar_indexes = sort_hsvs(hsv_values)
  sorted_bars = [bars[idx] for idx in sorted_bar_indexes]

  cv2.imshow('Sorted by HSV values', np.hstack(sorted_bars))
  cv2.imshow(f'{len(colors)} Most Common Colors with minimum and maximum', np.hstack(bars_with_range))
  cv2.waitKey(0)
