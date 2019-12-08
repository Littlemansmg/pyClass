# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def command_menu():
    print("COMMAND MENU\n"
          "view   - View pending tasks\n"
          "update - Update product price\n"
          "exit   - Exit program")


def get_command():
    command = input("Command: ").lower()
    if command != "view" and command != "update" and command != 'exit':
        return ValueError
    return command
