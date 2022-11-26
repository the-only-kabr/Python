import reader.user_interface as user_interface

def read():
    l = ['Введите Фамилию: ',  'Введите Имя: ', 'Введите номре телефона: ','Введите адрес проживания: ','Дата рождения: ']
    return user_interface.data_read(l)