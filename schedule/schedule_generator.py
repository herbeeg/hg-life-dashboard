import tkinter as tk

class ScheduleGenerator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 20

        self.create_widgets()

    def create_widgets(self):
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