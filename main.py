import tkinter as tk
import tkinter.ttk as ttk

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

if '__main__' == __name__:
    root = tk.Tk()
    app = MainApp(master=root)
    app.mainloop()