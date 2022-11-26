import userI
import sum
import min
import div


def initial():
    l = userI.value()
    if l[1] == '+':
        sum.sum(l)
    if l[1] == '-':
        min.min(l)
    # if l[1] == '/':
    #     calc.calc(l[0]  l[2])
