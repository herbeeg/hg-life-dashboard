import tkinter as tk
import tkinter.simpledialog

class GoalDialog(tk.simpledialog.Dialog):
    def body(self, master=None):
        self.input_padding = 2

        self.goal_name_label = tk.Label(master)
        self.goal_name_label['text'] = 'Goal Name:'
        self.goal_name_label.grid(row=0, column=0, pady=self.input_padding)
        self.goal_name_input = tk.Entry(master)
        self.goal_name_input.grid(row=0, column=1, pady=self.input_padding)

        self.goal_deadline_label = tk.Label(master)
        self.goal_deadline_label['text'] = 'Deadline:'
        self.goal_deadline_label.grid(row=1, column=0, pady=self.input_padding)
        self.goal_deadline_input = tk.Entry(master)
        self.goal_deadline_input.grid(row=1, column=1, pady=self.input_padding)

        self.key_result_label = tk.Label(master)
        self.key_result_label['text'] = 'Key Results:'
        self.key_result_label.grid(row=2, column=0, columnspan=2, pady=self.input_padding)
        self.key_result_add = tk.Button(master, command=self.add_key_result)
        self.key_result_add['text'] = '-Add-'
        self.key_result_add.grid(row=3, column=0, pady=self.input_padding)
        self.key_result_input = tk.Entry(master)
        self.key_result_input.grid(row=3, column=1, pady=self.input_padding)

        return self.goal_name_input

    def apply(self):
        print(self.goal_name_input.get())

    def add_key_result(self):
        print('added')