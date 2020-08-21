import tkinter as tk
import calendar
import json
import os

from datetime import datetime

class XEffect(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.data_directory = '/xeffect/data/'
        self.row_index = 0
        self.col_index = 0

        self.xeffect_data = self.load_xeffect_data()

        self.format_calendar_month(datetime.now().month)

    def create_widget(self, widget_item={}):
        print(widget_item)

        background_colour = widget_item['colour']

        title_label = tk.Label(self, bg=background_colour)
        title_label['text'] = widget_item['title']
        title_label.grid(row=self.row_index, column=self.col_index)

        self.row_index += 1

        for data in widget_item['data']:
            label = tk.Label(self, bg=background_colour)
            label['text'] = data['title']
            label.grid(row=self.row_index, column=self.col_index)

            self.row_index += 1

        return True

    def load_xeffect_data(self):
        try:
            with open(self.master.get_working_directory() + self.data_directory + 'ld_august_2020.json') as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            try:
                filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Load Data', filetypes=[('JSON Files', '*.json')]))
            except TypeError as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='No valid file selected')

                self.master.load_view('menu')
                return

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    json_data = json.load(file)

                    for item in json_data['items']:
                        self.create_widget(item)

            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def format_calendar_month(self, month):
        return True
