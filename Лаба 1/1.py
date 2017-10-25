mass = [2, 5, 9, 8]


def minimum(x):
    i = x[0]
    for n in x:
        if n < i:
            i = n
    return i


def average(array):
    if len(array) == 0:
        return (-1)
    summa = 0
    for num in array:
        summa += num
    return summa / len(array)


print("Минимальное число в массиве: ", minimum(mass))
# mass = []
print("Среднее арифметическое: ", average(mass))