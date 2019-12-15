
import Classes
import UI
import DB
from tkinter import Tk
from datetime import datetime


if __name__ == "__main__":
    connect = DB.connect("blackjack")
    deck = Classes.Deck()
    hands = Classes.Hand(deck)
    logic = Classes.Logic()

    cursor = connect.cursor()
    startmoney = float(DB.get_money(cursor))

    root = Tk()
    UI.center_gui(root)
    my_gui = UI.BlackJackGUI(root, logic, deck, hands, cursor, connect)
    UI.BlackJackGUI.load_values(my_gui)
    root.mainloop()
    endmoney = float(my_gui.money)
    if endmoney >= startmoney:
        added = endmoney - startmoney
    else:
        added = 0
    DB.session_end(connect, cursor, datetime.now(), startmoney, added, endmoney)
