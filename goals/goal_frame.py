import tkinter as tk

class GoalFrame(tk.Frame):
    def __init__(self, master=None, name=''):
        super().__init__(master)
        self.master = master

        self.name = name

    def getName(self):
        return self.name