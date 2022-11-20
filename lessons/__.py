#1. Задайте строку из набора чисел. \
#Напишите программу, которая покажет большее и меньшее число.
#В качестве символа-разделителя используйте пробел.

str=input()
a=[int(x) for x in str.split()]
mina=a[0]
maxa=a[0]
for item in a:
    if item>maxa:
        maxa=item
    elif item<mina:
        mina=item
        
print(maxa, mina)
