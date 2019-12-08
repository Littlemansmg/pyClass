# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def command_menu():
    print("COMMAND MENU\n"
          "view     - View pending tasks\n"
          "history  - View completed tasks\n"
          "add      - Add a task\n"
          "complete - Complete a task\n"
          "del      - Delete a task\n"
          "exit     - Exit program")


def get_command():
    command = input("Command: ").lower()
    if command != "view" and command != "add" and command != "del" and \
            command != 'exit' and command != 'history' and command != 'complete':
        return ValueError
    return command
