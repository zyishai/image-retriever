import multiprocessing as mp
from functools import reduce
from correlogram.lambda_calc import horizontal_lambda, vertical_lambda
from utils.log import log_time

# Total running complexity O(4D(N^2)) -> O(D(N^2)).
@log_time
def gamma(pixels, src_color, target_color, distance):
  sum = 0
  print(f'Found {len(pixels)} pixels.')

  q = mp.Queue()

  def cb(lambda_sum):
    q.put(lambda_sum)

  with mp.Pool(mp.cpu_count() - 1) as p:
    p.starmap_async(vertical_lambda, map(lambda pixel: (pixel, distance), pixels), callback=cb)
    p.starmap_async(horizontal_lambda, map(lambda pixel: (pixel, distance), pixels), callback=cb)
    p.close()
    p.join()
  
  while not q.empty():
    results = q.get()
    sum += reduce(lambda a, b: a + b, results)
  
  return sum