n=int(input())
i=1
while i<=n:
    a=[(1+(1/i))**i]
    print(f'{i}: {a}', end=" ")
    i=i+1
#print(a)
