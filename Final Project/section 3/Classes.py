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
        return f"{self.number} of {self.suit}"


class Hand:
    def __init__(self, deck):
        self.dealer = []
        self.player = []
        for i in range(2):
            self.dealer.append(deck.deal_card())
            self.player.append(deck.deal_card())

    def get_dealer(self):
        return self.dealer

    def print_dealer(self):
        string = ''
        for card in self.dealer:
            string += str(card) + ' '
        return string

    def print_dealer_points(self):
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
        return self.player

    def print_player(self):
        string = ''
        for card in self.player:
            string += str(card) + ' '
        return string

    def print_player_points(self):
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
    def bet(self, money, bet, result):
        if result:
            money = money + (bet * 1.5)
            return money
        else:
            money = money - bet
            return money

    def hit(self, deck, hands, money, bet):
        dealer = hands.get_dealer()
        player = hands.get_player()
        player.append(deck.deal_card())
        temp, money = self.check_bust(hands, money, bet)
        if temp != '':
            return temp, money
        if hands.print_dealer_points() < 17:
            dealer.append(deck.deal_card())
            temp, money = self.check_bust(hands, money, bet)
            if temp != '':
                return temp, money
        return '', money

    def stand(self, deck, hands, money, bet):
        dealer = hands.get_dealer()
        while hands.print_dealer_points() < 17:
            dealer.append(deck.deal_card())
            temp, money = self.check_bust(hands, money, bet)
            if temp is not None:
                return temp, money

        return self.winner(hands, money, bet)

    def winner(self, hands, money, bet):
        dealer = hands.print_dealer_points()
        player = hands.print_player_points()
        if dealer > player:
            money = self.bet(money, bet, False)
            return "Dealer wins!", money
        elif dealer < player:
            money = self.bet(money, bet, True)
            return "You win!", money
        else:
            money = self.bet(money, bet, False)
            return 'Draw!', money

    def check_bust(self, hands, money, bet):
        dealer = hands.print_dealer_points()
        player = hands.print_player_points()
        if dealer > 21:
            money = self.bet(money, bet, True)
            return "Dealer Busted! You win!", money
        if player > 21:
            money = self.bet(money, bet, False)
            return "You Busted! You lose!", money
        return '', money

    def replay(self, hands, result, money):
        print(f"YOUR POINTS:     {hands.print_player_points()}\n"
              f"DEALER'S POINTS: {hands.print_dealer_points()}\n\n"
              f"{result}\n"
              f"Money: {money}\n")
        while True:
            try:
                end = input("Play again? (y/n)").lower()
                if not end.startswith('y') and not end.startswith('n'):
                    raise ValueError
            except ValueError:
                print("Please type y or n.")
                continue
            break
        if end == 'n':
            print("Bye!")
            with open('./money.txt', 'w') as file:
                file.write(str(money))
            exit()
        else:
            return False

