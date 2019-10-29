
print("change calculator")


while 1:
    cents = input("Enter number of cents (0-99): ")
    cents = int(cents)
    quarter = cents // 25
    dimes = (cents - quarter * 25) // 10
    nickle = (cents - (quarter * 25) - (dimes * 10)) // 5
    penny = (cents - (quarter * 25) - (dimes * 10) - (nickle * 5)) // 1

    print("Quarters:\t{}\n"
          "Dimes:\t\t{}\n"
          "Nickles:\t{}\n"
          "Pennies:\t{}\n".format(quarter, dimes, nickle, penny))

    end = input("Continue? (y/n)")
    if end.lower() != 'n':
        continue
    print("Bye!")
    break
