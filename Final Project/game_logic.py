# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

from random import shuffle, randint

class Deck:
    def __init__(self):
        cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
        suits = ['Spades', 'Diamonds', 'Clubs', 'Hearts']
        deck = []

        # Create deck of 52
        for card in cards:
            for suit in suits:
                string = f'{card} of {suit}'
                deck.append(string)

        # shuffle deck and apply to self
        shuffle(deck)
        self.deck = deck

    def get_hands(self):
        card_one = randint(0, 51)
        card_two = randint(0, 51)

        # create a hand of two, make sure they aren't the same card.
        while True:
            if card_one == card_two:
                card_two = randint(0, 51)
            else:
                break
        user_hand = ['u', self.deck[card_one], self.deck[card_two]]

        card_one = randint(0, 51)
        card_two = randint(0, 51)

        while True:
            if self.deck[card_one] in user_hand:
                card_one = randint(0, 51)
                continue
            elif self.deck[card_two] in user_hand:
                card_two = randint(0, 51)
                continue
            break
        dealer_hand = ['d', self.deck[card_one], self.deck[card_two]]

        return user_hand, dealer_hand

    def hit(self, hand):
        while True:
            new_card = randint(0, 51)
            if self.deck[new_card] not in hand:
                hand.append(self.deck[new_card])
                break
            else:
                continue
        return hand


def point_calc(hand):
    points = 0
    for card in hand:
        try:
            if int(card[0]) == 1:
                points += 10
            else:
                points += int(card[0])
        except ValueError:
            if card[0] == 'A':
                points += 11
            else:
                points += 10

    # ace can be 1 or 11 depending on the points. this sets
    # the points to be 10 points lower if the user is over 21
    if points > 21 and any("Ace" in x for x in hand):
        points -= 10

    return points


def check_blackjack(hand):
    if point_calc(hand) == 21:
        print("BLACKJACK! YOU WIN!")
        return True
    return False


def check_bust(hand, number):
    if number > 21:
        if hand[0] == 'u':
            print('You busted! You lose!')
            return True
        if hand[0] == 'd':
            print("Dealer busted! You win!")
            return True
    else:
        return False
