xyz=[int(xyz) for xyz in input("Введите координаты через пробел: ").split()]
for i in xyz i!=0:
    for x in [True,False]:
        for y in [True,False]:
            for z in [True,False]:
                print(x,'AND',y,'OR',z,'=',x and y or z)
else:
    print(False)
