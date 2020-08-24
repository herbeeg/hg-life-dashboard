import tkinter.font
import tkinter as tk
import calendar
import json
import os

from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageTk

class XEffect(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.title_label_font = tk.font.Font(family='TkDefaultFont', weight='bold')

        self.data_directory = '/xeffect/data/'
        self.row_index = 0
        self.col_index = 1

        self.calendar = calendar.Calendar().itermonthdays(datetime.now().year, datetime.now().month)
        self.calendar = [d for d in self.calendar if 0 != d]

        self.xeffect_data = self.load_xeffect_data()

    def create_widget(self, widget_item={}):
        background_colour = widget_item['colour']
        foreground_colour = '#ffffff'

        title_label = tk.Label(self, bg=background_colour, fg=foreground_colour, font=self.title_label_font)
        title_label['text'] = widget_item['title']
        title_label.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

        self.row_index += 1

        for data in widget_item['data']:
            label = tk.Label(self, bg=background_colour, fg=foreground_colour)
            label['text'] = data['title']
            label.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

            self.col_index += 1

            for count in range(len(self.calendar)):
                checkbox = tk.Checkbutton(self)
                checkbox.grid(row=self.row_index, column=self.col_index)

                if (count + 1) in data['checked']:
                    checkbox.toggle()

                self.col_index += 1

            self.row_index += 1
            self.col_index = 0

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

                    self.print_calendar_dates(self.calendar)

                    for item in json_data['items']:
                        self.create_widget(item)

            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def print_calendar_dates(self, dates):
        for date in dates:
            label = tk.Label(self, bg='#ffffff', fg='#000000', font=self.title_label_font)
            label['text'] = str(date).zfill(2)
            label.grid(row=self.row_index, column=self.col_index)

            self.col_index += 1

        self.row_index += 1
        self.col_index = 0