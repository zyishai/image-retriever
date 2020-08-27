#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from core.image import Image
from correlogram import specific_correlogram

def main():
  img = Image('imgs/luffy.jpg')
  p1 = img.pixel_at(15, 69)
  print(p1.color.unpack(format="rgb"))
  p1.DEBUG_display_on_image()


if __name__ == "__main__":
  main()