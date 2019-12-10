
from game_logic import *
from UI import *


def main():
    while True:
        user_hand, dealer_hand = deck.get_hands()
        display_hand(dealer_hand)
        display_hand(user_hand)
        get_points(user_hand[1:])

        if check_blackjack(user_hand[1:]):
            end()
            continue

        if check_blackjack(dealer_hand[1:]):
            end()
            continue

        while True:
            option = ask_hit()
            if option == 'hit':
                user_hand = deck.hit(user_hand)
                display_hand(user_hand)
                get_points(user_hand[1:])

            if check_bust(user_hand, point_calc(user_hand[1:])):
                end()
                break

            while point_calc(dealer_hand[1:]) < 17:
                dealer_hand = deck.hit(dealer_hand)

            if check_bust(dealer_hand, point_calc(dealer_hand[1:])):
                end()
                break

            if option == 'stand':
                dealer_hand[0] = 's'
                display_hand(dealer_hand)
                winner(user_hand, dealer_hand)
                end()
                break


if __name__ == "__main__":
    deck = Deck()
    print("Blackjack\n")
    main()
