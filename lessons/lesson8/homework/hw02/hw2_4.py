# Произведение элементов
# Считайте число N и сформируйте список из N элементов, заполнив его числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Input format
# В первой строке одно целое число N. Во второй строке целые числа через пробел, указанные позиции.
# Output format
# Одно число, произведение элементов на указанных позициях.
# 5   1 2 3 ->    -24
# 7   0 14   - > 49
# 5   0 1    -> 20

n = int(input())
data = list(map(int, input().split()))
list = []
for i in range(-n, n+1):
    list.append(i)
res = 1
# print(list)
for line in data:
    pos = int(line)
    res *= list[pos]
print(res)

# import random


# def fillList(_n):
#     _list = []
#     for i in range(n):
#         _list.append(random.randint(-n, n))
#     return _list


# def sum(_l, _list):
#     sum = 1
#     # print(f" numbers {_l}")
#     for i in range(len(_list)):
#         if i in _l:
#             sum *= _list[i]
#     return sum


# n = int(input())
# # n = int(input('Введите число : '))
# list = fillList(n)
# # print(list)
# numbers = [int(i) for i in input().split()]
# # sum = sum(numbers, list)
# print(sum(numbers, list))
