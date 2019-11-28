# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.height + self.width) * 2

    def __str__(self):
        shape = ''
        shape += ("* " * self.width)
        for i in range(self.height - 2):
            shape += ('\n* ' + "  " * (self.width - 2) + '*')
        shape += ('\n' + "* " * self.width)
        return shape


class Square(Rectangle):
    pass


def square():
    length = 0
    while True:
        try:
            length = int(input("Length:\t   "))
            if length <= 0:
                raise ValueError
        except ValueError:
            print("You must put in an integer.")
            continue
        break

    new_shape = Square(length, length)
    print(f"Perimeter: {new_shape.perimeter()}")
    print(f"Area:\t   {new_shape.area()}")
    print(new_shape)


def rect():
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
    print(new_shape)


def main():
    print("Rectangle Calculator")

    while True:
        try:
            shape = input("Rectangle or square? (r/s): ")
            if shape.lower() != 'r' and shape.lower() != 's':
                raise ValueError
        except ValueError:
            print("Please type r or s.")
            continue

        if shape == 'r':
            rect()

        if shape == 's':
            square()


        end = input("\nContinue? (y/n): ")
        print()
        if end.lower() == 'n':
            exit()


if __name__ == "__main__":
    main()
