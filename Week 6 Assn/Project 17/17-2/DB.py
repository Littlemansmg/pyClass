# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import sqlite3


def connect(path):
    return sqlite3.connect(path)


def view(cursor):
    cursor.execute("Select * From Player ORDER BY wins DESC ")
    result = cursor.fetchall()
    return result


def add(connect, cursor, player):
    cursor.execute("SELECT MAX(playerID) from Player")
    # This code is ass, but I can't be bothered to make it work better.
    id = cursor.fetchall()
    new = id[0]
    work = new[0]
    print(work)
    cursor.execute("INSERT INTO Player VALUES (?,?,?,?,?)",
                   (work + 1, player['name'], player['wins'], player['losses'], player['ties']))
    connect.commit()


def delete(connect, cursor, player_name):
    cursor.execute("DELETE FROM Player WHERE name like ?", (player_name,))
    connect.commit()
    print(f"{player_name} was deleted from database.")

