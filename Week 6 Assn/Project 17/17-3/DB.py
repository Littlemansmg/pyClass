# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import sqlite3


def connect(path):
    return sqlite3.connect(path)


def get_all(cursor):
    cursor.execute("SELECT * FROM Task")
    return cursor.fetchall()


def view(cursor):
    cursor.execute("Select * From Task where completed = 0")
    result = cursor.fetchall()
    return result


def complete(connect, cursor, task):
    result = view(cursor)
    taskid = result[task-1][0]
    cursor.execute("UPDATE Task Set completed = 1 where taskID = ?", (taskid,))
    connect.commit()
    print("Task completed.")


def add(connect, cursor, description):
    cursor.execute("SELECT MAX(taskID) from Task")
    # This code is ass, but I can't be bothered to make it work better.
    id = cursor.fetchall()
    new = id[0]
    work = new[0]
    cursor.execute("INSERT INTO task VALUES (?,?,0)",
                   (work + 1, description))
    connect.commit()


def history(cursor):
    cursor.execute("Select * From Task where completed = 1")
    result = cursor.fetchall()
    return result


def delete(connect, cursor, task):
    cursor.execute("DELETE FROM Task WHERE taskID = ?", (task,))
    connect.commit()
    print(f"")

