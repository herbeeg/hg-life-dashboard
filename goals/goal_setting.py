import tkinter as tk

class GoalSetting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.create_widgets()

    def create_widgets(self):
        self.goal_1_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_1_button['text'] = 'New Goal'
        self.goal_1_button.grid(row=0, column=1, sticky='NSEW')

        self.goal_2_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_2_button['text'] = 'New Goal'
        self.goal_2_button.grid(row=0, column=4, sticky='NSEW')

        self.goal_3_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_3_button['text'] = 'New Goal'
        self.goal_3_button.grid(row=0, column=7, sticky='NSEW')

        self.goal_4_button = tk.Button(self, command=self.generate_goal_layout)
        self.goal_4_button['text'] = 'New Goal'
        self.goal_4_button.grid(row=0, column=10, sticky='NSEW')

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

    def generate_goal_layout(self):
        return True