# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import time
import random as rand
import os


def updateinventory(item):
    update = open('./inventory.txt', 'a', encoding='utf-8')
    update.writelines('\n' + item)
    update.close()


def walk():
    randomitem = rand.choice(itemlist)
    print("While talking down a path, you see {}.".format(randomitem))
    pickup = input("Do you want to grab it? (y/n)")

    if len(inventory) < 4 and pickup == 'y':
        updateinventory(randomitem)
        inventory.append(randomitem)
        print("Picked up {}.".format(randomitem))
    elif pickup == 'n':
        print("Okay.")
    else:
        print("You can't carry any more items. Drop something first.")


def show():
    for i in range(len(inventory)):
        print("{}. {}".format(i + 1, inventory[i]))
    time.sleep(2)


def drop():
    show()
    while True:
        try:
            update = int(input("Number: "))
            inventory[update - 1]
            print("{} was dropped".format(inventory[update - 1]))
            inventory.pop(update - 1)
            time.sleep(2)
            break
        except (IndexError, ValueError):
            print("That's not a valid number. Try again")
            continue
    update = open('./inventory.txt', 'w', encoding='utf-8')
    for line in inventory:
        update.write('\n' + line)

    update.close()


def command_menu():
    print("\nCOMMAND MENU\n"
          "walk - Walk down the path\n"
          "show - Show all items\n"
          "drop - Drop an item\n"
          "exit - Exit program")


def main():
    while True:
        command_menu()
        command = input("Command: ")
        if command.lower() == 'walk':
            walk()
        elif command.lower() == 'show':
            show()
        elif command.lower() == 'drop':
            drop()
        elif command.lower() == 'exit':
            print("Bye!")
            exit()


if __name__ == "__main__":
    inventory = []
    itemlist = []

    try:
        if not os.path.exists('./inventory.txt'):
            print("Could not find inventory file!\n"
                  "Wizard is starting with no inventory.")
            with open('./inventory.txt', 'w'):
                pass
        else:
            with open('./inventory.txt', 'r') as file:
                for i in file.readlines():
                    inventory.append(i.strip('\n'))
                file.close()
    except FileNotFoundError:
        print("Could not fine inventory file!\n"
              "Wizard is starting with no inventory.")

    if not os.path.exists('./wizard_all_items.txt'):
        print("Could not find items file.\n"
              "Exiting program. Bye!")
        exit()

    file = open('./wizard_all_items.txt', "r", encoding='utf-8')
    for i in file.readlines():
        itemlist.append(i.strip('\n'))

    main()
