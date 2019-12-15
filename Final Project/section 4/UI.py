# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import Classes
from tkinter import *
import DB
import locale
locale.setlocale(locale.LC_ALL, '')


class BlackJackGUI:
    def __init__(self, master, logic, deck, hands, cursor, connect):
        self.deck = deck
        self.logic = logic
        self.hands = hands
        self.cursor = cursor
        self.connect = connect
        self.master = master
        self.money = DB.get_money(self.cursor)
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
                                     highlightcolor="black", relief='solid', width=34)
        self.dealer_card_box.grid(row=3, column=1, padx=12, sticky='w')

        self.dealer_points = Label(master, text="Points:", anchor='w')
        self.dealer_points.grid(row=4, column=0, pady=4)
        self.dealer_points_box = Label(master, highlightbackground="black",
                                       highlightcolor="black", relief='solid', width=17,
                                       anchor='w')
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
        self.hit = Button(master, text="Hit", command=self.hit_funk)
        self.hit.grid(row=8, column=1, pady=4, sticky='w')

        self.stand = Button(master, text="Stand", command=self.stand_funk)
        self.stand.grid(row=8, pady=4, column=1)

        # Results
        self.results = Label(master, text="RESULT:")
        self.results.grid(row=9, column=0, pady=4)
        self.result_box = Label(master, highlightbackground="black", anchor='w',
                                highlightcolor="black", relief='solid', width=34, )
        self.result_box.grid(row=9, column=1, padx=12, sticky='n')

        # Again/Exit buttons
        self.play = Button(master, text="Play", command=self.replay)
        self.play.grid(row=10, column=1, pady=4, sticky='w')

        self.exit = Button(master, text="Exit", command=master.quit)
        self.exit.grid(row=10, pady=4, column=1)

    def hit_funk(self):
        result = ''
        try:
            bet = float(self.bet_entry.get())
        except ValueError:
            self.result_box.config(text="You must bet 5 or more.")
            return
        if bet == '' or bet < 5:
            self.result_box.config(text="You must bet 5 or more.")
            return
        elif bet > 1000:
            self.result_box.config(text="You must bet 1000 or less")
            return
        elif bet > float(self.money):
            self.result_box.config(text="You can't bet more than you have.")
            return
        result, self.money = self.logic.hit(self.deck, self.hands, float(self.money),
                                            bet)
        self.dealer_card_box.config(text=' '.join(self.hands.print_dealer()))
        self.dealer_points_box.config(text=self.hands.print_dealer_points())
        self.player_card_box.config(text=' '.join(self.hands.print_player()))
        self.player_points_box.config(text=self.hands.print_player_points())
        if result:
            self.result_box.config(text=result)
            self.money_box.config(text=self.money)
            self.bet_entry.config(state='disabled')
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')

    def stand_funk(self):
        result = ''
        bet = float(self.bet_entry.get())
        if bet == '' or bet < 5:
            self.result_box.config(text="You must bet 5 or more.")
            return
        elif bet > 1000:
            self.result_box.config(text="You must bet 1000 or less")
            return
        elif bet > float(self.money):
            self.result_box.config(text="You can't bet more than you have.")
            return
        result, self.money = self.logic.stand(self.deck, self.hands, float(self.money),
                                              float(self.bet_entry.get()))
        self.bet_entry.config(state='disabled')
        self.hit.config(state='disabled')
        self.stand.config(state='disabled')
        self.dealer_card_box.config(text=' '.join(self.hands.print_dealer()))
        self.dealer_points_box.config(text=self.hands.print_dealer_points())
        self.player_card_box.config(text=' '.join(self.hands.print_player()))
        self.player_points_box.config(text=self.hands.print_player_points())
        if result:
            self.result_box.config(text=result)
            self.money_box.config(text=self.money)
            self.bet_entry.config(state='disabled')
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')
            self.result_box.config(text=result)

    def replay(self):
        self.deck = Classes.Deck()
        self.logic = Classes.Logic()
        self.hands = Classes.Hand(self.deck)
        self.load_values()
        self.money_box.config(text=self.money)
        self.result_box.config(text='')
        self.bet_entry.config(state='normal')
        self.hit.config(state='active')
        self.stand.config(state='active')

    def load_values(self):
        self.money_box.config(text=locale.currency(float(self.money), grouping=True))
        self.dealer_card_box.config(text=' '.join(self.hands.print_dealer()))
        self.dealer_points_box.config(text=self.hands.print_dealer_points())
        self.player_card_box.config(text=' '.join(self.hands.print_player()))
        self.player_points_box.config(text=self.hands.print_player_points())
        self.check_blackjack()

    def check_blackjack(self):
        if self.hands.print_dealer_points() == 21:
            self.result_box.config(text="BLACKJACK! Dealer wins!")
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')
        if self.hands.print_player_points() == 21:
            self.result_box.config(text="BLACKJACK! You win!")
            self.hit.config(state='disabled')
            self.stand.config(state='disabled')


def center_gui(root):
    windowWidth = root.winfo_reqwidth()
    windowHeight = root.winfo_reqheight()
    positionRight = int(root.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(root.winfo_screenheight() / 2 - windowHeight / 2)
    root.geometry(f'+{positionRight}+{positionDown}')

