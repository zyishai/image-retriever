#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from core.image import Image
from correlogram import specific_correlogram
from utils import dominant_colors

def main():
  img = Image('imgs/luffy.jpg')
  p1 = img.pixel_at(15, 69)
  print(p1.color.unpack(format="rgb"))
  print(dominant_colors.get_dominant_colors(img, 20))
  print("\nPress ENTER or any key to close the preview")
  p1.DEBUG_display_on_image()


if __name__ == "__main__":
  main()