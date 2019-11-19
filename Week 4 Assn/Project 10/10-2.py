# created by Scott "LittlemanSMG" Goes on 11/19/2019


import re


def mass_template():
    for i in contacts:
        print(template.format(i[2].lower(), i[0].capitalize()))


def main():
    mass_template()


if __name__ == "__main__":
    contacts = []
    template = str
    try:
        with open('./email.txt', 'r') as file:
            for i in file:
                contacts.append(re.split('; |,|\n', i))

        with open('./template_email.txt') as file:
            template = str(file.read())

    except FileNotFoundError:
        print("Can't find files.\nBye!")
        exit()

    main()
