#Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.

#Пример:

#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def grades(x, n):
    if n==0:
        return str(x)
    if n==1:
        return str(x)+"x"
    grades = ["⁰", "¹", "²", "³", "⁴", "⁵", "⁶", "⁷", "⁸", "⁹"]
    result = str(x)
    if x != 0:
        result += "x"
    for i in str(n):
        result += grades[int(i)]
    return result

def quadratic_equation(m):
    result=[]
    for i in range(m, -1, -1):
        koeff = random.randint(0, 100)
        if koeff != 0:
            result.append(grades(koeff, i))
    return "+".join(result)

print(quadratic_equation(int(input())))