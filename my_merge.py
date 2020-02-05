import random
from timeit import Timer

def merge(lst):
    if len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        lst_l = merge(lst[:mid])
        lst_r = merge(lst[mid:])
        return sort(lst_l, lst_r)


def sort(l_lst, r_lst):
    srt_lst = []
    l_index = 0
    r_index = 0
    while l_index < len(l_lst) and r_index < len(r_lst):
        if l_lst[l_index] < r_lst[r_index]:
            srt_lst.append(l_lst[l_index])
            l_index += 1
        else:
            srt_lst.append(r_lst[r_index])
            r_index += 1
    while l_index < len(l_lst):
        srt_lst.append(l_lst[l_index])
        l_index += 1
    while r_index < len(r_lst):
        srt_lst.append(r_lst[r_index])
        r_index += 1


    return srt_lst


if __name__ == "__main__":
    lst = [random.randint(13, 25) for i in range(10**6)]
    #print(lst)
    print(merge(lst))
    #t = Timer(lambda: (merge(lst)))
    #print(t.timeit(number=10))