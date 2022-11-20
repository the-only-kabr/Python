n=int(input('n'))
i=input('indeces').split()
prod=1
s=[int(s) for s in range(-n, n+1)]
index=[int(index) for index in i]
if index==s.index:
  prod=prod*s[index]
print(prod)
print(s)
print(s.index)
