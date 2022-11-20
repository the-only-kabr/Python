x=input()
x=x.replace("-", "0")
xr=x.replace(".", "0")
a=[int(a) for a in str(xr)]
print(sum(a))
