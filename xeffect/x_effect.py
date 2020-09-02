import tkinter.font
import tkinter as tk
import calendar
import json
import os

from app_constants import AppConstants
from datetime import datetime
from functools import partial

class XEffect(tk.Frame):
    """
    Builds all of the calendar frame elements and 
    contains logic for loading and saving the
    current window state when the user is
    toggling checkboxes.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Set initial grid inboxes, title label fonts
        and calendar data for the current month.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

        self.finished_loading = False

        self.title_label_font = tk.font.Font(family='TkDefaultFont', weight='bold')

        self.data_directory = '/xeffect/data/'
        self.row_index = 0
        self.col_index = 1

        self.calendar = calendar.Calendar().itermonthdays(datetime.now().year, datetime.now().month)
        self.calendar = [d for d in self.calendar if 0 != d]
        """Using list comprehension to remove padded calendar dates."""

        self.current_month_year = calendar.month_name[datetime.now().month].lower() + ' ' + str(datetime.now().year)
        self.search_filename = AppConstants.filePreface() + self.current_month_year.replace(' ', '_') + '.json'
        """Calendar and date conversion for dynamic filename loading and title."""

        self.printCalendarTitle(self.current_month_year.title())
        self.xeffect_data = self.loadXeffectData()

    def createWidget(self, widget_item={}):
        """
        Each item group is classed as a widget, with their
        own titles, colours and rows of data.

        The data is traversed and the labels and
        checkboxes will be rendered out, the
        amount being decided based on the
        current month.

        Args:
            widget_item (dict, optional): The widget data pulled from the existing JSON. Defaults to {}.
        """
        background_colour = widget_item['colour']
        foreground_colour = '#ffffff'

        title_label = tk.Label(self, bg=background_colour, fg=foreground_colour, font=self.title_label_font)
        title_label['text'] = widget_item['title']
        title_label.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

        self.row_index += 1

        for data in widget_item['data']:
            label = tk.Label(self, bg=background_colour, fg=foreground_colour)
            label['text'] = data['title']
            label.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

            self.col_index += 1

            for count in range(len(self.calendar)):
                checkbox = tk.Checkbutton(self, command=partial(self.saveXeffectData, parent=data['title'], index=(count + 1)))
                """We can track the unique title and checkbox index individually by passing them as parameters to the callable function when clicked."""
                checkbox.grid(row=self.row_index, column=self.col_index)

                if (count + 1) in data['checked']:
                    """We use the actual date rather than the index in the JSON file."""
                    checkbox.toggle()

                self.col_index += 1

            self.row_index += 1
            self.col_index = 0

    def loadXeffectData(self):
        """
        If the provided file naming convention does not match
        anything in the given directory, then the user is
        allowed to choose a file of their own to help
        with moving files and builds around.

        We store a copy of the loaded data in a variable
        that we can modify as changes are made by the 
        user so it's much quicker and easier to
        encode and save that back to a file. 

        Raises:
            FileNotFoundError: Fail if the file does not exist in the given location

        Raises:
            TypeError: Fail if the file does not have the .json extension

        Returns:
            dict: The JSON file contents, converted.
        """
        try:
            with open(self.master.getWorkingDirectory() + self.data_directory + self.search_filename) as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            try:
                filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Load Data', filetypes=[('JSON Files', '*.json')]))
            except TypeError as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='No valid file selected')

                self.master.loadView('menu')
                """Return to the main menu if there is a problem while loading a file."""
                return

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    json_data = json.load(file)

                    self.printCalendarDates(self.calendar)

                    for item in json_data['items']:
                        self.createWidget(item)

                    self.finished_loading = True
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

        return json_data

    def saveXeffectData(self, parent, index):
        """
        The loaded JSON data is stored locally so we're
        just able to reference the class variable
        contents to encode what's required to 
        save back to the existing file.

        Args:
            parent (str): The row title for the checkbox
            index (int): The grid position of the checkbox

        Returns:
            None: If the grid element is still loading
        """
        if False == self.finished_loading:
            """Wait until the checkbox grid has finished loading before allowing any save operations."""
            return None
        
        for item in self.xeffect_data['items']:
            for data in item['data']:
                if data['title'] == parent:
                    if index in data['checked']:
                        data['checked'].remove(index)
                    else:
                        data['checked'].append(index)
                        data['checked'].sort()

                    self.writeToFile(json.dumps(self.xeffect_data))

    def writeToFile(self, encoded_json):
        """
        The JSON gets condensed down into a single line 
        but retains the whitespace to maintain some
        readability as required.

        Args:
            encoded_json (str): Compressed JSON data
        """
        try:
            with open(self.master.getWorkingDirectory() + self.data_directory + self.search_filename, 'w+') as json_file:
                file_contents = encoded_json
                json_file.write(file_contents)
                json_file.close()
        except Exception as ex:
            tk.messagebox.showerror(title='Error Saving Data', message='Unable to save file %s' % json_file.name)

    def printCalendarDates(self, dates):
        """
        Render out the calendar dates at the top of the
        grid layout, ensuring that the number of
        digits for each column is the same.

        Args:
            dates (Iterator): List of day numbers for the current month
        """
        for date in dates:
            label = tk.Label(self, bg='#ffffff', fg='#000000', font=self.title_label_font)
            label['text'] = str(date).zfill(2)
            """Prefix any single digit dates with a zero."""
            label.grid(row=self.row_index, column=self.col_index)

            self.col_index += 1

        self.row_index += 1
        self.col_index = 0

    def printCalendarTitle(self, title):
        """
        The calendar title needs to stretch across the entirity
        of the container so it can be centered correctly
        and we can retain the grid structure. 
        
        Therefore, the columnspan parameter is used when
        drawing the grid element. This is based on the 
        amount of days for that given month.

        Args:
            title (str): The current month and year combined
        """
        label = tk.Label(self, font=self.title_label_font)
        label['text'] = title
        label.grid(row=self.row_index, column=self.col_index, columnspan=len(self.calendar), pady=10)

        self.row_index += 1
