import tkinter as tk

from functools import partial

class ScheduleGenerator(tk.Frame):
    """
    Handles widget generation of the schedule grid,
    the size and values of which are decided
    either by user input or configurations
    housed in a local JSON file.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None, hour_start=0, hour_end=23, loads={}):
        """
        If local JSON data exists, then we immediately 
        store that information in a class variable.

        Otherwise, we want to setup a new dict object
        with empty values so that we're able to
        access the variable in the same way.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
            hour_start (int, optional): Time to start the schedule grid from. Defaults to 0.
            hour_end (int, optional): Time to finish the schedule grid from. Defaults to 23.
            loads (dict, optional): Local JSON data if it exists. Defaults to {}.
        """
        super().__init__(master)
        self.master = master

        self.frame_padding = 20

        self.row_index = 1
        self.col_index = 0

        self.hour_start = hour_start
        self.hour_end = hour_end

        if loads:
            self.grid_data = loads
        else:
            self.grid_data = {
                'start': self.hour_start,
                'end': self.hour_end
            }
            
            for day in self.columnTitles():
                self.grid_data.update({day:{'data':{}}})

                for hour in list(range(self.hour_start, self.hour_end)):
                    self.grid_data[day]['data'].update({str(hour):''})

        self.createWidgets()

    def createWidgets(self):
        """
        Render the schedule grid as clickable Label text 
        containers, that allow the user to edit
        existing elements, save those changes
        to a file or discard as necessary.

        Click events are bound to a left-click on each
        generated label and allow us to track them
        individually by passing parameters to
        the callback function instead of
        storing them in variables.
        """
        for hour in list(range(self.hour_start, self.hour_end)):
            hour_display = tk.Label(self)
            hour_display['text'] = hour
            hour_display.grid(row=self.row_index, column=self.col_index, sticky='W')
            
            self.row_index += 1

        self.row_index = 0
        self.col_index += 1
        
        for day in self.columnTitles():
            day_title = tk.Label(self, width=15, padx=self.frame_padding)
            day_title['text'] = day.title()
            day_title.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

            self.row_index += 1

            for hour in list(range(self.hour_start, self.hour_end)):
                hour_area = tk.Label(self, borderwidth=2, relief='raised', pady=10)
                hour_area['text'] = self.grid_data[day]['data'][str(hour)]
                hour_area.grid(row=self.row_index, column=self.col_index, sticky='NSEW')

                hour_area.bind('<Button-1>', partial(self.master.editSchedule, label_object=hour_area, day=day, hour=hour))
                """We're able to make use of the partial() function to pass keyword arguments as required."""

                self.row_index += 1
            
            self.row_index = 0
            self.col_index += 1

    def columnTitles(self):
        """
        We convert these values to title case when
        printing them out at the top of each
        column in the schedule grid.

        Returns:
            list: Lower case versions of each weekday.
        """
        return [
            'monday',
            'tuesday',
            'wednesday',
            'thursday',
            'friday',
            'saturday',
            'sunday'
        ]

    def storeData(self, json_string):
        """
        We use this data locally when making edit
        operations to the schedule grid and
        encoding to an output file.

        Args:
            json_string (str): Condensed JSON data
        """
        self.grid_data = json_string

    def getData(self):
        """
        Getter for readability when the Schedule()
        class makes any references.

        Returns:
            str: Condensed JSON data
        """
        return self.grid_data
