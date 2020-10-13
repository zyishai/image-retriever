#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from correlogram import specific_correlogram
from utils.dominant_colors import get_unique_colors
from adapters.cv_image import OpenCVImage

def main():
  luffy = OpenCVImage('imgs/luffy.jpg')

  for color in get_unique_colors(luffy):
    print(specific_correlogram(luffy, color, color, 8))
  
  luffy.show_simplified()


if __name__ == "__main__":
  main()