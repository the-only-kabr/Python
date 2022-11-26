# a – открытие для добавления данных
# r – открытие для чтения данных
# w – открытие для записи данных

# with open('data.txt', 'w') as data:
#     data.write('line 1 \n')
#     data.write('line 2 \n')

# colors = ['red', 'green', 'blue']
# data = open('data.txt', 'a')
# data.writelines(colors)
# data.write('\n1234')
# data.write('\n Goll \n')
# data.close()

# path = 'neData.txt'
# data = open(path, 'a')
# data.write('Shtm new')

# path = 'newData.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# from function import *

# a = int(input())
# b = int(input())
# s = [str(s) for s in input().split()]

# print(multi(a,b))
# print(new_string(s,b))
# print(concatenation('q', 's', 'd', 'w'))
# print(printFib(a))

# Кортежи
# a = (1,2,3,4)
# print(a[-1])
# t = (1,)
# print(type(t))
# print(t[0])
# for i in range(len(a)):
#     print(a[i])

# 
# dictionary = {}
# dictionary = \
#     {
#         'up' : '↑',
#         'down' : '↓',
#         'left' : '←',
#         'right' : '→'
#     }
# print(dictionary['left'])
# print(dictionary['right'])
# print(dictionary['up'])
# print(dictionary['down'])

# for key  in dictionary.keys():
#     print(key)
# for values in dictionary.values():
#     print(values)
# for item in dictionary:
#     print(dictionary[item])
# Вниз (↓) — Alt и 2 5.
# Вверх (↑) — Alt и 2 4.
# Вверх-вниз (↕) — Alt и 1 8.
# Влево-вправо (↔) — Alt и 2 9.  

#Множество 
# colors = {'red','green','blue'}
# print(type(colors))
# print(colors)
# colors.add('yellow')
# print(colors)
# colors.add('red')
# print(colors)
# b = set([2, 5, 8, 13, 21])

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()
# print(c)
# u = a.union(b)
# print(u)
# i =  a.intersection(b)
# print(i)
def printList(_list):
    for i in range(len(_list)):
        print(_list[i], end = '')
    print()

list1 = [1, 2, 3, 4, 5]
list2 = list1
printList(list1)
printList(list2)
list1[0] = 321
printList(list1)
printList(list2)

print(list1.pop())
printList(list1)
print(list1.pop())
printList(list1)
print(list1.pop())
printList(list1)