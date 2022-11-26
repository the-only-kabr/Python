def data_read(_list):
    flag = input('Введите формат файла записи : ')
    new_data = []
    for i in range(len(_list)):
        new_data.append(input(f'{_list[i]}'))
    return flag,new_data