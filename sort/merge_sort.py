def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2
        left_list = list_[:mid]
        right_list = list_[mid+1:]
        l = merge_sort(left_list)
        r = merge_sort(right_list)
    

def merge(list1, list2):
    merge_list = []
    for i in range(len(list1)):
