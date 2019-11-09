# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def end():
    if input("Try again? (y/n): ") == 'n':
        print("Bye!")
        exit()


def check_prime(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)

    if len(factors) == 2:
        print("{} is prime".format(number))
    else:
        print("{} is not prime.\n"
              "It has {} factors: ".format(number, len(factors)))
        print(*factors)


def user_prime():
    while True:
        user_number = int(input("Please enter an integer been 1 and 5000:"))
        if 1 < user_number < 5000:
            check_prime(user_number)
            break
        else:
            print("Invalid integer. Please try again.")
            continue


def main():
    print("Prime Number Checker")
    while True:
        user_prime()
        end()


if __name__ == "__main__":
    main()
