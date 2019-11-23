# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import time
import re


def cmd_view():
    try:
        month = input("Three-letter month: ").capitalize()
        if month not in sales.keys():
            raise Exception

        print(f'Sale amount for {month} is ${float(sales[month]):,.2f}')

    except Exception:
        print("Invalid month")

    time.sleep(2)


def cmd_totals():
    yearly_total = 0.0
    for line in sales.keys():
        try:
            yearly_total += float(sales[line])
        except ValueError:
            print("Using sales amount of 0 for {}".format(line[0]))

    average = round(yearly_total / 12, 2)

    print(f'Yearly total:     ${yearly_total:,.2f}\n'
          f'Monthly average:  ${average:,.2f}')
    time.sleep(2)


def cmd_edit():
    new_month = input("Three-letter Month: ")
    new_sales = input("Sales amount: ")
    sales[new_month] = new_sales
    with open('./monthly_sales.txt', 'w') as file:
        for key, value in sales.items():
            file.write(f'{key} {value}\n')
    print(f'Sales amount for {new_month} is ${float(new_sales):,.2f}')


def cmd_exit():
    print('Bye!')
    exit()


def command_menu():
    print("COMMAND MENU\n"
          "view   - View sales for a specified month\n"
          "edit   - Edit sales for a specified month\n"
          "totals - view sales summary for the year\n"
          "exit   - Exit the program")


def main():
    print('Monthly Sales Program')
    while True:
        command_menu()
        command = input("Command: ")
        if command.lower() == 'view':
            cmd_view()
        elif command.lower() == 'edit':
            cmd_edit()
        elif command.lower() == 'totals':
            cmd_totals()
        elif command.lower() == 'exit':
            print("Bye!")
            exit()


if __name__ == "__main__":
    sales = {}
    with open('./monthly_sales.txt', 'r') as file:
        for line in file.readlines():
            line = re.split("; |\t|\n", line)
            sales[line[0]] = line[1]

    main()
