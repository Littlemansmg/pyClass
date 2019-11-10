# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def is_winner(player):
    horizontal = []
    for i in range(len(board)):
        for x in range(len(board[i])):
            horizontal.append(board[i][x])
            if len(horizontal) < 3:
                continue
            else:
                if horizontal[0] == player and horizontal[1] == player and horizontal[2] == player:
                    print("{} wins!".format(player))
                    exit()
        horizontal.clear()

    if board[0][0] == player and board[1][0] == player and board[2][0] == player:
        print("{} wins!".format(player))
        exit()
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        print("{} wins!".format(player))
        exit()
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        print("{} wins!".format(player))
        exit()
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        print("{} wins!".format(player))
        exit()
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        print("{} wins!".format(player))
        exit()


def player_turn(player):
    print("{}'s turn".format(player))
    while True:
        row = int(input("Pick a row (1, 2, 3): ")) - 1
        column = int(input("Pick a column (1, 2, 3): ")) - 1

        try:
            board[row][column]
            if board[row][column] != ' ':
                raise IndexError
            else:
                board[row][column] = player
                break
        except IndexError:
            print("Try again")
    display_board()


def display_board():
    print("+---+---+---+\n"
          "| {} | {} | {} |\n"
          "+---+---+---+\n"
          "| {} | {} | {} |\n"
          "+---+---+---+\n"
          "| {} | {} | {} |\n"
          "+---+---+---+".format(board[0][0], board[0][1], board[0][2],
                                 board[1][0], board[1][1], board[1][2],
                                 board[2][0], board[2][1], board[2][2]))


def main():
    display_board()
    while True:
        player_turn('X')
        is_winner('X')
        player_turn('O')
        is_winner('O')


if __name__ == "__main__":
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    main()
