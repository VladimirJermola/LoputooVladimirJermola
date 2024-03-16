import csv
import os
from tkinter.filedialog import askopenfilename

class Model:
    def __init__(self):
        self.selected_file = None
        self.search_string = None
        self.file_name = None
        #self.search_result = None

    def open_file(self):
        filename = askopenfilename()
        #print(filename)
        self.file_name = os.path.basename(filename)
        #print(self.file_name)
        self.selected_file = filename


    def search_file(self, search_str):
        try:
            matching_rows = []
            # Open the Excel file for reading
            with open(self.selected_file, 'r', encoding='utf-8') as file:
                # Iterate through each line in the file
                for line in file:
                    # Split the line into columns (assuming CSV format)
                    columns = line.strip().split(',')
                    # Check if any column contains the searched value
                    if any(search_str.lower() in column.lower() for column in columns):
                        matching_rows.append(columns)
            #print(matching_rows)
            #self.view.lbl_result = matching_rows
            return matching_rows
        except Exception as e:
            print("CSV faili otsingu viga: ", e)
            return None



