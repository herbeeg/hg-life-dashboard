import tkinter as tk
import os

import main.main_menu as main
import journal.journal as journal
import xeffect.x_effect as xeffect

from functools import partial

class MainApp(tk.Frame):
    """
    Main container to provide a canvas for all 
    application elements.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Initialise parent window populated with 
        main menu elements and packs them
        for rendering onto the window.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.window_title = 'Life Dashboard'

        self.main.pack()
        self.pack()

    def load_view(self, view = 'menu'):
        """
        Switches out the container view based on
        what element of the application we 
        want to load.

        Args:
            view (str, optional): Container codename to load. Defaults to 'menu'.
        """
        self.clear_view()

        if 'menu' == view:
            self.master.title('Menu - ' + self.window_title)

            self.main = main.MainMenu(self)
            self.main.pack()
            self.detach_back_button()
        elif 'budget' == view:
            self.master.title('Budget - ' + self.window_title)

            self.budget = ''
        elif 'xeffect' == view:
            self.master.title('X-Effect - ' + self.window_title)
            
            self.xeffect = xeffect.XEffect(self)
            self.xeffect.pack()
            self.attach_back_button()
        elif 'goals' == view:
            self.master.title('Goal Setting - ' + self.window_title)

            self.goals = ''
        elif 'schedule' == view:
            self.master.title('Schedule - ' + self.window_title)

            self.schedule = ''
        elif 'journal' == view:
            self.master.title('Journal - ' + self.window_title)

            self.journal = journal.Journal(self)
            self.journal.pack()
            self.attach_back_button()

    def clear_view(self):
        """
        Destroy all elements in the current frame
        so that we can prepare the element to
        have a new frame loaded and packed.
        """
        for widget in self.winfo_children():
            widget.destroy()

    def attach_back_button(self):
        """
        Create a new, absolutely positioned back button
        element to the root frame and anchor it to
        the top-left of the window.
        """
        self.menu_back = tk.Button(self.master, padx=10, pady=5, command=partial(self.load_view, 'menu'))
        self.menu_back['text'] = '<-- Back'
        self.menu_back.pack()
        self.menu_back.place(anchor='nw', x=10)

    def detach_back_button(self):
        """
        As the back button is attached to the root
        frame, the element will be destroyed
        and re-created when necessary.
        """
        if hasattr(self, 'menu_back') and None != self.menu_back:
            self.menu_back.destroy()

    def get_working_directory(self):
        return os.getcwd()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('Menu - Life Dashboard')
    root.geometry('1280x720')
    root.resizable(width=False, height=False)

    app = MainApp(master=root)
    app.mainloop()