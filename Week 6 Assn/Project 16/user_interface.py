# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

from game_logic import point_calc


def display_hand(hand):
    if hand[0] == 'u':
        print("Your Cards:")
        for card in hand[1:]:
            print(card)
    elif hand[0] == 'd':
        print("Dealer's Show Card:")
        print(hand[1])
        print()
    else:
        print("Dealers hand:")
        for card in hand[1:]:
            print(card)


def get_points(hand):
    print(f"{point_calc(hand)} points.")


def ask_hit():
    while True:
        try:
            option = input("\nHit or Stand? (hit/stand): ")
            if option.lower() != 'hit' and option.lower() != 'stand':
                raise ValueError
        except ValueError:
            print("Please type hit or stand.")
            continue
        break
    return option.lower()


def winner(user_hand, dealer_hand):
    u_points = point_calc(user_hand[1:])
    d_points = point_calc(dealer_hand[1:])
    print(f'Your Points: {u_points}\n'
          f'Dealers Points: {d_points}\n')
    if u_points > d_points:
        print("You win!")
        return True
    elif u_points < d_points:
        print("Dealer wins!")
        return True
    else:
        print("Draw!")
        return True


def end():
    while True:
        try:
            end = input("Play again? (y/n): ")
            if end.lower() != 'y' and end.lower() != 'n':
                raise ValueError
            elif end.lower() == 'n':
                print("Come back soon!")
                exit()
        except ValueError:
            print("Please type y or n.")
        break
