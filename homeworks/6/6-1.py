#Задайте последовательность чисел. Напишите программу, которая выведет\
# список неповторяющихся элементов исходной последовательности.

s=input()
num=[i for i in s.split(' ')]
nums=list(set(num))
print(nums)
