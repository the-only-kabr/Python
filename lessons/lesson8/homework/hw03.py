import math
# //Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# //стоящих на нечётной позиции.
# //Пример:  [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


# def sumi(_list):
#     sum = 0
#     for i in range(len(_list)):
#         if i % 2 != 0:
#             sum += _list[i]
#     return sum


# n = [int(i) for i in input().split()]
# print(sumi(n))


# //Напишите программу, которая найдёт произведение пар чисел списка.
# //Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# //Пример:
# //[2, 3, 4, 5, 6] => [12, 15, 16];
# //[2, 3, 5, 6] => [12, 15]

# def sumOfNumber(_list):
#     newList = []
#     for i in range(int(math.ceil(len(_list) / 2))):
#         newList.append(list[i] * list[len(_list)-i-1])
#     return newList


# list = [int(i) for i in input('Введите список цифр : ').split()]
# newList = sumOfNumber(list)
# print(newList)


# //Задайте список из вещественных чисел. Напишите программу,
# //которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# //Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# def findDifferent(_list):
#     max = 0
#     min = 10
#     for i in range(len(_list)):
#         s = str(list[i])
#         newString = s[s.find(".") + 1:]
#         newString = findLength(newString)
#         if newString > max:
#             max = newString
#         if newString < min and newString != 0:
#             min = newString
#     return max - min


# def findLength(_n):
#     if len(_n) < 2:
#         _n += '0'
#     return int(_n)


# list = [float(f) for f in input(" Введите числа : ").split()]
# print(findDifferent(list))

# //Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# //Пример:
# //- 45 -> 101101
# //- 3 -> 11
# //- 2 -> 10

# print(bin(int(input("Введите число : "))))  # ::))))))))


def findBinary(_n):
    b = ''
    while _n > 0:
        b = str(_n % 2) + b
        _n = _n // 2
    return b


n = int(input('Введите число: '))
print(findBinary(n))

# //Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# //Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]


Nb решение подонгоно под  k = 8


def fibanaci(_n):
    _list = []
    for i in range(_n):
        if i == 0 or i == 1:
            _list.append(1)
        else:
            _list.append(_list[i-2] + _list[i-1])
    return _list


def negaFibanaci(_n):
    _list = [0]
    for i in range(_n-1, 0, -1):
        if i == _n - 1:
            _list.insert(0, 1)
        else:
            _list.insert(0, _list[1] - _list[0])
    return _list


# n = int(input("Введите число : "))
# list = fibanaci(n)
# negaList = negaFibanaci(n+1)
# print(*negaList, *list)
