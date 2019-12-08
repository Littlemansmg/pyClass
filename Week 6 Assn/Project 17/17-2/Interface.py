# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def command_menu():
    print("COMMAND MENU\n"
          "view - View players\n"
          "add  - Add a player\n"
          "del  - Delete a player\n"
          "exit - Exit program")


def get_command():
    command = input("Command: ").lower()
    if command != "view" and command != "add" and command != "del" and command != 'exit':
        return ValueError
    return command


def add():
    pass


def delete():
    pass