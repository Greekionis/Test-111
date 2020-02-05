import random
from timeit import Timer

def q_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = random.choice(lst)
        l_lst = [n for n in lst if n < pivot]
        e_lst = [pivot] * lst.count(pivot)
        r_lst = [n for n in lst if n > pivot]
        return q_sort(l_lst) + e_lst + q_sort(r_lst)


if __name__ == "__main__":
    lst = [random.randint(13, 25) for i in range(10**6)]
    #print(q_sort(lst))
    t = Timer(lambda: (q_sort(lst)))
    print(t.timeit(number=10))