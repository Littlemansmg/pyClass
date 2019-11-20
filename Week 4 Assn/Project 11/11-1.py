# created by Scott "LittlemanSMG" Goes on 11/19/2019


import datetime
import math


def do_math_list(birthday, today, name):
    template_format = [name,
                       birthday.strftime('%A, %B %d, %Y'),
                       today.strftime('%A, %B %d, %Y')]

    age_days = (datetime.date(today.year, today.month, today.day) -
                datetime.date(birthday.year, birthday.month, birthday.day)).days

    if age_days < 730:
        template_format.append(str(age_days) + " days")
    else:
        template_format.append(str(math.floor(age_days / 365)) + " years")

    is_birthday = (datetime.date(1, today.month, today.day) -
                   datetime.date(1, birthday.month, birthday.day)).days

    if is_birthday == 0:
        template_format.append(name + "'s birthday is today!")
    elif is_birthday == -1:
        template_format.append(name + "'s birthday is tomorrow!")
    elif is_birthday == 1:
        template_format.append(name + "'s birthday was yesterday.")
    else:
        template_format.append(name + "'s birthday is in " + str(abs(is_birthday)) + " days")

    return template_format


def format_date(birthday):
    birthday_date = birthday.split('/')
    if birthday_date[2] > datetime.datetime.now().strftime('%Y'):
        birthday_date[2] = "19" + birthday_date[2]
    else:
        birthday_date[2] = "20" + birthday_date[2]

    month, day, year = int(birthday_date[0]), int(birthday_date[1]), int(birthday_date[2])
    birth = datetime.date(year, month, day)
    today = datetime.datetime.now()

    return birth, today


def get_birth():
    name = input("Enter name: ")
    birthday = input('Enter birthday (MM/DD/YY): ')

    return name, birthday


def main():
    print('Birthday Calculator')
    while True:
        name, birthday = get_birth()
        fmt_birth, today = format_date(birthday)
        template = do_math_list(fmt_birth, today, name)
        print("Birthday: {}\n"
              "Today:\t{}\n"
              "{} is {} old.\n"
              "{}\n".format(template[1], template[2], template[0],
                            template[3], template[4]))
        end = input('Continue? y/n: ')
        if end.lower() == 'n':
            print('Bye!')
            exit()


if __name__ == "__main__":
    main()
