with open('data.txt', 'w') as data:
    data.write('line 1 \n')
    data.write('line 2 \n')

colors = ['red', 'green', 'blue']
data = open('data.txt', 'a')
data.writelines(colors)
data.close()

path = 'data.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

