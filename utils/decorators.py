from timeit import default_timer
from functools import wraps, update_wrapper

def log_time(fn):
  @wraps(fn)
  def run(*args, **kargs):
    start = default_timer()
    result = fn(*args, **kargs)
    print(f'{fn.__name__} runs: {default_timer() - start:.10f} secs.')
    return result
  
  return run

def memoize(fn):
  memo = {}
  
  @wraps(fn)
  def helper(*args):
    if args not in memo:
      memo[args] = fn(*args)
    return memo[args]
  return helper

class Accumulate:
  def __init__(self, fn):
    self.fn = fn
    # update attribute of the instance. 
    # Note: `help()` will return docstring of the *type* not of the *instance*. 
    # See here: https://stackoverflow.com/questions/25973376/functools-update-wrapper-doesnt-work-properly/25973438#25973438
    update_wrapper(self, fn)
    self.runs = 0

  def __call__(self, *args, **kwds):
    self.runs += 1
    return self.fn(*args, **kwds)

  def call_count(self):
    return self.runs