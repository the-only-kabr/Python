# def f(x):
#     return x ** 2
# g = f
# print(f(2))
# print(g(2))

# print(type(f))

# def calc(x):
#     return x +10

# def calc2(x):
#     return x *10

# def math(operacion, x):
#     print(operacion(x))
# print(calc(10))
# print(calc2(10))
# math(calc2,10)
# math(calc, 5 )
# def sum(x, y):
#     return x + y
# s = lambda w, y : w + y
# def mult(x, y):
#     return x * y
# m = lambda z, s: z * s
# def calc(func, a , b):
#     print(func(a,b))

# calc(lambda x , y : x + y , 3, 4)
# calc(m, 3, 4)

# list = []
# for i in range(1,21):
#     if i % 2 == 0:
#         list.append(i)

# def f(x):
#     return x ** 3

# list = [(i, f(i)) for i in range(1,20) if i % 2 == 0]
# print(list)

# path = 'data.txt'
# data = open(path,'r')
# list =  data.read()
# print(list)
# data.close()

# def f(i):
#     return i ** i

# newData = []
# for e in list:
#     e = int(e)
#     if int(e) % 2 == 0:
#         newData.append((e , f(e)))
# # newData = [int(i , lambda i : i ** i) for i in list if int(i) % 2 == 0 ]
# print(*newData)
exit()


def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


path = 'data.txt'
first_data = open(path, 'r')
data = first_data.read().split()
print(data)
first_data.close()

res = select(int, data)
res = where(lambda x: not x % 2, res)
res = select(lambda x: (x, x ** 2), res)
print(res)

li = [x for x in range(1, 11)]
print(li)
li = list(map(lambda x: x+10, li))
print(li)

n = list(map(int, input().split()))
print(type(n))
res = list(filter(lambda x: not x % 2, n))
print(res)

a = list(map(str, input().split()))
b = list(map(int, input().split()))
c = list(map(str, input().split()))

data = list(zip(a, b, c))
print(data)

li = ['Vasia', 'Slava', "Kolia"]
data = list(enumerate(li))
print(data)
