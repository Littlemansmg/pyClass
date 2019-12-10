# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

from random import shuffle, randint, choice


class Deck:
    def __init__(self):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        self.deck = []

        # Create deck of 52
        for card in cards:
            for suit in suits:
                try:
                    int(card)
                    self.deck.append(Card(card, suit, card))
                except ValueError:
                    if card != 'Ace':
                        points = 10
                        self.deck.append(Card(card, suit, points))
                    else:
                        points = (1, 10)
                        self.deck.append(Card(card, suit, points))

    # shuffle deck and apply to self
    def deck_shuffle(self, deck):
        shuffle(deck)
        self.deck = deck

    def deal_card(self):
        i = choice(range(len(self.deck)))
        card = self.deck[i]
        self.deck.pop(i)
        return card


class Card:
    def __init__(self, number, suit, points):
        self.number = number
        self.suit = suit
        self.points = points

    def __str__(self):
        return f"{self.number}|{self.suit[0]}"


class Hand:
    def __init__(self, deck):
        self.dealer = []
        self.player = []
        for i in range(2):
            self.dealer.append(deck.deal_card())
            self.player.append(deck.deal_card())

    def get_dealer(self):
        string = ''
        for card in self.dealer:
            string += str(card) + ' '
        return string

    def get_dealer_points(self):
        points = 0
        for card in self.dealer:
            if type(card.points) is tuple:
                points += card.points[1]
            else:
                points += card.points
            if points > 21 and card.number == 'Ace':
                points -= 10
        return points

    def get_player(self):
        string = ''
        for card in self.player:
            string += str(card) + ' '
        return string

    def get_player_points(self):
        points = 0
        for card in self.player:
            if type(card.points) is tuple:
                points += card.points[1]
            else:
                points += card.points
            if points > 21 and card.number == 'Ace':
                points -= 10
        return points


class Logic:
    def hit(self, hand):
        while True:
            new_card = randint(0, 51)
            if self.deck[new_card] not in hand:
                hand.append(self.deck[new_card])
                break
            else:
                continue
        return hand