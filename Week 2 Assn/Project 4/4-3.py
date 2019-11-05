# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def meter_ft():
    meter_input = float(input("Enter meters: "))
    ft = meter_input / 0.3048
    print("{} meters".format(round(ft, 2)))


def ft_meter():
    ft_input = float(input("Enter feet: "))
    meter = ft_input * 0.3048
    print("{} meters".format(round(meter, 2)))


def title_n_menu():
    print("Feet and Meters Converter\n\n"
          "Conversions Menu:\n"
          "a. Feet to Meters\n"
          "b. Meters to Feet.")
    conversion_input = input("Select a conversion (a/b)")
    return conversion_input


def main():
    while True:
        if title_n_menu() == 'a':
            ft_meter()
        else:
            meter_ft()

        end = input("Would you like to perform another conversion? (y/n): ")
        if end.lower() == 'y':
            continue
        break
    print("Thanks, bye!")


if __name__ == "__main__":
    main()
