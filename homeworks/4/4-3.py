#Задайте последовательность чисел. Напишите программу, которая выведет\
# список неповторяющихся элементов исходной последовательности.

s=input()
num=[i for i in s.split(' ')]
print(num)
#num.sort()
#print(num)
unique=[]
for i in num:
    if num.count(i)<2:
      unique.append(i)
print(unique)



#s=input()
#num=[i for i in s.split(' ')]
#print(num)
#num.sort()
#print(num)
#i=0
#while i <= len(num)-2:
#    if num[i]==num[i+1]:
 #       num.remove(num[i])
#    else:
 #       i+=1
#print(num)