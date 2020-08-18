import tkinter as tk

class Journal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        self.journal_input = tk.Text(self, height=20, borderwidth=50)
        self.journal_input.pack(side='top', fill='x')