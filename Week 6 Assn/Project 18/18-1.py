from tkinter import *
import math


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Right Triangle Calculator")

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=10, column=10)

        self.calculate_button = Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.grid(row=10, column=4)

        self.a_side_label = Label(master, text='Side A')
        self.a_side_label.grid(row=3, column=3)
        self.side_a = Entry(master)
        self.side_a.grid(row=3, column=4)

        self.b_side_label = Label(master, text='Side B')
        self.b_side_label.grid(row=4, column=3)
        self.side_b = Entry(master)
        self.side_b.grid(row=4, column=4)

        self.c_side_label = Label(master, text='Side C')
        self.c_side_label.grid(row=5, column=3)
        self.c_frame = Label(master, highlightbackground="black", highlightcolor="black", highlightthickness=1,
                             state='disabled')
        self.c_frame.grid(row=5, column=4)

    def greet(self):
        print("Greetings!")

    def calculate(self):
        try:
            a = int(self.side_a.get())
            b = int(self.side_b.get())

            remainder = round(math.sqrt(a ** 2 + b ** 2), 3)
            self.c_frame.config(text=remainder, state='active')
        except ValueError:
            print("Can't get an empty")


def center_gui(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry(f'+{positionRight}+{positionDown}')


if __name__ == "__main__":
    root = Tk()
    center_gui(root)
    my_gui = MyFirstGUI(root)
    root.mainloop()
