# created by Scott "LittlemanSMG" Goes on 11/05/2019


def get_total():
    running_total = 0.0
    sales_tax = .06
    print("Enter Items (Enter 0 to end)")
    while True:
        item = float(input("Cost of item: "))
        if item != 0:
            running_total += item
        else:
            break

    final_total = round((running_total * sales_tax) + running_total, 2)
    print("Total:\t\t\t {}\n"
          "Sales Tax:\t\t {}\n"
          "Total after tax: {}".format(running_total, round(running_total * sales_tax, 2), final_total))
    return final_total


def end():
    if input("Again? (y/n): ").lower() == 'n':
        print("Thanks bye!")
        exit()

