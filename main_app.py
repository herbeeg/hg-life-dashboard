import tkinter as tk

import main.main_menu as main
import journal.journal as journal

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
        elif 'budget' == view:
            self.master.title('Budget - ' + self.window_title)

            self.budget = ''
        elif 'xeffect' == view:
            self.master.title('X-Effect - ' + self.window_title)
            
            self.xeffect = ''
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

    def clear_view(self):
        """
        Destroy all elements in the current frame
        so that we can prepare the element to
        have a new frame loaded and packed.
        """
        for widget in self.winfo_children():
            widget.destroy()

if '__main__' == __name__:
    """Setup root tkinter window."""
    root = tk.Tk()
    root.title('Menu - Life Dashboard')
    root.geometry('1280x720')
    root.resizable(width=False, height=False)

    app = MainApp(master=root)
    app.mainloop()