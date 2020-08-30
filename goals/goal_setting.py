import tkinter as tk

from .goal_dialog import GoalDialog
from functools import partial

class GoalSetting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        self.top_padding = tk.Label(self, text='')
        self.top_padding.grid(row=0, column=0, columnspan=12, pady=10)

        self.goal_1_button = tk.Button(self, command=partial(self.generate_goal_layout, col_index=0))
        self.goal_1_button['text'] = 'New Goal'
        self.goal_1_button.grid(row=1, column=1, sticky='NSEW')

        self.goal_2_button = tk.Button(self, command=partial(self.generate_goal_layout, col_index=1))
        self.goal_2_button['text'] = 'New Goal'
        self.goal_2_button.grid(row=1, column=4, sticky='NSEW')

        self.goal_3_button = tk.Button(self, command=partial(self.generate_goal_layout, col_index=2))
        self.goal_3_button['text'] = 'New Goal'
        self.goal_3_button.grid(row=1, column=7, sticky='NSEW')

        self.goal_4_button = tk.Button(self, command=partial(self.generate_goal_layout, col_index=3))
        self.goal_4_button['text'] = 'New Goal'
        self.goal_4_button.grid(row=1, column=10, sticky='NSEW')

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

    def generate_goal_layout(self, col_index):
        self.goal_dialog = GoalDialog(self.master)
        """Wait for user to fill in the dialog options or cancel the operation."""
        print(self.goal_dialog.get_goal_config())