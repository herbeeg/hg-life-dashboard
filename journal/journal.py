import tkinter.filedialog
import tkinter.messagebox
import tkinter as tk
import os

class Journal(tk.Frame):
    """
    Builds all of the journal frame elements and
    contains logic for text file manipulation
    when dealing with journal entries.

    Extends the tkinter Frame class.
    """
    def __init__(self, master=None):
        """
        Set GUI element padding values and animation
        settings for the status frame.

        Args:
            master (Tk, optional): The parent tkinter window element. Defaults to None.
        """
        super().__init__(master)
        self.master = master

        self.frame_padding = 5
        self.button_padding = 50
        self.animation_delay = 1500

        self.create_widgets()

    def create_widgets(self):
        """
        Render all journal widget elements and map 
        all input commands to their respective 
        filedialog functions.

        The status label doesn't get packed as we
        don't want to render that on the screen
        until we've had a file operation.
        """
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
        """
        Generate a filedialog window when the 'Edit'
        button is clicked and attempt to read
        any text files that are selected.

        Uses the 'r+' mode so that respective files
        are opened for reading and writing.

        Raises:
            TypeError: Fail if the file extension is not a valid text file
        """
        filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Edit Journal', filetypes=[('Text Files', '*.txt')]))

        if filename:
            filename += file_extension

            try:
                if '.txt' != file_extension:
                    raise TypeError('Invalid file extension %s' % file_extension)

                with open(filename, 'r+') as file:
                    contents = file.read()
                    self.refresh_text_input(contents)

                    self.update_status('File Loaded!')
            except Exception as ex:
                tk.messagebox.showerror(title='Error Loading Journal', message='Unable to open file %s' % filename)

    def save_file(self):
        """
        Generate a filedialog window when the 'Save'
        button is clicked and allow the user to
        specify a filename and location.

        Uses the 'w+' mode so that respective files
        are cleared before writing takes place.
        """
        filename = tk.filedialog.asksaveasfilename(title='Save Journal', filetypes=[('Text Files', '*.txt')])

        if filename:
            try:
                with open(filename, 'w+') as text_file:
                    file_contents = self.get_contents()
                    text_file.write(file_contents)
                    text_file.close()

                    self.update_status('File Saved!')
            except Exception as ex:
                tk.messagebox.showerror(title='Error Saving Journal', message='Unable to save file %s' % filename)
            

    def delete_file(self):
        """
        Uses the pre-existing askopenfilename() function
        to generate a window where the user can choose
        a file to delete by 'opening'.

        Users are required to confirm that they want
        to delete the chosen file again before
        the application can proceed.

        Raises:
            TypeError: Fail if the file extension is not a valid text file
            IOError: Fail if the file does not exist
        """
        filename, file_extension = os.path.splitext(tk.filedialog.askopenfilename(title='Delete Journal', filetypes=[('Text Files', '*.txt')]))

        if filename:
            confirm_choice = tk.messagebox.askyesno(title='Confirm Journal Deletion', message='Are you sure you want to delete this journal?')

            if True == confirm_choice:
                filename += file_extension

                try:
                    if '.txt' != file_extension:
                        raise TypeError('Invalid file extension %s' % file_extension)

                    if os.path.exists(filename):
                        os.remove(filename)

                        self.update_status('File Deleted!')
                    else:
                        raise IOError('Selected file does not exist.')
                except Exception as ex:
                    tk.messagebox.showerror(title='Error Deleting Journal', message='Could not delete file %s' % filename)

    def get_contents(self):
        """
        Gets the entirity of data from the text file
        by specifying '1.0' as the starting point.

        Avoids any trailing newline characters by
        specifying 'end-1c', meaning up to the
        last but one character.

        Returns:
            str: The contents of the text file
        """
        return self.journal_input.get(1.0, 'end-1c')

    def refresh_text_input(self, content):
        """
        Completely clear the text input area before
        text file contents are loaded for avoid
        any concatenation.

        Args:
            content (str): The text file contents
        """
        self.journal_input.delete(1.0, 'end-1c')
        self.journal_input.insert(1.0, content)

    def update_status(self, text):
        """
        Change the relevant text on the label
        element and un-hide it by packing
        it once again.

        Args:
            text (str): Text to be printed on the label
        """
        self.journal_status['text'] = text
        self.after(self.animation_delay, self.animate_status)
        self.journal_status.pack(side='left', fill='x', expand=True, padx=self.frame_padding, pady=self.frame_padding)

    def animate_status(self):
        """
        Recursive function that removes the last
        character from the label string each
        time it's called until none are left.

        After the initial wait period passes, a
        shorter time period is used to give
        the feeling of an animation.
        """
        current_text = self.journal_status['text']

        if 0 < len(current_text):
            self.journal_status['text'] = current_text[:-1]
            self.after(20, self.animate_status)
        else:
            self.journal_status.forget()
