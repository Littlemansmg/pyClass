from tkinter import *

class GUI:
    def __init__(self, master, name, language, time):
        self.name = name
        self.language = language
        self.time = time
        self.master = master

        self.name_label = Label(master, text='Name:')
        self.name_label.grid(row=1, column=1)
        self.name_entry = Entry(master)
        self.name_entry.insert(0, self.name)
        self.name_entry.grid(row=1, column=2, columnspan=2)

        self.required = Label(master, text='Required.', show='disabled')

        self.language_label = Label(master, text='Language:')
        self.language_label.grid(row=2, column=1)
        self.language_entry = Entry(master)
        self.language_entry.insert(0, self.language)
        self.language_entry.grid(row=2, column=2, columnspan=2)

        self.name_label = Label(master, text='Auto save every x minutes:')
        self.name_label.grid(row=3, column=1)
        self.name_entry = Entry(master)
        self.name_entry.insert(0, self.time)
        self.name_entry.grid(row=3, column=2, columnspan=2)

        self.save_button = Button(master, text="Save")
        self.save_button.grid(row=4, column=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=3)


def center_gui(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry(f'+{positionRight}+{positionDown}')

if __name__ == '__main__':
    options = []
    with open('./preferences.txt', "r") as file:
        for line in file:
            options = line.split(sep=',')

    root = Tk()
    center_gui(root)
    mygui = GUI(root, options[0], options[1], options[2])
    root.mainloop()
