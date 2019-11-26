# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import random


def search_number(number, number_random):
    middle = int(len(number_random) // 2 - 1)
    try:
        if number == number_random[middle]:
            print(f"{number} is in random numbers.")
        if number < number_random[middle]:
            search_number(number, number_random[:middle])
        if number > number_random[middle]:
            search_number(number, number_random[middle:])
    except IndexError:
        print(f"{number} is NOT in random numbers.")




def get_number():
    numbers = []
    for i in range(10):
        numbers.append(random.randint(1, 100))

    return numbers


def main():
    print("Binary Search")
    print("Enter 'x' to exit")
    print(number_rand)
    while True:
        find_number = 0

        while True:
            try:
                find_number = input("Enter a number from 1 to 100: ")
                if find_number.lower() == 'x':
                    print('Bye!')
                    exit()
                elif 1 > int(find_number) > 100:
                    raise ValueError
            except ValueError:
                print("You must type in a number between 1 and 100:")
                continue
            break

        search_number(int(find_number), number_rand)


if __name__ == "__main__":
    number_rand = get_number()
    number_rand.sort()
    main()
