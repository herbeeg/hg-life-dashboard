import tkinter.messagebox
import tkinter.simpledialog
import tkinter as tk

class GoalDialog(tk.simpledialog.Dialog):
    def body(self, master=None):
        goal_window = self._nametowidget('.!mainapp.!goalsetting')
        self.goal_config = {}

        self.input_padding = 2

        self.goal_name_label = tk.Label(master)
        self.goal_name_label['text'] = 'Goal Name:'
        self.goal_name_label.grid(row=0, column=0, pady=self.input_padding)
        self.goal_name_input = tk.Entry(master)

        if goal := goal_window.getGoalState():
            self.goal_name_input.insert(tk.END, goal[0]['text'])

        self.goal_name_input.grid(row=0, column=1, pady=self.input_padding)

        self.goal_deadline_label = tk.Label(master)
        self.goal_deadline_label['text'] = 'Deadline:'
        self.goal_deadline_label.grid(row=1, column=0, pady=self.input_padding)
        self.goal_deadline_input = tk.Entry(master)

        if goal := goal_window.getGoalState():
            self.goal_deadline_input.insert(tk.END, goal[1]['text'])

        self.goal_deadline_input.grid(row=1, column=1, pady=self.input_padding)

        self.key_result_label = tk.Label(master)
        self.key_result_label['text'] = 'Key Results:'
        self.key_result_label.grid(row=2, column=0, pady=self.input_padding)
        self.key_result_add = tk.Button(master, command=self.addKeyResult)
        self.key_result_add['text'] = '-Add-'
        self.key_result_add.grid(row=3, column=0, pady=self.input_padding)
        self.key_result_input = tk.Entry(master)
        self.key_result_input.grid(row=3, column=1, pady=self.input_padding)

        self.key_result_remove = tk.Button(master, command=self.removeKeyResult)
        self.key_result_remove['text'] = '-Remove-'
        self.key_result_remove.grid(row=4, column=0, pady=self.input_padding)
        self.key_result_list = tk.Listbox(master, selectmode=tk.SINGLE)
        self.key_result_list.grid(row=4, column=1, pady=self.input_padding)

        if goal := goal_window.getGoalState():
            for result in goal[2:]:
                self.key_result_list.insert(tk.END, result['text'])

        self.focus_force()

        return self.goal_name_input

    def validate(self):
        if not self.goal_name_input.get():
            tk.messagebox.showwarning('Bad Input Value', 'Goal name input was empty.')
            return 0

        elif not self.goal_deadline_input.get():
            tk.messagebox.showwarning('Bad Input Value', 'Goal deadline input was empty.')
            return 0

        self.goal_config = {
            'name': self.goal_name_input.get(),
            'date': self.goal_deadline_input.get(),
            'results': []
        }

        for result in self.key_result_list.get(0, tk.END):
            self.goal_config['results'].append(result)

        return 1

    def addKeyResult(self):
        if 5 > self.key_result_list.size():
            if not any(item == self.key_result_input.get() for item in self.key_result_list.get(0, tk.END)):
                """Don't allow any duplicates in the listbox tuple."""
                self.key_result_list.insert(tk.END, self.key_result_input.get())
        else:
            tk.messagebox.showwarning(title='Item Limit Reached', message='Maximum number of key result items reached.')

    def removeKeyResult(self):
        self.key_result_list.delete(tk.ANCHOR)

    def getGoalConfig(self):
        return self.goal_config
