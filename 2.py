def sos(hum, step):
    lst = [i + 1 for i in range(hum)]         # Массив "людей"
    pos = step - 1                          # Позиция начал, с учетом индексации в массивах

    while len(lst) > 1:
        print(lst)
        lst.pop(pos)
        pos = pos + step-1
        while pos >= len(lst):              # Уменьшаю Pos до тех пор, пока не станет меньше длины массива
            pos = pos - len(lst)
    return lst


if __name__ == "__main__":
    hum = 7
    step = 5
    print(sos(hum, step))