from Model import Model
from View import View
import csv
import os
from tkinter.filedialog import askopenfilename

class Controller:
    def __init__(self):
        self.__model = Model()
        self.__view = View(self, self.__model)
        self.search_result = []

    def main(self):
        self.__view.main()

    def open_file_click(self):
        self.__model.open_file()
        self.__view.char_input.focus_set()
        self.__view.btn_send['state'] = 'normal'
        self.__view.lb_file_info['text'] ='Avatud fail: ' + self.__model.file_name


    def search_file_click(self, info):
        #search_str = info
        #print(info)
        self.__model.search_result = self.__model.search_file(info)
        if self.__model.file_name == 'Persons.csv':
            self.__view.generate_table(self.__model.search_result)
        else:
            self.__view.generate_table_big(self.__model.search_result)
        #self.__view.generate_table(self.__model.search_result)




