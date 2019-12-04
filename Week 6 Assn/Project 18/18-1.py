from tkinter import *
import math


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Right Triangle Calculator")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side=BOTTOM)

        self.calculate_button = Button(master, text="Calculate", command=self.calculate)
        self.calculate_button.pack(side=BOTTOM)

        self.a_side_label = Label(master, text='Side A')
        self.a_side_label.pack()
        self.side_a = Entry(master)
        self.side_a.pack()

        self.b_side_label = Label(master, text='Side B')
        self.b_side_label.pack()
        self.side_b = Entry(master)
        self.side_b.pack()

        self.c_side_label = Label(master, text='Side C')
        self.c_side_label.pack()
        self.c_frame = Message(master, highlightbackground="black", highlightcolor="black", highlightthickness=1,
                               width=100)
        self.c_frame.pack()



    def greet(self):
        print("Greetings!")

    def calculate(self):
        try:
            a = int(self.side_a.get())
            b = int(self.side_b.get())

            remainder = round(math.sqrt(a ** 2 + b ** 2), 3)
            self.c_frame.config(text=remainder)
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
