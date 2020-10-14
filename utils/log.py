from timeit import default_timer

def log_time(fn):
  def run(*args, **kargs):
    start = default_timer()
    result = fn(*args, **kargs)
    print(f'{fn.__name__} runs: {default_timer() - start} secs.')
    return result
  
  return run