from random import randint

def get_temperature(senser):
    return randint(-25,0) if senser else(0,20)

def get_preassure(senser):
    if senser:
        return randint(720,750)
    else:
        return randint(750,770)

def get_wind_seed(senser):
    if senser:
        return randint(0,5)
    else:
        return randint(6,10)

def data_collectiono(sensor = 1):
    return (get_temperature(sensor),
            get_preassure(sensor),
            get_wind_seed(sensor))