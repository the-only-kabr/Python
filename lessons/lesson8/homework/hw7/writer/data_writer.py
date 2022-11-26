import writer.csv_writer as csv_writer
import writer.txt_writer as txt_writer

def write(flag, data):
    print(data)
    if flag == 'csv':
        csv_writer.write(data)
    if flag == 'txt':
        txt_writer.write(data)
