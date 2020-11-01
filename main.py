#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from core import locate
from adapters.cv_image import OpenCVImage
from utils.image import draw_rect
from utils.decorators import log_time

@log_time
def main():
  image = OpenCVImage('imgs/luffy.jpg')
  template = OpenCVImage('imgs/luffy2_small.jpg', cluster=image.cluster)

  max_contribution, max_offset = locate(image, template)
  print(f'Max contribution: {max_contribution} at {max_offset}.')
  draw_rect(image.cv_image, max_offset, template.dimensions())

if __name__ == "__main__":
  main()