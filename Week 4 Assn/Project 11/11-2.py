# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import datetime
import re


def get_time(miles, mph):
    hours = int(miles) // int(mph)
    minutes = int(miles) % int(mph)

    return [hours, minutes]


def get_travel():
    date_depart = input("Estimated date of departure (YYYY-MM-DD): ").split('-')
    time_depart = input("Estimated time of departure (HH:MM AM/PM): ")
    time_depart = re.split('; |:| ', time_depart)
    if time_depart[2].lower() == 'pm':
        time_depart[0] = int(time_depart[0]) + 12

    full_depart = datetime.datetime(int(date_depart[0]), int(date_depart[1]),
                                    int(date_depart[2]), int(time_depart[0]),
                                    int(time_depart[1]))
    miles_travel = int(input("Enter miles: "))
    mph_travel = int(input("Enter miles per hour: "))

    return full_depart, miles_travel, mph_travel


def main():
    while True:
        full_depart, miles, mph = get_travel()

        travel_time = get_time(miles, mph)
        full_depart += datetime.timedelta(hours=travel_time[0],
                                          minutes=travel_time[1])

        print("Hours {}\n"
              "Minutes: {}\n"
              "Estimated date of arrival: {}\n"
              "Estimated time of arrival: {}\n"
              "".format(travel_time[0], travel_time[1],
                        full_depart.strftime('%Y-%m-%d'), full_depart.strftime('%I:%M %p')))

        end = input("Continue? (y/n): ")
        if end.lower() == 'n':
            print('Bye!')
            exit()


if __name__ == "__main__":
    main()
