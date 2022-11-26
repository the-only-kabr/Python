def multi(_a,_b):
    return _a * _b

def new_string(_symbol, _count = 3):
    return _symbol *  _count

def concatenation(*params):
    res: str = ""
    for item in params:
        res += item
    return res

def fib(_n):
    if _n in [1,2]:
        return 1
    else:
        return fib(_n-1) + fib(_n-2)

def printFib(_n):
    list = []
    for i in range(1,_n+1):
        list.append(fib(i))
    return list