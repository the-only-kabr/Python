n=input("-")
list=[int(i) for i in n.split()]
res=0
for i in range(1,len(list),2):
    res=res+list[i]
print(res)
