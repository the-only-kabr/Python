# 4. Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def get_random_list(_list):
    return [round(random.randint(0, 5), 2) for x in range(_list+1)]


def file_writer(file_name, data):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(str(data))


def mnogochlen_str(kofs):
    indexes = {
          "0": "",
          "1": "",
          "2": "\u00B2",
          "3": "\u00B3",
          "4": "\u2074",
          "5": "\u2075",
          "6": "\u2076",
          "7": "\u2077",
          "8": "\u2078",
          "9": "\u2079",
          "-": "\u207B"
          }

    resalt = []
    for i, item in enumerate(kofs):
        if item > 1 and i < len(kofs)-1:
            resalt.append(f'{item}x{indexes[str(len(kofs)-1-i)]}')
        elif item == 1 and i < len(kofs)-1:
            resalt.append(f'x{indexes[str(len(kofs)-1-i)]}')
        elif i == len(kofs)-1 and item != 0:
            resalt.append(f'{item}')
        elif item == 0:
            continue

    return '+'.join(resalt) + ' = 0'


_list = int(input('Введите степень многочлена - '))
kofs = get_random_list(_list)
name_file = input('Введите имя файла для записи коэффициентов - ')
file_writer(name_file, kofs)
print(f'Коэффициенты - {kofs} были записаны в файл {name_file}')
strng = mnogochlen_str(kofs)
print(f'Ваш многочлен степени {_list} со случайными коэффициентами {strng}')
