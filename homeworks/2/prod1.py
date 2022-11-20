from math import prod
 
#arr = [int(input('Введите элемент списка: ')) for i in range(int(input('Введите длину списка: ')))]
#print(f'Весь список: {arr}')
#print(f'Сумма элементов списка равна: {sum(arr)}')
#print(f'Произведение элементов списка: {prod(arr)}')

N=int(input('n'))
index=input('index')
prod=1
rangen=[a for a in range(-N, N+1)]
indece=[int(indece) for indece in str(index).split()]
for i in indece:
    if indece[i]==rangen.index(indece[i][0, N+1]):
        prod=prod*rangen[i]
    print(prod)
