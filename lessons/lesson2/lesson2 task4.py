n=int(input('Введите число'))
dict={x+1:3*(x+1)+1 for x in list(range(n))}
print(dict)
