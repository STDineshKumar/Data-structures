def bbsort(a, j=0):
    l = len(a)
    for i in range(l-j-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
    if l-j == 0:
        return
    bbsort(a, j=j+1)
    

def bbsort2(a):
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
    print(a)