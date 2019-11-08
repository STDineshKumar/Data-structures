"""
Logic:
------
NOTE
-----
Space Complexity:
-----------------
Time Complexity:
-----------------
"""

def min_index(a):
    min_idx = 0
    for i in range(len(a)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx

def selection_sort(a):
    """ Iterative approach.
    """
    n = len(a)
    for i in range(n):
        min_offset = min_index(a[i:])
        if a[i] > a[i + min_offset]:
            a[i], a[i + min_offset] = a[i + min_offset], a[i]
    return a

def selection_sort2(a, i=0):
    """ Recursive approach.
    """
    n = len(a)
    if n > i:
        min_offset = min_index(a[i:])
        if a[i] > a[i + min_offset]:
            a[i], a[i + min_offset] = a[i + min_offset], a[i]
        selection_sort2(a, i+1)


if __name__ == "__main__":
    a = [9, 8, 3, 4, 2, 7, 0, 1]
    print(a)
    print(selection_sort(a))
    a = [9, 8, 3, 4, 2, 7, 0, 1]
    print(a)
    selection_sort2(a)
    print(a)