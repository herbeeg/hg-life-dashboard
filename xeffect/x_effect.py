import tkinter.font
import tkinter as tk
import calendar
import json
import os

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

        self.print_calendar_title('August 2020')
        self.xeffect_data = self.load_xeffect_data()

    def create_widget(self, widget_item={}):
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
                checkbox = tk.Checkbutton(self, command=partial(self.save_xeffect_data, parent=data['title'], index=(count + 1)))
                checkbox.grid(row=self.row_index, column=self.col_index)

                if (count + 1) in data['checked']:
                    """We use the actual date rather than the index in the JSON file."""
                    checkbox.toggle()

                self.col_index += 1

            self.row_index += 1
            self.col_index = 0

    def load_xeffect_data(self):
        """
        If the provided file naming convention does not match
        anything in the given directory, then the user is
        allowed to choose a file of their own to help
        with moving files and builds around.

        Raises:
            FileNotFoundError: Fail if the file does not exist in the given location

        Raises:
            TypeError: Fail if the file does not have the .json extension
        """
        try:
            with open(self.master.get_working_directory() + self.data_directory + 'ld_august_2020.json') as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            try:
                filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Load Data', filetypes=[('JSON Files', '*.json')]))
            except TypeError as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='No valid file selected')

                self.master.load_view('menu')
                """Return to the main menu if there is a problem while loading a file."""
                return

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    json_data = json.load(file)

                    self.print_calendar_dates(self.calendar)

                    for item in json_data['items']:
                        self.create_widget(item)

                    self.finished_loading = True
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

        return json_data

    def save_xeffect_data(self, parent, index):
        print(parent)
        print(index)
        if False == self.finished_loading:
            return None

    def print_calendar_dates(self, dates):
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

    def print_calendar_title(self, title):
        label = tk.Label(self, font=self.title_label_font)
        label['text'] = title
        label.grid(row=self.row_index, column=self.col_index, columnspan=len(self.calendar), pady=10)

        self.row_index += 1
