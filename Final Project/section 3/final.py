
import Classes
import UI
import DB
from datetime import datetime
import os


def main(money):
    while True:
        UI.intro(now)
        bet = UI.get_bet(money)
        UI.show_cards(hands, True)
        while True:
            option = UI.option()
            if option == 'hit':
                result, money = logic.hit(deck, hands, money, bet)
                if result:
                    end = logic.replay(hands, result, money)
                    if not end:
                        break
            elif option == 'stand':
                result, money = logic.stand(deck, hands, money, bet)
                if result:
                    end = logic.replay(hands, result, money)
                    if not end:
                        break
            UI.show_cards(hands, False)
        clear()


if __name__ == "__main__":
    deck = Classes.Deck()
    hands = Classes.Hand(deck)
    logic = Classes.Logic()
    money = DB.get_money()
    clear = lambda: os.system('cls')  # on Windows System
    now = datetime.now().strftime("%I:%M.%S %p")
    main(money)

