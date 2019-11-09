# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import time


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
            len(contacts)
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
    contacts = [['Guido Van Rossum', "guido@guidovanrossum.com", "999-333-234"],
                ["Eric Idle", "eric@ericidle.com", "+44 20 7946 0958"]]
    main()
