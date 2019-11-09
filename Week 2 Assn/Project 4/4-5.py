# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import random as rand


def check_special(die1, die2):
    if die1 == 1 and die2 == 1:
        print('Snake eyes!')
    elif die1 == 6 and die2 == 6:
        print('Boxcars!')
    if die1 + die2 == 12:
        print("That's my favorite number!")


def user_continue():
    if input("\nRoll again? (y/n): ") == 'n':
        exit()


def title_card():
    print("Dice Roller")
    return input("Roll the dice? (y/n) ")


def roll_die():
    die = rand.randint(1, 6)
    return die


def main():
    if title_card() != 'n':
        while True:
            die1 = 6 #roll_die()
            die2 = 6 #roll_die()
            print("Die 1: {}\n"
                  "Die 2: {}\n"
                  "Total: {}".format(die1, die2, die1 + die2))
            check_special(die1, die2)
            user_continue()


if __name__ == "__main__":
    main()
