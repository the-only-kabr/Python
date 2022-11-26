import txt_reader
import csv_reader

def reader(flag):
    if flag == '1':
        txt_reader.read()
    elif flag == '2':
        csv_reader.read()
