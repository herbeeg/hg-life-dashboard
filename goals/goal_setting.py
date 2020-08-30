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

        button_text = 'New Goal'

        self.goal_1_new = tk.Button(self, command=partial(self.generate_goal_layout, col_index=1))
        self.goal_1_new['text'] = button_text
        self.goal_1_new.grid(row=1, column=1, sticky='NSEW')

        self.goal_2_new = tk.Button(self, command=partial(self.generate_goal_layout, col_index=4))
        self.goal_2_new['text'] = button_text
        self.goal_2_new.grid(row=1, column=4, sticky='NSEW')

        self.goal_3_new = tk.Button(self, command=partial(self.generate_goal_layout, col_index=7))
        self.goal_3_new['text'] = button_text
        self.goal_3_new.grid(row=1, column=7, sticky='NSEW')

        self.goal_4_new = tk.Button(self, command=partial(self.generate_goal_layout, col_index=10))
        self.goal_4_new['text'] = button_text
        self.goal_4_new.grid(row=1, column=10, sticky='NSEW')

        self.bot_padding = tk.Label(self, text='')
        self.bot_padding.grid(row=2, column=0, columnspan=12, pady=10)

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

    def generate_goal_layout(self, col_index):
        self.goal_dialog = GoalDialog(self.master)
        """Wait for user to fill in the dialog options or cancel the operation."""

        button_text = 'Edit Goal'

        if 1 == col_index:
            self.goal_1_new.destroy()
            self.goal_1_edit = tk.Button(self, command=partial(self.edit_goal_layout, col_index=1))
            self.goal_1_edit['text'] = button_text
            self.goal_1_edit.grid(row=1, column=0, columnspan=3)
        elif 4 == col_index:
            self.goal_2_button.destroy()
        elif 7 == col_index:
            self.goal_3_button.destroy()
        elif 10 == col_index:
            self.goal_4_button.destroy()

        self.grid_columnconfigure(col_index-1, weight=1, uniform='')
        self.grid_columnconfigure(col_index, weight=1, uniform='')
        self.grid_columnconfigure(col_index+1, weight=1, uniform='')
        
        label = tk.Label(self)
        label['text'] = 'Goal 1: ' + self.goal_dialog.get_goal_config()['name']
        label.grid(row=3, column=0, columnspan=3)

    def edit_goal_layout(self, col_index):
        return True
