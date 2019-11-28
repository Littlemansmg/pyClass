# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import random


class RandomIntList(list):
    def __init__(self, number):
        super().__init__(self)
        self.number = number
        for i in range(number):
            self.append(random.randint(1, 100))
        self.new_list = []
        for i in range(len(self)):
            self.new_list.append(self[i])

    def __str__(self):
        return str(self.new_list)[1:-1]

    def get_count(self):
        return self.number

    def get_total(self):
        total = 0
        for i in self.new_list:
            total += i
        return total

    def get_average(self):
        total = 0
        for i in self.new_list:
            total += i

        average = round(total / self.number, 3)
        return average


def main():
    print('Random Integer List')
    while True:
        try:
            numbers = int(input("How many integers should the list contain?: "))
            if numbers <= 0:
                raise ValueError
        except ValueError:
            print("Please type a positive integer above 0.")
            continue

        rando = RandomIntList(numbers)
        print("Random Integers\n===============")
        print(f"Integers:\t{rando}\n"
              f"Count:\t\t{rando.get_count()}\n"
              f"Total:\t\t{rando.get_total()}\n"
              f"Average:\t{rando.get_average()}")

        end = input("\nContinue? (y/n): ")
        if end.lower() == 'n':
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
