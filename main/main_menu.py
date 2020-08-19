import tkinter as tk

from functools import partial

class MainMenu(tk.Frame):
    """
    Builds all of the main menu elements in
    the application which can be used by
    the parent window for rendering.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Set GUI element padding for re-use when
        generating the widget area.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

        self.frame_padding = 10
        self.button_padding = 50

        self.create_widgets()

    def create_widgets(self):
        """
        Render all menu button elements and map their
        commands to the main application's view
        loader function.

        Makes use of the functools.partial library
        to allow passing of parameters to button
        command configs.
        """
        self.budgets_open = tk.Button(self, padx=self.button_padding, command=partial(self.master.load_view, 'budget'))
        self.budgets_open['text'] = 'Budget'
        self.budgets_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.xeffect_open = tk.Button(self, padx=self.button_padding, command=partial(self.master.load_view, 'xeffect'))
        self.xeffect_open['text'] = 'X-Effect'
        self.xeffect_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.goals_open = tk.Button(self, padx=self.button_padding, command=partial(self.master.load_view, 'goals'))
        self.goals_open['text'] = 'Goal Setting'
        self.goals_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.schedules_open = tk.Button(self, padx=self.button_padding, command=partial(self.master.load_view, 'schedule'))
        self.schedules_open['text'] = 'Schedule'
        self.schedules_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.journal_open = tk.Button(self, padx=self.button_padding, command=partial(self.master.load_view, 'journal'))
        self.journal_open['text'] = 'Journal'
        self.journal_open.pack(side='top', fill='x', padx=self.frame_padding, pady=self.frame_padding)