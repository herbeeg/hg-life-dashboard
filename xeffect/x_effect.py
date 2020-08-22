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
        self.col_index = 0

        self.search_date = str(datetime.now().year) + '-' + str(datetime.now().month).zfill(2) + '-'
        self.calendar = calendar.Calendar().itermonthdates(datetime.now().year, datetime.now().month)
        self.calendar = [x for x in self.calendar if str(x).startswith(self.search_date)]

        self.xeffect_data = self.load_xeffect_data()

    def create_widget(self, widget_item={}):
        print(widget_item)

        background_colour = widget_item['colour']
        foreground_colour = '#ffffff'

        title_label = tk.Label(self, bg=background_colour, fg=foreground_colour, font=self.title_label_font)
        title_label['text'] = widget_item['title']
        title_label.grid(row=self.row_index, column=self.col_index)

        self.row_index += 1

        for data in widget_item['data']:
            label = tk.Label(self, bg=background_colour, fg=foreground_colour)
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

                    self.print_calendar_dates(self.calendar)

                    for item in json_data['items']:
                        self.create_widget(item)

            except Exception as ex:
                print(ex)
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def print_calendar_dates(self, dates):
        for date in dates:
            label = tk.Label(self, image=self.generate_date_image(date))
            label.grid(row=self.row_index, column=self.col_index)

            self.col_index += 1

        self.row_index += 1

    def generate_date_image(self, text):
        text = str(text)

        image = Image.new(mode='RGB', size=(20,100), color=(0, 0, 0))
        text_image = ImageDraw.Draw(image)
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 12)
        text_image.text((0, 45), text, font=fnt)

        image = image.rotate(90)
        image.save('test.png')

        return image