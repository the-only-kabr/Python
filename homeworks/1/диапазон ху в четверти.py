quarter=int(input('Введите номер четверти - '))
if quarter<1 or quarter>4:
        print('Превышена область значений')
elif quarter==1:
    for x in range(3):
        for y in range(3):
            print(f'Диапазон значений x = {x}, y = {y}')
elif quarter==2:
    for x in range(3):
        for y in range(3):
            print(f'Диапазон значений x = {x}, y = {-y}')
elif quarter==3:
    for x in range(3):
        for y in range(3):
            print(f'Диапазон значений x = {-x}, y = {-y}')
elif quarter==4:
    for x in range(3):
        for y in range(3):
            print(f'Диапазон значений x = {-x}, y = {y}')
