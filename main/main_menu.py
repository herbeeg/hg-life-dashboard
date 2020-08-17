import tkinter as tk

class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 10
        self.button_padding = 50

        self.create_widgets()

    def create_widgets(self):
        self.budgets_open = tk.Button(self, padx=self.button_padding)
        self.budgets_open['text'] = 'Budget'
        self.budgets_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.xeffect_open = tk.Button(self, padx=self.button_padding)
        self.xeffect_open['text'] = 'X-Effect'
        self.xeffect_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.goals_open = tk.Button(self, padx=self.button_padding)
        self.goals_open['text'] = 'Goal Setting'
        self.goals_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.schedules_open = tk.Button(self, padx=self.button_padding)
        self.schedules_open['text'] = 'Schedule'
        self.schedules_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.journal_open = tk.Button(self, padx=self.button_padding)
        self.journal_open['text'] = 'Journal'
        self.journal_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)