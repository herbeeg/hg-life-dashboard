import tkinter as tk

import main.main_menu as main

class MainApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.main = main.MainMenu(self)

        self.main.pack()
        self.pack()

    def load_view(self, view = 'menu'):
        self.clear_view()

        if 'menu' == view:
            self.main = main.MainMenu(self)
            self.main.pack()
        elif 'budget' == view:
            self.budget = ''
        elif 'xeffect' == view:
            self.xeffect = ''
        elif 'goals' == view:
            self.goals = ''
        elif 'schedule' == view:
            self.schedule = ''
        elif 'journal' == view:
            self.journal = ''


    def clear_view(self):
        for widget in self.winfo_children():
            widget.destroy()

if '__main__' == __name__:
    root = tk.Tk()
    root.title('Life Dashboard')
    root.geometry('1280x720')
    root.resizable(width=False, height=False)

    app = MainApp(master=root)
    app.mainloop()