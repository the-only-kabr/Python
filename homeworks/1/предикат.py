for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:
            if (not (x or y or z)) == (not x and not y and not z):
                print('yeah')
            else:
                print('not')
