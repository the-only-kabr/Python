import interface_reader
import file_reader

n = int(input('введите 1 если хотите записать данные 2 если прочитать : '))
if n == 1:
    interface_reader.init()
elif n == 2:
    file_reader.init()
# Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.fdsfaa
