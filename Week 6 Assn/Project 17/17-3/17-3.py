import DB
import Interface
import Logic


def main():
    while True:
        try:
            command = Interface.get_command()
        except ValueError:
            print("Invalid command")
            continue
        if command == 'view':
            Logic.view(cursor)
        if command == 'history':
            Logic.history(cursor)
        if command == 'add':
            Logic.add(connect, cursor)
        if command == 'complete':
            Logic.complete(connect, cursor)
        if command == 'del':
            Logic.delete(connect, cursor)
        if command == 'exit':
            Logic.end()


if __name__ == "__main__":
    connect = DB.connect("task_list_db.sqlite")
    cursor = connect.cursor()
    Interface.command_menu()
    main()