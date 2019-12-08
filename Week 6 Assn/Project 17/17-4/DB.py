# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import sqlite3


def connect(path):
    return sqlite3.connect(path)


def get_cats(cursor):
    cursor.execute("SELECT * FROM Category")
    return cursor.fetchall()


def view(cursor, category):
    cursor.execute("Select productCode, productName, listPrice "
                   "From Product where categoryID = ?", (category,))
    result = cursor.fetchall()
    return result


def update(connect, cursor, code, price):
    cursor.execute("UPDATE Product SET listPrice = ? where productCode = ?",
                   (price, code))

    connect.commit()
