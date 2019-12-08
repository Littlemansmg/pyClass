# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import DB


def view(cursor):
    results = DB.view(cursor)
    print(f"Name\t\tWins\tLosses\tTies\tGames\n"
          f"--------------------------------------------------")
    for player in results:
        games = int(player[2] + player[3] + player[4])
        print(f"{player[1]}\t\t{player[2]}\t\t{ player[3]}\t\t{player[4]}\t\t{games}")


def add(connect, cursor):
    player = {'name': input("Name: "), 'wins': input("Wins: "),
              'losses': input("Losses: "), 'ties': input("Ties: ")}

    DB.add(connect, cursor, player)

    print(f"{player['name']} was added to database.")


def delete(connect, cursor):
    player = input("Name: ")
    DB.delete(connect, cursor, player)

def end():
    print("Bye!")
    exit()
