#! /Users/yishaizehavi/.virtualenvs/cv/bin/python3

import multiprocessing as mp
from correlogram import specific_correlogram
from utils.colors import get_unique_colors
from adapters.cv_image import OpenCVImage
from utils.log import log_time

PROCESSES = mp.cpu_count() - 1

@log_time
def main():
  luffy = OpenCVImage('imgs/luffy.jpg')
  colors = get_unique_colors(luffy)

  print(f'Running with {PROCESSES} processes!')
  pool = mp.Pool(PROCESSES)

  def cb(result):
    for correlogram in result:
      print(correlogram)

  pool.starmap_async(specific_correlogram, map(lambda color: (luffy, color, color, 8), colors), callback=cb)
    
  pool.close()
  pool.join()

if __name__ == "__main__":
  main()