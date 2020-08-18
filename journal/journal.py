import tkinter as tk

class Journal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.button_padding = 50

        self.create_widgets()

    def create_widgets(self):
        self.journal_input = tk.Text(self, height=20, borderwidth=50)
        self.journal_input.pack(side='top', fill='both')

        self.journal_delete = tk.Button(self, padx=self.button_padding)
        self.journal_delete['text'] = 'Delete'
        self.journal_delete.pack(side='right', fill='x')

        self.journal_save = tk.Button(self, padx=self.button_padding)
        self.journal_save['text'] = 'Save'
        self.journal_save.pack(side='right', fill='x')

        self.journal_load = tk.Button(self, padx=self.button_padding)
        self.journal_load['text'] = 'Load'
        self.journal_load.pack(side='right', fill='x')
