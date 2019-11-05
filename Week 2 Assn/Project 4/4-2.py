# created by Scott "LittlemanSMG" Goes on 11/05/2019


def miles_to_feet(miles):
    feet = miles * 1520
    return int(feet)


def main():
    miles_input = input("How many miles did you walk?: ")
    miles_input = float(miles_input)
    print("You walked {} feet.".format(miles_to_feet(miles_input)))


if __name__ == "__main__":
    main()
