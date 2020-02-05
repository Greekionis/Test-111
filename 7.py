"""
Поскольку цифры лежат на близком интервале (от 13 до 25), предпочтение у "пузырька", по сравнению со "слиянием"
"""
import random, timeit


def my_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = random.choice(arr)
    l_nums = [n for n in arr if n < pivot]
    e_nums = [pivot] * arr.count(pivot)
    b_nums = [n for n in arr if n > pivot]
    return my_sort(l_nums) + e_nums + my_sort(b_nums)



if __name__ == "__main__":
    arr = [random.randint(13, 25) for i in range(10**6)]
    print(my_sort(arr))







