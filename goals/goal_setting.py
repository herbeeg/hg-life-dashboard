import tkinter as tk

from .goal_dialog import GoalDialog

class GoalSetting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        self.top_padding = tk.Label(self, text='')
        self.top_padding.grid(row=0, column=0, columnspan=12, pady=10)

        self.goal_1_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_1_button['text'] = 'New Goal'
        self.goal_1_button.grid(row=1, column=1, sticky='NSEW')

        self.goal_2_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_2_button['text'] = 'New Goal'
        self.goal_2_button.grid(row=1, column=4, sticky='NSEW')

        self.goal_3_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_3_button['text'] = 'New Goal'
        self.goal_3_button.grid(row=1, column=7, sticky='NSEW')

        self.goal_4_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_4_button['text'] = 'New Goal'
        self.goal_4_button.grid(row=1, column=10, sticky='NSEW')

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

    def generate_goal_layout(self):
        self.goal_dialog = GoalDialog(self.master)