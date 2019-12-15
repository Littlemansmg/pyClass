# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import sqlite3
import datetime


def connect(path):
    return sqlite3.connect(path)


def get_money(cursor):
    cursor.execute("SELECT stopMoney from Sessions order by Session_ID desc limit 1")
    start_money = cursor.fetchall()
    return start_money[0][0]


def session_end(connect, cursor, start_time, start_money=100, added=0, stop_money=100):
    stop = datetime.datetime.now()
    cursor.execute('INSERT INTO Sessions(startTime, startMoney, addedMoney, stopTime, stopMoney)'
                   ' Values(?,?,?,?,?)',
                   (start_time, start_money, added, stop, stop_money))
    connect.commit()
