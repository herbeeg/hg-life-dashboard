import tkinter as tk

class GoalFrame(tk.Frame):
    """
    Represents a goal data container in a 
    single column within the application.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None, name=''):
        """
        Assign the frame name. For example:

        'goal_1_frame'

        Args:
            master (Tk, optional): The parent tkinter frame element. Defaults to None.
            name (str, optional): Name of the frame element. Defaults to ''.
        """
        super().__init__(master)
        self.master = master

        self.name = name

    def getName(self):
        """
        As Python doesn't have an easy way of converting
        a variable's name to a string: 

        (e.g. self.foo => 'foo')

        ...we extend the tkinter Frame class and
        assign a class variable that we can
        call when we search the local
        JSON data for key=>values.

        Returns:
            str: The name of the frame
        """
        return self.name