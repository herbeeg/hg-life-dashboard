import tkinter as tk

from .goal_dialog import GoalDialog
from functools import partial

class GoalSetting(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.editing_goal = False
        self.goal_state = {}

        self.create_widgets()

    def create_widgets(self):
        top_padding = tk.Label(self, text='')
        top_padding.grid(row=0, column=0, columnspan=12, pady=10)

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

        bot_padding = tk.Label(self, text='')
        bot_padding.grid(row=2, column=0, columnspan=12, pady=10)

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

    def generate_goal_layout(self, col_index, new_goal=True):
        if new_goal:
            self.goal_state = {}

        self.goal_dialog = GoalDialog(self.master, title='Edit Goal')
        """Wait for user to fill in the dialog options or cancel the operation."""

        if not self.goal_dialog.get_goal_config():
            return

        button_text = 'Edit Goal'

        if 1 == col_index:
            self.goal_1_new.destroy()

            if self.editing_goal:
                self.goal_1_frame.destroy()
            
            self.goal_1_frame = tk.Frame(self)

            self.goal_1_edit = tk.Button(self, command=partial(self.edit_goal_layout, col_index=1))
            self.goal_1_edit['text'] = button_text
            self.goal_1_edit.grid(row=1, column=0, columnspan=3)

            self.load_goal_layout(self.goal_1_frame)
            self.goal_1_frame.grid(row=3, column=0, columnspan=3)
        elif 4 == col_index:
            self.goal_2_new.destroy()

            if self.editing_goal:
                self.goal_2_frame.destroy()
            
            self.goal_2_frame = tk.Frame(self)

            self.goal_2_edit = tk.Button(self, command=partial(self.edit_goal_layout, col_index=4))
            self.goal_2_edit['text'] = button_text
            self.goal_2_edit.grid(row=1, column=3, columnspan=3)

            self.load_goal_layout(self.goal_2_frame)
            self.goal_2_frame.grid(row=3, column=3, columnspan=3)
        elif 7 == col_index:
            self.goal_3_new.destroy()

            if self.editing_goal:
                self.goal_3_frame.destroy()
            
            self.goal_3_frame = tk.Frame(self)

            self.goal_3_edit = tk.Button(self, command=partial(self.edit_goal_layout, col_index=7))
            self.goal_3_edit['text'] = button_text
            self.goal_3_edit.grid(row=1, column=6, columnspan=3)

            self.load_goal_layout(self.goal_3_frame)
            self.goal_3_frame.grid(row=3, column=6, columnspan=3)
        elif 10 == col_index:
            self.goal_4_new.destroy()

            if self.editing_goal:
                self.goal_4_frame.destroy()
            
            self.goal_4_frame = tk.Frame(self)

            self.goal_4_edit = tk.Button(self, command=partial(self.edit_goal_layout, col_index=10))
            self.goal_4_edit['text'] = button_text
            self.goal_4_edit.grid(row=1, column=9, columnspan=3)

            self.load_goal_layout(self.goal_4_frame)
            self.goal_4_frame.grid(row=3, column=9, columnspan=3)

        self.editing_goal = False

    def load_goal_layout(self, frame):
        goal_data = self.goal_dialog.get_goal_config()

        title = tk.Label(frame)
        title['text'] = goal_data['name']
        title.grid(row=0, column=0, pady=5)

        deadline = tk.Label(frame)
        deadline['text'] = goal_data['date']
        deadline.grid(row=1, column=0, pady=5)

        for index, item in enumerate(goal_data['results'], start=1):
            """Allowing access to the index for text and positioning use."""
            result = tk.Label(frame)
            result['text'] = item
            result.grid(row=index+1, column=0, pady=5)

    def edit_goal_layout(self, col_index):
        if 1 == col_index:
            self.goal_state = self.goal_1_frame.winfo_children()
        elif 4 == col_index:
            self.goal_state = self.goal_2_frame.winfo_children()
        elif 7 == col_index:
            self.goal_state = self.goal_3_frame.winfo_children()
        elif 10 == col_index:
            self.goal_state = self.goal_4_frame.winfo_children()

        self.editing_goal = True
        self.generate_goal_layout(col_index, False)

    def get_goal_state(self):
        return self.goal_state