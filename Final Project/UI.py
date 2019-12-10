# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import Classes
from game_logic import point_calc
from tkinter import *
import DB
import locale
locale.setlocale(locale.LC_ALL, '')


class BlackJackGUI:
    def __init__(self, master):
        self.master = master
        master.title("Blackjack")

        # Money
        self.money_label = Label(master, text="Money:")
        self.money_label.grid(row=0, column=0, padx=7, pady=2, sticky='e')
        self.money_box = Label(master, highlightbackground="black", highlightcolor="black",
                               relief='solid', width=17, anchor='w')
        self.money_box.grid(row=0, column=1, padx=12, pady=5, sticky='w')

        # Bet
        self.bet_label = Label(master, text="Bet:")
        self.bet_label.grid(row=1, column=0, padx=7, pady=2, sticky='e')
        self.bet_entry = Entry(master)
        self.bet_entry.grid(row=1, column=1, padx=12, sticky='w')

        # REGION DEALER
        self.dealer_name = Label(master, text="DEALER")
        self.dealer_name.grid(row=2, column=0, pady=2)

        self.dealer_cards = Label(master, text="Cards:")
        self.dealer_cards.grid(row=3, column=0, pady=4)
        self.dealer_card_box = Label(master, anchor='w', highlightbackground="black",
                                     highlightcolor="black", relief='solid', width=34,)
        self.dealer_card_box.grid(row=3, column=1, padx=12, sticky='w')

        self.dealer_points = Label(master, text="Points:", anchor='w')
        self.dealer_points.grid(row=4, column=0, pady=4)
        self.dealer_points_box = Label(master, highlightbackground="black",
                                       highlightcolor="black", relief='solid', width=17)
        self.dealer_points_box.grid(row=4, column=1, padx=12, sticky='w')
        # END REGION DEALER

        # REGION Player
        self.player_name = Label(master, text="YOU")
        self.player_name.grid(row=5, column=0, pady=2)

        self.player_cards = Label(master, text="Cards:")
        self.player_cards.grid(row=6, column=0, pady=4)
        self.player_card_box = Label(master, highlightbackground="black", anchor='w',
                                     highlightcolor="black", relief='solid', width=34, )
        self.player_card_box.grid(row=6, column=1, padx=12, sticky='w')

        self.player_points = Label(master, text="Points:")
        self.player_points.grid(row=7, column=0, pady=4)
        self.player_points_box = Label(master, highlightbackground="black", anchor='w',
                                       highlightcolor="black", relief='solid', width=17)
        self.player_points_box.grid(row=7, column=1, padx=12, pady=5, sticky='w')
        # END REGION Player

        # Play options
        self.hit = Button(master, text="Hit")
        self.hit.grid(row=8, column=1, pady=4, sticky='w')

        self.stand = Button(master, text="Stand")
        self.stand.grid(row=8, pady=4, column=1)

        # Results
        self.results = Label(master, text="RESULT:")
        self.results.grid(row=9, column=0, pady=4)
        self.result_box = Label(master, highlightbackground="black", anchor='w',
                                highlightcolor="black", relief='solid', width=34, )
        self.result_box.grid(row=9, column=1, padx=12, sticky='n')

        # Again/Exit buttons
        self.play = Button(master, text="Play")
        self.play.grid(row=10, column=1, pady=4, sticky='w')

        self.exit = Button(master, text="Exit", command=master.quit)
        self.exit.grid(row=10, pady=4, column=1)

    def load_values(self, cursor, deck):
        money = DB.get_money(cursor)
        hands = Classes.Hand(deck)
        self.money_box.config(text=locale.currency(float(money), grouping=True))
        self.dealer_card_box.config(text=' '.join(hands.get_dealer()))
        self.dealer_points_box.config(text=hands.get_dealer_points())
        self.player_card_box.config(text=' '.join(hands.get_player()))
        self.player_points_box.config(text=hands.get_player_points())

def center_gui(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry(f'+{positionRight}+{positionDown}')


def display_hand(hand):
    pass


def get_points(hand):
    pass


def winner(user_hand, dealer_hand):
    u_points = point_calc(user_hand[1:])
    d_points = point_calc(dealer_hand[1:])
    print(f'Your Points: {u_points}\n'
          f'Dealers Points: {d_points}\n')
    if u_points > d_points:
        print("You win!")
        return True
    elif u_points < d_points:
        print("Dealer wins!")
        return True
    else:
        print("Draw!")
        return True
