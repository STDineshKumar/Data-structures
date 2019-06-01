import timeit
import numpy as np
from merge_sort import merge
from merge_sort import merge_sort

# Decorator to pass arguments fot mege sort.
def wrapper(func, *args, **kwargs):
        def wrapped():
                return func(*args, **kwargs)
        return wrapped

if __name__ == '__main__':
        a = np.random.randint(1,high=100,size=100, dtype=np.int64)
        a = list(a)
        wrapped_ = wrapper(merge_sort, a)
        print(timeit.timeit(wrapped_, number= 1000))
