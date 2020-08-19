import tkinter.filedialog
import tkinter.messagebox
import tkinter as tk
import os

class Journal(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.frame_padding = 5
        self.button_padding = 50
        self.animation_delay = 1500

        self.create_widgets()

    def create_widgets(self):
        self.journal_input = tk.Text(self, height=20, borderwidth=50)
        self.journal_input.pack(side='top', fill='both')

        self.journal_delete = tk.Button(self, padx=self.button_padding, command=self.delete_file)
        self.journal_delete['text'] = 'Delete'
        self.journal_delete.pack(side='right', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.journal_edit = tk.Button(self, padx=self.button_padding, command=self.pick_file)
        self.journal_edit['text'] = 'Edit'
        self.journal_edit.pack(side='right', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.journal_save = tk.Button(self, padx=self.button_padding, command=self.save_file)
        self.journal_save['text'] = 'Save'
        self.journal_save.pack(side='right', fill='x', padx=self.frame_padding, pady=self.frame_padding)

        self.journal_status = tk.Label(self, bg='#c9f6c9')
        self.journal_status['text'] = ''
        

    def pick_file(self):
        filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Edit Journal', filetypes=[('Text Files', '*.txt')]))

        if filename:
            filename += file_extension

            try:
                if '.txt' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename, 'r+') as file:
                    contents = file.read()
                    self.refresh_text_input(contents)
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Journal', message='Unable to open file %s' % filename)

    def save_file(self):
        filename = tk.filedialog.asksaveasfilename(title='Save Journal', filetypes=[('Text Files', '*.txt')])

        if filename:
            text_file = open(filename, 'w+')
            file_contents = self.get_contents()
            text_file.write(file_contents)
            text_file.close()

            self.update_status('File Saved!')

    def delete_file(self):
        filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Delete Journal', filetypes=[('Text Files', '*.txt')]))

        if filename:
            filename += file_extension

            try:
                if '.txt' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                if os.path.exists(filename):
                    os.remove(filename)
                else:
                    raise IOError('Selected file does not exist.')
            except Exception as ex:
                tk.messagebox.showerror(title='Error Deleting Journal', message='Could not delete file %s' % filename)

    def get_contents(self):
        return self.journal_input.get(1.0, 'end-1c')

    def refresh_text_input(self, content):
        self.journal_input.delete(1.0, 'end-1c')
        self.journal_input.insert(1.0, content)

    def update_status(self, text):
        self.journal_status['text'] = text
        self.after(self.animation_delay, self.animate_status)
        self.journal_status.pack(side='left', fill='x', expand=True, padx=self.frame_padding, pady=self.frame_padding)

    def animate_status(self):
        current_text = self.journal_status['text']

        if 0 < len(current_text):
            self.journal_status['text'] = current_text[:-1]
            self.after(20, self.animate_status)
        else:
            self.journal_status.forget()
