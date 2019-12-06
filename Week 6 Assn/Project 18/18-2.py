from tkinter import *

class GUI:
    def __init__(self, master, name, language, time):
        # get preferences from file
        self.name = name
        self.language = language
        self.time = time
        self.master = master
        master.title('Auto Save')

        # name entry
        self.name_label = Label(master, text='Name:')
        self.name_label.grid(row=1, column=1)
        self.name_entry = Entry(master)
        self.name_entry.insert(0, self.name)
        self.name_entry.grid(row=1, column=2, columnspan=2)

        # Language entry
        self.language_label = Label(master, text='Language:')
        self.language_label.grid(row=2, column=1)
        self.language_entry = Entry(master)
        self.language_entry.insert(0, self.language)
        self.language_entry.grid(row=2, column=2, columnspan=2)

        # Auto save entry
        self.auto_label = Label(master, text='Auto save every x minutes:')
        self.auto_label.grid(row=3, column=1)
        self.auto_entry = Entry(master)
        self.auto_entry.insert(0, self.time)
        self.auto_entry.grid(row=3, column=2, columnspan=2)

        # Save button
        self.save_button = Button(master, text="Save", command=self.save)
        self.save_button.grid(row=4, column=2)

        # Close button
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=3)

        # Error Labels
        self.name_required = Label(master)
        self.language_required = Label(master)
        self.int_save = Label(master)

    def save(self):
        name = self.name_entry.get()
        language = self.language_entry.get()
        auto = self.auto_entry.get()
        try:
            if name == '' and auto == '':
                self.name_required.config(text='Required.')
                self.int_save.config(text='Please type a valid int')
                self.name_required.grid(row=1, column=4)
                self.int_save.grid(row=3, column=4)

            if name == '':
                self.name_required.config(text='Required.')
                self.name_required.grid(row=1, column=4)

            if language == '':
                self.language_required.config(text='Required.')
                self.name_required.grid(row=2, column=4)
            int(auto)
        except ValueError:
            self.int_save.config(text='Please type a valid int')
            self.int_save.grid(row=3, column=4)
            return

        if name != '':
            self.name_required.grid_forget()
        if auto != '':
            self.int_save.grid_forget()

        with open('./preferences.txt', "w") as file:
            file.write(f"{name},{language},{auto}")

def center_gui(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry(f'+{positionRight}+{positionDown}')


if __name__ == '__main__':
    options = []

    with open('./preferences.txt', 'r') as file:
        for line in file:
            options = line.split(sep=',')
    if options == []:
        options = ["Name here", "English", "x"]
        with open('./preferences.txt', 'w') as file:
            file.write(f"{options[0]}, {options[1]}, {options[2]}")

    root = Tk()
    center_gui(root)
    mygui = GUI(root, options[0], options[1], options[2])
    root.mainloop()
