import tkinter as tk

from functools import partial

class ScheduleGenerator(tk.Frame):
    def __init__(self, master=None, hour_start=0, hour_end=23):
        super().__init__(master)
        self.master = master

        self.frame_padding = 20

        self.row_index = 1
        self.col_index = 0

        self.hour_start = hour_start
        self.hour_end = hour_end

        self.create_widgets()

    def create_widgets(self):
        for hour in list(range(self.hour_start, self.hour_end)):
            hour_display = tk.Label(self)
            hour_display['text'] = hour
            hour_display.grid(row=self.row_index, column=self.col_index, sticky='W')
            
            self.row_index += 1

        self.row_index = 0
        self.col_index += 1
        
        for day in self.column_titles():
            day_title = tk.Label(self, width=15, padx=self.frame_padding)
            day_title['text'] = day
            day_title.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

            self.row_index += 1

            for hour in list(range(self.hour_start, self.hour_end)):
                hour_area = tk.Label(self, borderwidth=2, relief='raised', pady=10)
                hour_area['text'] = day + ' ' + str(hour)
                hour_area.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

                hour_area.bind('<Button-1>', partial(self.master.edit_schedule, label_object=hour_area))
                """We're able to make use of the partial() function to pass keyword arguments as required."""

                self.row_index += 1
            
            self.row_index = 0
            self.col_index += 1

    def column_titles(self):
        return [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ]