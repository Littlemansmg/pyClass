# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def show_rect(self):
        temp = len("* " * self.width)
        print("* " * self.width)
        for i in range(self.height - 2):
            print("*" + " " * (temp - 3) + "*")
        print("* " * self.width)


def main():
    print("Rectangle Calculator")
    while True:
        height, width = 0, 0
        while True:
            try:
                height = int(input('Height:\t   '))
                if height <= 0:
                    raise ValueError
            except ValueError:
                print("You must put in an integer.")
                continue
            break

        while True:
            try:
                width = int(input('Width: \t   '))
                if width <= 0:
                    raise ValueError
            except ValueError:
                print("You must put in an integer.")
                continue
            break

        new_shape = Rectangle(height, width)
        print(f"Perimeter: {new_shape.perimeter()}")
        print(f"Area:\t   {new_shape.area()}")
        new_shape.show_rect()
        end = input("\nContinue? (y/n): ")
        print()
        if end.lower() == 'n':
            exit()


if __name__ == "__main__":
    main()
