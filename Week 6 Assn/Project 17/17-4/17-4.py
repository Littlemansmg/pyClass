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
        if command == 'update':
            Logic.update(connect, cursor)
        if command == 'exit':
            Logic.end()


if __name__ == "__main__":
    connect = DB.connect("guitar_shop.sqlite")
    cursor = connect.cursor()
    Interface.command_menu()
    main()
