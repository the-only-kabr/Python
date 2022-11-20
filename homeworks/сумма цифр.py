#Напишите программу, которая принимает
#на вход вещественное число и показывает сумму его цифр.
#x=int(input('Введите число: '))
#print(type(x))

#x=x.replace("-", "0")
#xr=x.replace(".", "0")
#a=[int(i) for i in str(x)]
  #  a=a.replace("-", "0")
 #   a=a.replace(".", "0") 
##print(a)
#    print(sum(a))
#print(type(sum(a)))

x=int(input())

def sum(x):
    if float(x)<0:
        x=float(x)*(-1)
    number=0
    for i in str(x):
        if i !=".":
            number+=int(i)
        return number
print(int(summa(x)))
