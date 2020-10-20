#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from core.correlogram import autocorrelogram
from utils.colors import get_unique_colors
from adapters.cv_image import OpenCVImage
from utils.log import log_time

import cv2 as cv

@log_time
def main():
  luffy = OpenCVImage('imgs/luffy_small.jpg')
  colors = get_unique_colors(luffy)
  
  # This code runs for ~2.5 secs for `luffy_small.jpg` and for ~10.6 secs for `luffy.jpg`.
  for color in colors:
    for i in range(1, 9):
      print(autocorrelogram(luffy, color, i))

if __name__ == "__main__":
  main()