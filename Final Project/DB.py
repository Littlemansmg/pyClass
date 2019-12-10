# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import sqlite3


def connect(path):
    return sqlite3.connect(path)

def get_money(cursor):
    cursor.execute("SELECT stopMoney from Sessions")
    start_money = cursor.fetchall()
    return start_money[0][0]
