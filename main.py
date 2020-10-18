#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from correlogram import specific_correlogram
from utils.colors import get_unique_colors
from adapters.cv_image import OpenCVImage
from utils.log import log_time

@log_time
def main():
  luffy = OpenCVImage('imgs/luffy.jpg')
  colors = get_unique_colors(luffy)

  for color in colors:
    print(specific_correlogram(luffy, color, color, 8))

if __name__ == "__main__":
  main()