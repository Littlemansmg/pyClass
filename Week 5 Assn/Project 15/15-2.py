# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import random


class Player:
    def __init__(self, name, roshambo):
        self.name = name
        self.roshambo = roshambo

    def __str__(self):
        return self.name + ': ' + self.roshambo


class Bart(Player):
    def generateRoshambo(self):
        return 'Rock'


class Lisa(Player):
    def generateRoshambo(self):
        options = ['Rock', 'Paper', 'Scissors']
        return random.choice(options)


def bart_play(player):
    bart = Bart('Bart', '')
    bart.roshambo = bart.generateRoshambo()
    win_logic(player, bart)


def lisa_play(player):
    lisa = Lisa('Lisa', '')
    lisa.roshambo = lisa.generateRoshambo()
    win_logic(player, lisa)


def win_logic(player1, player2):
    if player1.roshambo == player2.roshambo:
        print(player1)
        print(player2)
        print("Draw!")
    elif player1.roshambo == 'Rock' and player2.roshambo == 'Scissors':
        print(player1)
        print(player2)
        print(f"{player1.name} Wins!")
    elif player1.roshambo == 'Paper' and player2.roshambo == 'Rock':
        print(player1)
        print(player2)
        print(f"{player1.name} Wins!")
    elif player1.roshambo == 'Scissors' and player2.roshambo == 'Paper':
        print(player1)
        print(player2)
        print(f"{player1.name} Wins!")
    else:
        print(player1)
        print(player2)
        print(f"{player2.name} Wins!")


def get_option(option):
    if option.lower() == 'r':
        return 'Rock'
    if option.lower() == 'p':
        return 'Paper'
    if option.lower() == 's':
        return 'Scissors'


def main():
    print("Roshambo Game")
    name = input('Enter your name: ').capitalize()
    while True:
        try:
            opponent = input('Would you like to play against Bart or Lisa? (b/l): ')
            lst_option = ['b', 'l']
            if not opponent.lower() in lst_option:
                raise ValueError
        except ValueError:
            print("Please pick Bart or Lisa")
            continue
        break

    while True:
        try:
            option = input('Rock, paper, or scissors? (r/p/s): ')
            lst_option = ['r', 'p', 's']
            if not option.lower() in lst_option:
                raise ValueError
        except ValueError:
            print("Please type r p or s.")
            continue

        player1 = Player(name, get_option(option))

        if opponent.lower() == 'b':
            bart_play(player1)

        if opponent.lower() == 'l':
            lisa_play(player1)

        end = input("\nPlay again? (y/n): ")
        if end.lower() == 'n':
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
