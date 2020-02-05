from collections import Counter
"""
Пройтись по всем элментам в списке, посчитать количество каждой буквы в каждом элементе,
поместить это в словарь, отсортировать по значению, развернуть так, чтобы по убыванию значения, взять первый элемент
и приклеить к выходной строке.
"""

def dna(my_lst):
    dict_temp = []
    exit_str = ""
    for i in range(len(my_lst)):
        for j in range(len(my_lst[i])):
            dict_temp.append(my_lst[j][i])
        sorted_x = sorted(Counter(dict_temp).items(), key=lambda kv: kv[1], reverse=True)
        exit_str = exit_str + str(sorted_x[0][0])
        dict_temp = []
    return exit_str


if __name__ == "__main__":
    lst = ["ATTA", "ACTA", "AGCA", "ACAA"]
    print(dna(lst))
