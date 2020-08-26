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
        
        for day in self.column_titles():
            for hour in list(range(24)):
                return True

        return True

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