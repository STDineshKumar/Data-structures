import timeit
from random import randrange
from quick_sort import qsort
import numpy as np

def wrapper(func, *args, **kwargs):
    def wrapper():
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper

if __name__ == "__main__":
    a = np.random.randint(0, high=100, size=100, dtype=np.int64)
    a = list(a)
    quick_sort_obj = wrapper(qsort, a, 0, len(a)-1)
    print(timeit.timeit(quick_sort_obj, number=10000))
