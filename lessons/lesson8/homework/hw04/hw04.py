# Вычислить число c заданной точностью d
#  Пример:
# при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import re
from random import randint


def rounds(num, max_=2):
    '''с точностью не более n "значащих цифр", после запятой. '''
    left, right = str(num).split('.')
    zero, nums = zero_nums = [], []
    for n in right:
        zero_nums[0 if not nums and n == '0' else 1].append(n)
        if len(nums) == max_:
            break
    return '.'.join([left, ''.join(zero) + ''.join(nums)])


length = float(input('Введите длина числo : '))
num = float(input('Введите число : '))
print(rounds(num, length))

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def Factor(_n):
    _list = []
    d = 2
    while d * d <= _n:
        if _n % d == 0:
            _list.append(d)
            _n //= d
        else:
            d += 1
    if _n > 1:
        _list.append(_n)
    return _list


n = int(input())
print(Factor(n))

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


def pureList(_list):
    newList = []
    for i in range(len(_list)):
        if _list.count(_list[i]) < 2:
            newList.append(_list[i])
    return newList


n = [int(i) for i in input('Введите список значений : ').split()]
newList = pureList(n)
print(* newList)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: - k = 2 = > 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

max_val = 100
k = int(input('Введите натуральную степень k:'))
# коэфф. при старшей степени не должен быть равен 0
koeff = [randint(0, max_val) for i in range(k)]+[randint(1, max_val)]
poly = '+'.join([f'{(j,"")[j==1]}x^{i}' for i,
                j in enumerate(koeff) if j][::-1])
# Поиск и замены:
poly = poly.replace('x^1+', 'x+')
poly = poly.replace('x^0', '')
poly += ('', '1')[poly[-1] == '+']
poly = (poly, poly[:-2])[poly[-2:] == '^1']
print(poly)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
data1 = open('data1.txt', 'r')
data2 = open('data2.txt', 'r')
allData = open('allData.txt', 'w')


# # str1 = "1a^2b+1b^2a-1c^1+5"
# # str2 = "2a^2b+1c^1-4"

firstNumber = data1.read()
secondNumber = data2.read()


def polynomialSum(_list):
    soluthion = ""
    for i in range(len(_list)):
        n = _list[i]
        for z in range(i+1, len(_list)):
            item = _list[z]
            if n[1:].isdigit() and item[1:].isdigit():
                soluthion += str(int(n) + int(_list[z]))
                continue
            if n[2:] == item[2:]:
                s = int(n[:2]) + int(item[:2]), item[2:]
                if s[0] != 0:
                    soluthion += str(s)
                continue

    return soluthion


def allNumbers(_firstNumber, _secondNumber):
    numbers = _firstNumber+'+'+_secondNumber
    plusNumbers = numbers.split('+')
    plusNum = []
    for str in plusNumbers:
        plusNum.append(('+' + str).split('-'))
    endNum = []
    for n in range(len(plusNum)):
        num = plusNum[n]
        if len(num) > 1:
            endNum.append(num[0])
            endNum.append('-' + num[1])
        else:
            endNum.append(num[0])
    return endNum


num = allNumbers(firstNumber, secondNumber)
allNumber = polynomialSum(num)
allData.writelines(allNumber)
