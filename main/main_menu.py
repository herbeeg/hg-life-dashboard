import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.budgets_frame = tk.LabelFrame(self)
        self.budgets_frame['text'] = 'Budgets'
        self.budgets_frame.pack()

        self.budgets_open = tk.Button(self.budgets_frame)
        self.budgets_open['text'] = 'Open'
        self.budgets_open.pack()