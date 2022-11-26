def write(data):
    loc = open('data.csv','a')
    s = ",".join(data)
    loc.write('\n' + s)