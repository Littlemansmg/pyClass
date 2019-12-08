# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY
import DB


def view(cursor):
    results = DB.view(cursor)
    i = 0
    for task in results:
        i += 1
        print(f"{i}. {task[1]}")


def add(connect, cursor):
    description = input("Description: ")

    DB.add(connect, cursor, description)


def complete(connect, cursor):
    task = int(input("Task: "))
    DB.complete(connect, cursor, task)


def delete(connect, cursor):
    task = int(input("task: "))
    result = DB.get_all(cursor)
    taskid = result[task - 1][0]
    DB.delete(connect, cursor, taskid)


def history(cursor):
    results = DB.history(cursor)
    i = 0
    for task in results:
        i += 1
        print(f"{i}. {task[1]}")


def end():
    print("Bye!")
    exit()
