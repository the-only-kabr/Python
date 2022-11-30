#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("n="))
simple=[]
k=2
while k*k <=n:
    if n%k == 0:
        simple.append(k)
        n //=k
    else:
        k+=1
if n>1:
    simple.append(n)
print(simple)
print(k)
