from pythonProject.Repository_7.proxy_pattern.abstract_reader import Reader
from pythonProject.Repository_7.proxy_pattern.txt_reader import TxtReader
from pythonProject.Repository_7.proxy_pattern.txt_writer import TxtWriter

class TxtProxyReader(Reader):
    def __init__(self, txt_reader: TxtReader):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self.__is_actual = True
            return self.__result

class TxtWriter():
    def __init__(self, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__writer = txt_writer

    def write_file(self):
        self.__result = self.__writer.write_file()
        self.__is_actual = False
        return self.__result

    def update_actual_status(self, status):
        self.__is_actual = status
