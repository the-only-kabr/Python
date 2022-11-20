import math

aa=int(input("Введите число aa "))
bb=int(input("Введите число bb "))
print(f'aa+bb = {aa+bb}, aa-bb = {aa-bb}, aa*bb = {aa*bb}, aa/bb = {round(aa/bb, 2)},\
    aa//bb = {aa//bb}, aa%bb = {aa%bb}, sqrt(a^(10) + b^(10)) = {round(math.sqrt(pow(aa, 10)+ pow(bb, 10)),2)}')
