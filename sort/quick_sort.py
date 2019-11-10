def qsort(list_, i_l, i_u):
    if(i_l < i_u):
        pvt = partition(list_, i_l, i_u)
        qsort(list_, i_l, pvt - 1)
        qsort(list_, pvt + 1, i_u)

def partition(arr, first, last):
    pvtValue = arr[first]
    lower = first + 1
    upper = last
    done = False
    while not done:
         while lower <= upper and arr[lower] <= pvtValue:
           lower += 1
        
         while lower <= upper and arr[upper] >= pvtValue:
           upper -= 1

         if upper < lower:
            done = True
         else:
            arr[lower], arr[upper] = arr[upper], arr[lower]

    arr[first], arr[upper] = arr[upper], arr[first]
    return upper

if __name__ == "__main__":
   list_1 = [5, 4, 2, 1, 7, 8, 0]
   qsort(list_1, 0, len(list_1)-1)
   print(list_1)
