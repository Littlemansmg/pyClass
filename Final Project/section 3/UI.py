# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import Classes
import DB
import locale
locale.setlocale(locale.LC_ALL, '')


def intro(now):
    print(f"BLACKJACK!\n"
          f"Blackjack payout is 3:2\n"
          f"Start time: {now}\n")


def get_bet(money):
    print(f"Money: {money}")
    bet = 0
    while True:
        try:
            bet = (float(input("Bet: ")))
            if bet < 5:
                raise Exception
            if bet > 1000:
                raise Exception
            if bet >= money:
                # IDK how to make my own exceptions, so here is a random one.
                raise NotADirectoryError
        except (ValueError, Exception, NotADirectoryError) as e:
            if isinstance(e, ValueError):
                print("Please type a number.")
            elif isinstance(e, NotADirectoryError):
                print("You can't bet more than you have.")
            elif isinstance(e, Exception):
                print("Please type a number between 5 and 1000.")
            continue
        return bet


def show_cards(hands, intro):
    dealer = hands.get_dealer()
    player = hands.get_player()
    if intro:
        print(f"DEALERS'S SHOW CARD:\n"
              f"{dealer[0]}\n\n"
              f"YOUR CARDS:")
        for card in player:
            print(card)
    elif not intro:
        print(f"YOUR CARDS:")
        for card in player:
            print(card)
        print()


def option():
    while True:
        try:
            option = input("Hit or stand? (hit/stand): ").lower()
            if not option.startswith('h') and not option.startswith('s'):
                raise ValueError
        except ValueError:
            print("Please type hit or stand.")
            continue
        break
    return option

