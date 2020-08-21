import tkinter as tk
import calendar
import json
import os

from datetime import datetime

class XEffect(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.xeffect_data = self.load_xeffect_data()

        self.format_calendar_month(datetime.now().month)
        self.create_widgets()

    def create_widgets(self):
        return True

    def load_xeffect_data(self):
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
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def format_calendar_month(self, month):
        return True