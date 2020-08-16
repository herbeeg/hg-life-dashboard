import tkinter as tk
import tkinter.ttk as ttk

import main.main_menu as main

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.main.pack()
        self.pack()

if '__main__' == __name__:
    root = tk.Tk()
    root.title('Life Dashboard')
    root.geometry('1280x720')
    root.resizable(width=False, height=False)

    app = MainApp(master=root)
    app.mainloop()