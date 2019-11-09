# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import time


def show():
    for i in range(len(items)):
        print("{}. {}".format(i + 1, items[i]))
    time.sleep(2)


def grab():
    if len(items) < 4:
        item_name = input("Name: ")
        items.append(item_name)
        print("{} was added".format(item_name))
    else:
        print("You can't carry any more items. Drop something first.")
    time.sleep(2)


def edit():
    show()
    while True:
        update = int(input("Number: "))
        try:
            items[update - 1]  # probably a better way to do this but it works.
            name_update = input("Updated name: ")
            items[update - 1] = name_update
            print("Item number {} was updated.".format(update))
            time.sleep(2)
            break
        except IndexError:
            print("That's not a valid number. Try again")
            continue


def drop():
    show()
    while True:
        update = int(input("Number: "))
        try:
            items[update - 1]
            print("{} was dropped".format(items[update - 1]))
            items.pop(update - 1)
            time.sleep(2)
        except IndexError:
            print("That's not a valid number. Try again")
            continue


def command_menu():
    print("\nCOMMAND MENU\n"
          "show - Show all items\n"
          "grab - Grab an item\n"
          "edit - Edit an item\n"
          "drop - Drop an item\n"
          "exit - Exit program")


def main():
    while True:
        command_menu()
        command = input("Command: ")
        if command.lower() == 'show':
            show()
        elif command.lower() == 'grab':
            grab()
        elif command.lower() == 'edit':
            edit()
        elif command.lower() == 'drop':
            drop()
        elif command.lower() == 'exit':
            print("Bye!")
            exit()


if __name__ == "__main__":
    items = ['wooden staff', 'wizard hat', 'cloth shoes']
    main()
