a=int(input("Введите число: "))
if (a%5==0 and a%10==0) or (a%15==0) and a%30!=0:
    print("Кратно")
else:
    print("Не кратно")
