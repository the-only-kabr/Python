import random

n = list(map(int, input().split()))
for i in range(1, len(n)):
    if i % 2 != 0:
        t = n[i]
        n[i] = n[i - 1]
        n[i - 1] = t
    if i % 2 == 0 and i != len(n)-1:
        temp = n[i + 1]
        n[i + 1] = n[i]
        n[i] = temp

for z in range(len(n)):
    print(n[z], end=' ')
# Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# def fillDict(_m):
#     d = dict()
#     for i in range(1, n+1):
#         d[str(i)] = 3 * i + 1
#     return d


# def printDict(_d):
#     for z in range(len(_d)):
#         print(_d[z], end=' ')


# n = int(input("Введите число : "))
# nDict = fillDict(n)
# print(nDict)

# Задайте список из N элементов, заполненных числами из промежутка[-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# def fillList(_n):
#     _list = []
#     for i in range(n):
#         _list.append(random.randint(-n, n))
#     return _list


# n = int(input('Введите число : '))
# list = fillList(n)
# print(list)

# Реализуйте алгоритм перемешивания списка.


# def listShuffling(_list):
#     newList = []
#     listIndex = []
#     for i in range(len(_list)):
#         index = random.randint(0, len(_list)-1)
#         while index in listIndex:
#             index = random.randint(0, len(_list)-1)
#         newList.append(_list[index])
#         listIndex.append(index)
#     return newList


# n = int(input('Введите число : '))
# list = fillList(n)
# print(list)
# newList = listShuffling(list)
# print(newList)


# Submit a solution for 2-5-Перемешивание
# Перемешивание
# Считайте элементы и сформируйте из него список. Реализуйте следующий алгоритм перемешивания списка: Необходимо пройтись по всем элемента от 0 до последнего один раз и каждый
# четный элемент поменять местами с предыдущим, каждый нечетный со следующим, если такое возможно.
# Input format  Целые числе через пробел
# Output format  Целые числе через пробел
# Input   1 2 3
# Output  2 3 1
# Input   1 2 3 4
# Output  2 3 4 1
# n = [int(i) for i in input().split()]

# # for i in range(len(n)):
# n.append(n[0])
# n.remove(n[0])
# # print(i)
# # print(f" i % 2 == 0 : {i % 2 == 0}")
# # if i % 2 == 0:
# #     t = n[i]
# #     n[i] = n[i - 1]
# #     n[i - 1] = t
# # elif i % 2 != 0 and i != len(n)-1:
# #     print("Work")
# #     temp = n[i + 1]
# #     n[i + 1] = n[i]
# #     n[i] = temp

# for z in range(len(n)):
#     print(n[z], end=' ')


# n = [int(i) for i in input().split()]

# for i in range(len(n)):
#     if i % 2 == 0 and i != len(n)-1:
#         # if i % 2 != 0:
#         # print('Четное')
#         t = n[i - 1]
#         n[i - 1] = n[i]
#         n[i] = t
#     # if i % 2 == 0 and i != len(n)-1:
#     if i % 2 != 0 and i != len(n)-1:
#         print('НЕ четное')
#         print(i)
#         t = n[i + 1]
#         n[i + 1] = n[i]
#         n[i] = t
#     #     t = n[i + 1]
#     #     n[i + 1] = n[i]
#     #     n[i] = t
#     print(n)


# for z in range(len(n)):
#     print(n[z], end=' ')
