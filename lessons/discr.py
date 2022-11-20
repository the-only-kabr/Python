#Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:

#  1) с помощью математических формул нахождения корней квадратного уравнения

#
    #2) с помощью дополнительных библиотек Python
a = int(input('a'))
b = int(input('b'))
c = int(input('c'))
discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))
