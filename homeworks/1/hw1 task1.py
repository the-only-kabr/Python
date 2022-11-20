x=int(input('Введите координату X = '))
y=int(input('Введите координату Y = '))
if x==0 and y == 0:
        print('Функция не существует')
elif x!=0 and y==0:
        print('Точка на оси Х')
elif x==0 and y!=0:
        print('Точка на оси Y')
elif x>0 and y>0:
        print('Точка в первой четверти')
elif x>0 and y<0:
        print('Точка во второй четверти')
elif x<0 and y<0:
        print('Точка в третьей четверти')
elif x<0 and y>0:
        print('Точка в четвертой четверти')
