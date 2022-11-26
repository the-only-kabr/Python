# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда[1, 2, 6, 24](1, 1*2, 1*2*3, 1*2*3*4)

def numbers(_n):
    sum = 1
    for i in range(1, _n+1):
        sum *= i
    return sum


def fillList(_m):
    l = []
    for i in range(1, _m+1):
        l.append(numbers(i))
    return l


def printList(_list):
    for z in range(len(_list)):
        print(_list[z], end=' ')


n = int(input())
listNumbers = fillList(n)
print(listNumbers)
