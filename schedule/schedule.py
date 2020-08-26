import tkinter as tk

class Schedule(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 10
        self.button_padding = 30

        self.create_widgets()

    def create_widgets(self):
        hours = list(range(24))

        self.day_start = tk.StringVar(self.master)
        self.day_start.set('0')

        self.day_end = tk.StringVar(self.master)
        self.day_end.set('0')

        self.end_time_label = tk.Label(self)
        self.end_time_label['text'] = 'End Time:'
        self.end_time_label.pack(side='left', pady=self.frame_padding)

        self.end_time_input = tk.OptionMenu(self, self.day_end, *hours)
        self.end_time_input.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.start_time_label = tk.Label(self)
        self.start_time_label['text'] = 'Start Time:'
        self.start_time_label.pack(side='left', pady=self.frame_padding)

        self.start_time_input = tk.OptionMenu(self, self.day_start, *hours)
        self.start_time_input.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.generate_button = tk.Button(self, padx=self.button_padding, command=self.generate_week_schedule)
        self.generate_button['text'] = 'Generate'
        self.generate_button.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        return True

    def generate_week_schedule(self):
        return True
