import tkinter as tk
import tkinter.simpledialog

class GoalDialog(tk.simpledialog.Dialog):
    def body(self, master=None):
        self.goal_name_label = tk.Label(master, text='Goal Name:')
        self.goal_name_label.grid(row=0, column=0)

        self.goal_name_input = tk.Entry(master)
        self.goal_name_input.grid(row=0, column=1)

        return self.goal_name_input

    def apply(self):
        print(self.goal_name_input.get())