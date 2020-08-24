#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

from core.image import Image
from correlogram import specific_correlogram

def print_result(func):
  def inner(*args, **kargs):
    print("Calculating...")
    result = func(*args, **kargs)
    print(f"Result: {result}")
  return inner

@print_result
def main():
  # Example run. Result: 0.04375
  img = Image('imgs/luffy.jpg')
  p1 = img.pixelAt(5, 6)
  p2 = img.pixelAt(3, 9)
  return specific_correlogram(img, p1.color, p2.color, 5)


if __name__ == "__main__":
  main()