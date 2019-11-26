# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def guess_number(number, guesses, num_range):
    middle = int(len(num_range) // 2)
    guesses += 1
    if number == num_range[middle]:
        print(f"Guess {guesses} is {num_range[middle]}")
        print(f"The computer found it in {guesses} guesses.")
    elif number > num_range[middle]:
        print(f"Guess {guesses} is {num_range[middle]}")
        guess_number(number, guesses, num_range[middle:])
    elif number < num_range[middle]:
        print(f"Guess {guesses} is {num_range[middle]}")
        guess_number(number, guesses, num_range[:middle])


def main():
    print("Number Finder")
    print("Enter 'x' to exit")
    while True:
        find_number = 0

        while True:
            try:
                find_number = input("Enter a number between 0 and 100: ")
                if find_number.lower() == 'x':
                    print('Bye!')
                    exit()
                elif 1 > int(find_number) > 100:
                    raise ValueError
            except ValueError:
                print("You must type in a number between 1 and 100:")
                continue
            break

        guess_number(int(find_number), 0, number_range)


if __name__ == "__main__":
    number_range = []
    for i in range(101):
        number_range.append(i)
    main()
