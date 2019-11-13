# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import time
import csv
import re


def show():
    for i in range(len(contacts)):
        print("{}. {}".format(i + 1, contacts[i][0]))
    time.sleep(2)


def view():
    show()
    while True:
        index = int(input("Number: "))
        try:
            contacts[index - 1]
            print("Name: {}\n"
                  "Email: {}\n"
                  "Phone: {}\n".format(contacts[index - 1][0],
                                       contacts[index - 1][1],
                                       contacts[index - 1][2]))
            time.sleep(2)
            break
        except IndexError:
            print("That's not a valid number. Try again")
            continue


def add():
    name = input("Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    with open('./contacts.csv', 'a') as csvfile:
        write = csv.writer(csvfile, delimiter=',')
        write.writerow([name, email, phone])
    contacts.append([name, email, phone])
    print("{} added.".format(name))


def delete():
    show()
    while True:
        index = int(input("Number: "))
        try:
            contacts[index-1]
            print("{} was deleted.".format(contacts[index - 1][0]))
            contacts.pop(index-1)
            with open('./contacts.csv', 'w') as csvfile:
                for row in contacts:
                    csvfile.write('{},{},{}'.format(row[0], row[1], row[2]))


            break
        except IndexError:
            print("That's not a valid number. Try again")
            continue


def command_menu():
    print("\nCOMMAND MENU\n"
          "list - List all contacts\n"
          "view - View a contact\n"
          "add  - Add a contact\n"
          "del  - Delete a contact\n"
          "exit - Exit program")


def main():
    print("Contact Manager")
    while True:
        command_menu()
        command = input("Command: ")
        if command.lower() == 'list':
            show()
        elif command.lower() == 'view':
            view()
        elif command.lower() == 'add':
            add()
        elif command.lower() == 'del':
            delete()
        elif command.lower() == 'exit':
            print("Bye!")
            exit()


if __name__ == "__main__":
    contacts = []
    with open('./contacts.csv', 'r') as file:
        for i in file.readlines():
            contacts.append(i.split(','))
    main()
