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
        Setting data load directory and initialising
        required state tracking variables.

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
        """
        Render all goal columns and assign them a button
        action and index value. 
        
        If there is a local JSON data file present,
        this will be scanned for loading first
        before any user interaction takes
        place. 
        """
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
            """Assigning each column to a group allows control of the grid widths."""

        self.maybeLoadGoals()

    def generateGoalLayout(self, col_index, new_goal=True, bypass_dialog=False):
        """
        Based on which goal column group we want to
        update, those button and label elements
        are updated based on the feedback
        data from the custom dialog.

        Args:
            col_index (int): Index to specify central column of grid group
            new_goal (bool): Whether user is creating a goal or editing
            bypass_dialog (bool): Whether custom dialog should be skipped during JSON loading
        """
        if new_goal:
            self.goal_state = {}
            """Reset the stored dialog data if we're creating a new goal."""

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
                """Get rid of any pre-existing data to prevent frame overlap."""
            
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
        """
        Display the data for a single goal in it's grid
        frame, based on whether that's been loaded
        from the local JSON file or from the
        user's completed dialog inputs.

        Args:
            frame (GoalFrame): Frame object to get the correct JSON key from
        """
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
        """Once data has been loaded into the grid frame, we update the local JSON."""

    def editGoalLayout(self, col_index):
        """
        The state of the goal application is based on
        what buttons have been clicked and which
        widgets should therefore be updated.

        Args:
            col_index (int): Which grid group we want to change
        """
        if 1 == col_index:
            self.goal_state = self.goal_1_frame.winfo_children()
            """Get all of the child widgets for the frame to iterate through to retrieve necessary data."""
        elif 4 == col_index:
            self.goal_state = self.goal_2_frame.winfo_children()
        elif 7 == col_index:
            self.goal_state = self.goal_3_frame.winfo_children()
        elif 10 == col_index:
            self.goal_state = self.goal_4_frame.winfo_children()

        self.editing_goal = True
        """When the layout is updated, know whether to destroy the exisiting goal frame."""
        self.generateGoalLayout(col_index, new_goal=False)

    def getGoalState(self):
        """
        Used by the custom dialog to decide whether
        existing data should be populated into
        the entry fields when a new dialog
        box is generated.

        Returns:
            dict: Current child widget states for a frame
        """
        return self.goal_state

    def maybeLoadGoals(self):
        """
        If a valid local JSON file exists, then we use 
        that to load data into the existing grid  
        columns with the specified name, date
        and result attributes for each.

        Raises:
            FileNotFoundError: If the specific named file does not exist

        Raises:
            TypeError: If the file does not have the '.json' extension
        """
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
                        """Bypassing the dialog tells our application that we want to load data into the goal frames."""
                    if self.json_data['goal_2_frame']:
                        self.generateGoalLayout(4, bypass_dialog=True)
                    if self.json_data['goal_3_frame']:
                        self.generateGoalLayout(7, bypass_dialog=True)
                    if self.json_data['goal_4_frame']:
                        self.generateGoalLayout(10, bypass_dialog=True)

            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

        delattr(self, 'json_data')
        """Allows local JSON file checks to fail again so existing goals can be editied."""

    def saveGoalData(self, name, data={}):
        """
        Write encoded JSON to a specified directory and
        filename whenever entry fields in a custom
        goal dialog are completed successfully.

        Raises:
            FileNotFoundError: If the specific named file does not exist

        Raises:
            TypeError: If the file does not have the '.json' extension
        """
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