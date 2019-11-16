# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import csv
import time


def cmd_monthly():
    for line in sales:
        print('{} - {}'.format(line[0], line[1]))
    time.sleep(2)


def cmd_yearly():
    yearly_total = 0.0
    for line in sales:
        yearly_total += float(line[1])

    average = round(yearly_total / 12, 2)

    print('Yearly total:     {}\n'
          'Monthly average:  {}'.format(yearly_total, average))


def cmd_edit():
    new_month = input("Three-letter Month: ")
    new_sales = input("Sales amount: ")
    for i in range(len(sales) + 1):
        if new_month == sales[i][0]:
            sales[i][1] = new_sales
            break
    with open('./monthly_sales.csv', 'w') as csvfile:
        write = csv.writer(csvfile, delimiter=',', lineterminator='\n')
        for row in sales:
            write.writerow(row)


def cmd_exit():
    print('Bye!')
    exit()


def command_menu():
    print("COMMAND MENU\n"
          "monthly - View monthly sales\n"
          "yearly  - View yearly summary\n"
          "edit    - Edit sales for a month\n"
          "exit    - Exit the program")


def main():
    print('Monthly Sales Program')
    while True:
        command_menu()
        command = input("Command: ")
        if command.lower() == 'monthly':
            cmd_monthly()
        elif command.lower() == 'yearly':
            cmd_yearly()
        elif command.lower() == 'edit':
            cmd_edit()
        elif command.lower() == 'exit':
            print("Bye!")
            exit()


if __name__ == "__main__":
    sales = []
    with open('monthly_sales.csv', 'r') as csfile:
        reader = csv.reader(csfile.readlines())
        for line in reader:
            sales.append(line)

    main()
