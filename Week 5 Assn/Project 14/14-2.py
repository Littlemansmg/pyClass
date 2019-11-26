# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import random


class Deck:
    def __init__(self, full_deck):
        self.full_deck = full_deck

    def shuffle(self):
        random.shuffle(self.full_deck)
        print("I have shuffled a deck of 52 cards.")

    def deal(self):
        cards = 0
        while True:
            try:
                cards = int(input("How many cards would you like?: "))
                if 52 < cards <= 0:
                    raise ValueError
            except ValueError:
                print('You must input a number between 1 and 52')
                continue
            break
        print("Here are your cards:")
        for i in range(cards):
            print(self.full_deck[i])
        print(f"\nThere are {self.deck_len(cards)} left in the deck.\n"
              f"Good luck!")

    def deck_len(self, cards):
        return len(self.full_deck) - cards




class Card:
    def __init__(self):
        self.rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']


def main():
    card = Card()
    deck = []
    for suit in card.suit:
        for rank in card.rank:
            deck.append(f"{rank} of {suit}")

    deck_of_52 = Deck(deck)
    deck_of_52.shuffle()
    deck_of_52.deal()


if __name__ == "__main__":
    main()
