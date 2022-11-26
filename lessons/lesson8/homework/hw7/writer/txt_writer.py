def write(data):
    s = " ".join(data)
    loc = open('data.txt','a')
    loc.write('\n' + s)