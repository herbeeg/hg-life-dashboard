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

        self.key_result_remove = tk.Button(master, command=self.remove_key_result)
        self.key_result_remove['text'] = '-Remove-'
        self.key_result_remove.grid(row=4, column=0, pady=self.input_padding)
        self.key_result_list = tk.Listbox(master, selectmode=tk.SINGLE)
        self.key_result_list.grid(row=4, column=1, pady=self.input_padding)

        return self.goal_name_input

    def apply(self):
        print(self.goal_name_input.get())

    def add_key_result(self):
        if 5 > self.key_result_list.size():
            if not any(self.key_result_input.get() in item for item in self.key_result_list.get(0, tk.END)):
                """Don't allow any duplicates in the listbox tuple."""
                self.key_result_list.insert(tk.END, self.key_result_input.get())
        else:
            tk.messagebox.showwarning(title='Item Limit Reached', message='Maximum number of key result items reached.')

    def remove_key_result(self):
        self.key_result_list.delete(tk.ANCHOR)