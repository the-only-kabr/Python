n=input("-")
list=[int(i) for i in n.split()]
a=0
b=len(list)-1
i=0
while i<=(ceil(len(list)/2)):
    print(list[a]*list[b])
    i+=1
    a+=1
    b-=1
