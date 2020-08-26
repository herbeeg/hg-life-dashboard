import tkinter as tk

class ScheduleGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 20

        self.row_index = 1
        self.col_index = 0

        self.create_widgets()

    def create_widgets(self):
        for hour in list(range(24)):
            hour_display = tk.Label(self)
            hour_display['text'] = hour
            hour_display.grid(row=self.row_index, column=self.col_index, sticky='W')
            
            self.row_index += 1

        self.row_index = 0
        self.col_index += 1
        
        for day in self.column_titles():
            day_title = tk.Label(self, width=10, padx=self.frame_padding)
            day_title['text'] = day
            day_title.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

            self.row_index += 1

            for hour in list(range(24)):
                hour_area = tk.Label(self, borderwidth=2, relief='groove', pady=10)
                hour_area['text'] = day + ' ' + str(hour)
                hour_area.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

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