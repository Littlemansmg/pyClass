# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def get_info():
    cost = float
    tip = int
    while True:
        try:
            cost = float(input("Cost of meal: "))
            if cost < 0:
                print("Must be greater than 0. Please try again.")
                continue
        except ValueError:
            print("Must be a valid decimal number. Please try again.")
            continue
        while True:
            try:
                tip = int(input('Tip percent: '))
            except ValueError:
                print('Must be a valid integer. Please Try again.')
                continue
            break
        break

    tip_calc(cost, tip)


def tip_calc(cost, tip):
    tip_total = round(cost * (tip/100), 2)
    total = round(tip_total + cost, 2)

    print("\nCost of meal: \t{}\n"
          "Tip percent:\t{}%\n"
          "Tip amount:\t\t{}\n"
          "Total amount:\t{}".format(cost, tip, tip_total, total))


def main():
    print("Tip Calculator")
    get_info()


if __name__ == "__main__":
    main()
