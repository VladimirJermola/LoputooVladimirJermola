
from tkinter import *
from tkinter import ttk
import tkinter.font as font


class View(Tk):
    def __init__(self, controller, model):
        super().__init__()
        self.__controller = controller
        self.__width = 800
        self.__height = 650
        self.__regular_font = font.Font(family="Courier", size=14)
        self.__Treeview_font = font.Font(family="Verdana", size=14)
        self.file_name = None

        self.title("Inimese Otsimine")
        self.center_window(self.__width, self.__height)

        self.__top_frame = self.create_top_frame()
        self.__bottom_frame = self.create_bottom_frame()
        self.__bottom2_frame = self.create_bottom2_frame()

        self.__lb_info, self.__lb_file_info = self.create_lables()


        self.__text_box = self.create_text_box()

        self.__btn_send, self.__btn_file_selection = self.create_buttons()
        self.__char_input = Entry(self.__top_frame, width=25, justify="center", font=self.__regular_font)
        self.__char_input.grid(row=1, column=0, padx=5, pady=2, sticky=EW)
        self.bind('<Return>', lambda event: self.__controller.search_file_click(self.__char_input.get()))

    @property
    def char_input(self):
        return self.__char_input
    @property
    def text_box(self):
        return self.__text_box

    @property
    def btn_send(self):
        return self.__btn_send

    @btn_send.setter
    def text_box(self, value):
        self.__btn_send = value

    @property
    def lb_file_info(self):
        return self.__lb_file_info

    @lb_file_info.setter
    def lb_file_info(self, value):
        self.__lb_file_info = value


    @text_box.setter
    def text_box(self, info):
        self.__text_box.config(state=NORMAL)
        self.__text_box.delete('1.0', END)  # Clear previous content
        self.__text_box.insert(END, info)  # Insert new content
        self.__text_box.config(state=DISABLED)

    def change_send_btn(self, change):
        if change:
            self.__btn_send.config(state=NORMAL)
        else:
            self.__btn_send.config(state=DISABLED)

    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

    def create_top_frame(self):
        frame = Frame(self, bg="#ffe5c5", height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom2_frame(self):
        frame = Frame(self, height=50)
        frame.pack(expand=NO, fill=BOTH)
        return frame


    def create_text_box(self):
        # Tekitab info kasti kuhu tuleb tulemused ja lisab sellele scrollbari
        txt_box = Text(self.__bottom_frame, font=self.__regular_font, state=DISABLED)
        scrollbar = Scrollbar(self.__bottom_frame, orient="vertical")
        scrollbar.config(command=txt_box.yview)
        txt_box.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=RIGHT, fill=Y)
        txt_box.pack(padx=5, pady=2)

        return txt_box

    def create_buttons(self):
        send = Button(self.__top_frame, text="Otsi", font=self.__regular_font,state=DISABLED, command=lambda:self.__controller.search_file_click(self.__char_input.get()))
        file_selection = Button(self.__top_frame, text="Fail", font=self.__regular_font, command=self.__controller.open_file_click)

        send.grid(row=1, column=1, padx=5, pady=2, sticky=EW)
        file_selection.grid(row=1, column=2, padx=5, pady=2, sticky=EW)

        return send, file_selection

    def create_lables(self):
        info = Label(self.__top_frame, text="Sisesta Info Otsimiseks", font=self.__regular_font, bg="#ffe5c5")
        info.grid(row=0, column=0, padx=5, pady=2, sticky=EW)
        file_info = Label(self.__bottom2_frame, text="Avatud fail: ", font=self.__regular_font)
        file_info.grid(row=0, column=0, padx=5, pady=2, sticky=EW)

        return info, file_info

    def generate_table(self, data):
        for child in self.__bottom_frame.winfo_children():
            child.destroy()

        my_table = ttk.Treeview(self.__bottom_frame)
        vsb = Scrollbar(self.__bottom_frame, orient=VERTICAL, command=my_table.yview)
        vsb.pack(side=RIGHT, fill=Y)
        my_table.configure(yscrollcommand=vsb.set)

        my_table["columns"] = ("Eesnimi", "Perenimi", "Sünniaeg", "Sugu", "Isikukood")

        my_table.column("#0", width=0, stretch=NO)
        my_table.column("Eesnimi", width=100, anchor="center")
        my_table.column("Perenimi", width=100, anchor="center")
        my_table.column("Sünniaeg", width=100, anchor="center")
        my_table.column("Sugu", width=50, anchor="center")
        my_table.column("Isikukood", width=100, anchor="center")

        # Tabeli päis (heading)
        my_table.heading("Eesnimi", text="Eesnimi", anchor="center")
        my_table.heading("Perenimi", text="Perenimi", anchor="center")
        my_table.heading("Sünniaeg", text="Sünniaeg", anchor="center")
        my_table.heading("Sugu", text="Sugu", anchor="center")
        my_table.heading("Isikukood", text="Isikukood", anchor="center")

        for data_str in data:
            data_str = data_str[0]
            row = data_str.strip('{}').split(';')
            my_table.insert("", "end", values=row)


        my_table.pack(fill=BOTH, expand=True)

        return my_table

    def generate_table_big(self, data):
        for child in self.__bottom_frame.winfo_children():
            child.destroy()

        my_table = ttk.Treeview(self.__bottom_frame)
        vsb = Scrollbar(self.__bottom_frame, orient=VERTICAL, command=my_table.yview)
        vsb.pack(side=RIGHT, fill=Y)
        my_table.configure(yscrollcommand=vsb.set)

        my_table["columns"] = ("Eesnimi", "Perenimi","Sugu", "Sünniaeg", "Surnud", "Asula", "Tüüp", "Maakond")

        my_table.column("#0", width=0, stretch=NO)
        my_table.column("Eesnimi", width=100, anchor="center")
        my_table.column("Perenimi", width=100, anchor="center")
        my_table.column("Sugu", width=50, anchor="center")
        my_table.column("Sünniaeg", width=100, anchor="center")
        my_table.column("Surnud", width=100, anchor="center")
        my_table.column("Asula", width=100, anchor="center")
        my_table.column("Tüüp", width=100, anchor="center")
        my_table.column("Maakond", width=100, anchor="center")

        # Tabeli päis (heading)
        my_table.heading("Eesnimi", text="Eesnimi", anchor="center")
        my_table.heading("Perenimi", text="Perenimi", anchor="center")
        my_table.heading("Sugu", text="Sugu", anchor="center")
        my_table.heading("Sünniaeg", text="Sünniaeg", anchor="center")
        my_table.heading("Surnud", text="Surnud", anchor="center")
        my_table.heading("Asula", text="Asula", anchor="center")
        my_table.heading("Tüüp", text="Tüüp", anchor="center")
        my_table.heading("Maakond", text="Maakond", anchor="center")

        for data_str in data:
            data_str = data_str[0]
            row = data_str.strip('{}').split(';')
            my_table.insert("", "end", values=row)


        # Pack the table into the frame
        #my_table.pack(padx=5, pady=2)
        my_table.pack(fill=BOTH, expand=True)

        return my_table

