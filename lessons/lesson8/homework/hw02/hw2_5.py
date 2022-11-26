# Submit a solution for 2-5-Перемешивание
# Перемешивание
# Считайте элементы и сформируйте из него список. Реализуйте следующий алгоритм перемешивания списка: Необходимо пройтись по всем элемента от 0 до последнего один
# раз и каждый
# четный элемент поменять местами с предыдущим, каждый нечетный со следующим, если такое возможно.
# Input format  Целые числе через пробел
# Output format  Целые числе через пробел
# Input   1 2 3
# Output  2 3 1
# Input   1 2 3 4
# Output  2 3 4 1

# n = list(map(int, input().split()))
#

i = [int(x) for x in input().split()]
for j, item in enumerate(i):
    if item % 2 == 0 and j > 0:
        i[j], i[j-1] = i[j-1], i[j]
    elif item % 2 != 0 and j < len(i)-1:
        i[j], i[j+1] = i[j+1], i[j]

print(*i, sep=" ", end="")

# print(*n)
# for z in range(len(n)):
#     print(n[z], end=' ')

# temp = n[i]
# if n[i] % 2 == 0:
#     temp = n[i]
#     n[i] = n[i-1]
#     n[i-1] = temp
# if n[i] % 2 != 0 and i != len(n) - 1:
#     temp = n[i]
#     n[i] = n[i + 1]
#     n[i+1] = temp
# n[i] = temp
