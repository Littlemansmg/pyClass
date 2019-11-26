# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def get_info():
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    return num1, num2


def get_gcd(num1, num2):
    remainder = num1 % num2
    if remainder == 0:
        print(f"Greatest common divisor: {num2}")
    else:
        get_gcd(num2, remainder)


def main():
    print("Greatest Common Divisor")
    while True:
        num1, num2 = get_info()
        get_gcd(num1, num2)
        end = input("Continue? (y/n): ")
        if end.lower() == 'n':
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
