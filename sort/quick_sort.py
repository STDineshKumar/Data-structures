def qsort(list_, i_l=1, i_u=None):
    i_p = i_l - 1
    i_l = i_l
    i_u = i_u if i_u else len(list_) - 1

    if i_u <= i_l:
        return

    while (i_l <= i_u):
        if list_[i_p] >= list_[i_l]:
            i_l += 1
        elif list_[i_p] <= list_[i_u]:
            i_u -= 1
        else:
            list_[i_l], list_[i_u] = list_[i_u], list_[i_l]

    list_[i_p], list_[i_u] = list_[i_u], list_[i_p]
    print(list_)
    qsort(list_, 1, i_u)
    qsort(list_, i_u + 1, len(list_) - 1)


list_1 = [5, 4, 2, 1, 7, 8, 0]
qsort(list_1)
print(list_1)
