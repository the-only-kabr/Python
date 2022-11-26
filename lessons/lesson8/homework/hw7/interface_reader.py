import reader.data_reader as data_reader
import writer.data_writer as data_writer

def init():
    flag, data = data_reader.read()
    data_writer.write(flag, data)
