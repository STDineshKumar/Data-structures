def bbsort(a, j=0):
    """ Recursive bubble sort.
        Logic :
        -------
            Compare adjacent items in a list and swap items if lower index item is greater than the higher index item.
            Note*** Highest value item is moved to higest index.
            Sub-array n-1 elemens and repeate the compare process until sub-array lenght becomes zero.
        NOTE :
        ------
            This function uses in-place swap logic.
        Space Complexity:
        -----------------
            O(N)

        Time Complexity:
        ----------------
            O(N^2) = N*(N+1)/2
    """
    l = len(a)
    for i in range(l-j-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    if l-j == 0:
        return
    bbsort(a, j=j+1)
    

def bbsort2(a):
    """ Iterative bubble sort.
    """
    l = len(a)
    j =  0
    while ( l-j > 0):
        for i in range(l-j-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
        j += 1

if __name__ == '__main__':
    a = [4,5,3,2,1]
    bbsort(a)
    bbsort2(a)
    print(a)