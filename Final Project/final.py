
import Classes
import UI
import DB
from tkinter import Tk


def main():
    pass


if __name__ == "__main__":
    connect = DB.connect("blackjack")
    deck = Classes.Deck()
    cursor = connect.cursor()

    root = Tk()
    UI.center_gui(root)
    my_gui = UI.BlackJackGUI(root)
    UI.BlackJackGUI.load_values(my_gui, cursor, deck)
    root.mainloop()
