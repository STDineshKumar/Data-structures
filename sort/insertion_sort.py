def insertion_sort(a):
    """ Iterative apporach for insertion sort.
    """
    n = len(a)
    for i in range(n):
        for j in range(i, 0, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
            else:
                break
    return a

if __name__ == "__main__":
    a = [9, 3, -4, 0, 10, 20, -15, 1, 4]
    print(a)
    print(insertion_sort(a))