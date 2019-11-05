# created by Scott "LittlemanSMG" Goes on 11/05/2019


def even_odd_check(number):
    if number % 2 == 1:
        return "odd"
    else:
        return "even"


def main():
    input_number = input("Enter an integer: ")
    print("This is an {} number.".format(even_odd_check(int(input_number))))


if __name__ == "__main__":
    main()
