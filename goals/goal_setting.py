import json
import os
import tkinter as tk

from .goal_dialog import GoalDialog
from.goal_frame import GoalFrame
from functools import partial

class GoalSetting(tk.Frame):
    """
    Allowing users to create up to four goals which 
    can be edited via a simple custom dialog box, 
    allowing for name, deadline and key result 
    updates.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

        self.data_directory = '/goals/data/goals.json'

        self.editing_goal = False
        self.goal_state = {}

        self.createWidgets()

    def createWidgets(self):
        top_padding = tk.Label(self, text='')
        top_padding.grid(row=0, column=0, columnspan=12, pady=10)

        button_text = 'New Goal'

        self.goal_1_new = tk.Button(self, command=partial(self.generateGoalLayout, col_index=1))
        self.goal_1_new['text'] = button_text
        self.goal_1_new.grid(row=1, column=1, sticky='NSEW')

        self.goal_2_new = tk.Button(self, command=partial(self.generateGoalLayout, col_index=4))
        self.goal_2_new['text'] = button_text
        self.goal_2_new.grid(row=1, column=4, sticky='NSEW')

        self.goal_3_new = tk.Button(self, command=partial(self.generateGoalLayout, col_index=7))
        self.goal_3_new['text'] = button_text
        self.goal_3_new.grid(row=1, column=7, sticky='NSEW')

        self.goal_4_new = tk.Button(self, command=partial(self.generateGoalLayout, col_index=10))
        self.goal_4_new['text'] = button_text
        self.goal_4_new.grid(row=1, column=10, sticky='NSEW')

        bot_padding = tk.Label(self, text='')
        bot_padding.grid(row=2, column=0, columnspan=12, pady=10)

        for col in range(12):
            self.grid_columnconfigure(col, weight=1, uniform='goals')

        self.maybeLoadGoals()

    def generateGoalLayout(self, col_index, new_goal=True, bypass_dialog=False):
        if new_goal:
            self.goal_state = {}

        if not bypass_dialog:
            self.goal_dialog = GoalDialog(self.master, title='Edit Goal')
            """Wait for user to fill in the dialog options or cancel the operation."""

            if not self.goal_dialog.getGoalConfig():
                return

        button_text = 'Edit Goal'

        if 1 == col_index:
            self.goal_1_new.destroy()

            if self.editing_goal:
                self.goal_1_frame.destroy()
            
            self.goal_1_frame = GoalFrame(self, 'goal_1_frame')

            self.goal_1_edit = tk.Button(self, command=partial(self.editGoalLayout, col_index=1))
            self.goal_1_edit['text'] = button_text
            self.goal_1_edit.grid(row=1, column=0, columnspan=3)

            self.loadGoalLayout(self.goal_1_frame)
            self.goal_1_frame.grid(row=3, column=0, columnspan=3)
        elif 4 == col_index:
            self.goal_2_new.destroy()

            if self.editing_goal:
                self.goal_2_frame.destroy()
            
            self.goal_2_frame = GoalFrame(self, 'goal_2_frame')

            self.goal_2_edit = tk.Button(self, command=partial(self.editGoalLayout, col_index=4))
            self.goal_2_edit['text'] = button_text
            self.goal_2_edit.grid(row=1, column=3, columnspan=3)

            self.loadGoalLayout(self.goal_2_frame)
            self.goal_2_frame.grid(row=3, column=3, columnspan=3)
        elif 7 == col_index:
            self.goal_3_new.destroy()

            if self.editing_goal:
                self.goal_3_frame.destroy()
            
            self.goal_3_frame = GoalFrame(self, 'goal_3_frame')

            self.goal_3_edit = tk.Button(self, command=partial(self.editGoalLayout, col_index=7))
            self.goal_3_edit['text'] = button_text
            self.goal_3_edit.grid(row=1, column=6, columnspan=3)

            self.loadGoalLayout(self.goal_3_frame)
            self.goal_3_frame.grid(row=3, column=6, columnspan=3)
        elif 10 == col_index:
            self.goal_4_new.destroy()

            if self.editing_goal:
                self.goal_4_frame.destroy()
            
            self.goal_4_frame = GoalFrame(self, 'goal_4_frame')

            self.goal_4_edit = tk.Button(self, command=partial(self.editGoalLayout, col_index=10))
            self.goal_4_edit['text'] = button_text
            self.goal_4_edit.grid(row=1, column=9, columnspan=3)

            self.loadGoalLayout(self.goal_4_frame)
            self.goal_4_frame.grid(row=3, column=9, columnspan=3)

        self.editing_goal = False

    def loadGoalLayout(self, frame):
        if hasattr(self, 'json_data'):
            if self.json_data[frame.getName()]:
                goal_data = self.json_data[frame.getName()]
            else:
                return
        else: 
            goal_data = self.goal_dialog.getGoalConfig()

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

        self.saveGoalData(frame.getName(), goal_data)

    def editGoalLayout(self, col_index):
        if 1 == col_index:
            self.goal_state = self.goal_1_frame.winfo_children()
        elif 4 == col_index:
            self.goal_state = self.goal_2_frame.winfo_children()
        elif 7 == col_index:
            self.goal_state = self.goal_3_frame.winfo_children()
        elif 10 == col_index:
            self.goal_state = self.goal_4_frame.winfo_children()

        self.editing_goal = True
        self.generateGoalLayout(col_index, new_goal=False)

    def getGoalState(self):
        return self.goal_state

    def maybeLoadGoals(self):
        try:
            with open(self.master.getWorkingDirectory() + self.data_directory) as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            tk.messagebox.showwarning(title='Couldn\'t Load Data', message='No valid file found.')
            """The user can continue to create new goals no local data is required."""
            
            return

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    self.json_data = json.load(file)

                    if self.json_data['goal_1_frame']:
                        self.generateGoalLayout(1, bypass_dialog=True)
                    if self.json_data['goal_2_frame']:
                        self.generateGoalLayout(4, bypass_dialog=True)
                    if self.json_data['goal_3_frame']:
                        self.generateGoalLayout(7, bypass_dialog=True)
                    if self.json_data['goal_4_frame']:
                        self.generateGoalLayout(10, bypass_dialog=True)

            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

        delattr(self, 'json_data')

    def saveGoalData(self, name, data={}):
        try:
            with open(self.master.getWorkingDirectory() + self.data_directory) as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            tk.messagebox.showwarning(title='Couldn\'t Load Data', message='No valid file found.')
            """The user can continue to create new goals no local data is required."""
            
            return

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    json_import = json.load(file)

                    if json_import[name] or {} == json_import[name]:
                        json_import[name] = data
                        self.writeToFile(json.dumps(json_import))

            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def writeToFile(self, encoded_json):
        """
        The JSON gets condensed down into a single line 
        but retains the whitespace to maintain some
        readability as required.

        Args:
            encoded_json (str): Compressed JSON data
        """
        try:
            with open(self.master.getWorkingDirectory() + self.data_directory, 'w+') as json_file:
                file_contents = encoded_json
                json_file.write(file_contents)
                json_file.close()
        except Exception as ex:
            tk.messagebox.showerror(title='Error Saving Data', message='Unable to save file %s' % json_file.name)