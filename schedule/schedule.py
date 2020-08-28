import json
import os
import tkinter.simpledialog
import tkinter as tk

from .schedule_generator import ScheduleGenerator

class Schedule(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.data_directory = '/schedule/data/weekly_schedule.json'

        self.frame_padding = 10
        self.button_padding = 30

        self.create_widgets()

    def create_widgets(self):
        hours = list(range(24))

        self.generation_options = tk.Frame(self)

        self.day_start = tk.IntVar(self.master)
        self.day_start.set(0)

        self.day_end = tk.IntVar(self.master)
        self.day_end.set(0)

        self.start_time_label = tk.Label(self.generation_options)
        self.start_time_label['text'] = 'Start Time:'
        self.start_time_label.pack(side='left', pady=self.frame_padding)

        self.start_time_input = tk.OptionMenu(self.generation_options, self.day_start, *hours)
        self.start_time_input.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.end_time_label = tk.Label(self.generation_options)
        self.end_time_label['text'] = 'End Time:'
        self.end_time_label.pack(side='left', pady=self.frame_padding)

        self.end_time_input = tk.OptionMenu(self.generation_options, self.day_end, *hours)
        self.end_time_input.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.generate_button = tk.Button(self.generation_options, padx=self.button_padding, command=self.generate_week_schedule)
        self.generate_button['text'] = 'Generate'
        self.generate_button.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.save_button = tk.Button(self.generation_options, padx=self.button_padding, command=self.save_schedule)
        self.save_button['text'] = 'Save'
        self.save_button.pack(side='left', padx=self.frame_padding, pady=self.frame_padding)

        self.generation_options.pack(side='top')

        self.json_data = self.maybe_load_schedule()

    def generate_week_schedule(self, from_file=False):
        if hasattr(self, 'schedule_grid'):
            self.clear_schedule()

        self.schedule_grid = ScheduleGenerator(self, self.day_start.get(), self.day_end.get(), self.json_data)
        self.schedule_grid.pack()

        if from_file:
            self.schedule_grid.store_data(json_string=self.json_data)

    def edit_schedule(self, event, label_object, day, hour):
        """
        We need to parse the 'event' argument in this function 
        as not doing so will result in issues with the 
        required positional and keyword arguments.

        The click event itself is a hidden positional
        argument on the object's bind() function.

        Args:
            event (ButtonEvent): The registered click event
            label_object (tk.Label): The original clicked tkinter Label
        """
        task = tk.simpledialog.askstring(title='', prompt='Enter Task Name:', initialvalue=label_object['text'])

        label_object['text'] = task

        json = self.schedule_grid.get_data()
        json[day]['data'][str(hour)] = task

        self.schedule_grid.store_data(json)

    def save_schedule(self):
        try:
            data = self.schedule_grid.get_data()

            try:
                with open(self.master.get_working_directory() + self.data_directory, 'w+') as json_file:
                    file_contents = json.dumps(data)
                    json_file.write(file_contents)
                    json_file.close()
            except Exception as ex:
                tk.messagebox.showerror(title='Error Saving Data', message='Unable to save file %s' % json_file.name)
        except AttributeError:
            tk.messagebox.showerror(title='Error Saving Data', message='Grid schedule has not been generated yet.')

    def maybe_load_schedule(self):
        try:
            with open(self.master.get_working_directory() + self.data_directory) as file:
                filename, file_extension = os.path.splitext(file.name)
        except FileNotFoundError:
            tk.messagebox.showwarning(title='Couldn\'t Load Data', message='No valid file found.')
            
            return {}

        if filename:
            filename += file_extension

            try:
                if '.json' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename) as file:
                    self.json_data = json.load(file)

                    self.day_start.set(self.json_data['start'])
                    self.day_end.set(self.json_data['end'])

                    self.generate_week_schedule(from_file=True)
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Data', message='Unable to open file %s' % filename)

    def clear_schedule(self):
        self.schedule_grid.destroy()