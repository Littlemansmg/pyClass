# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


import datetime
import logging as logger


def get_value(invest, interest, years):
    total = 0.0

    for i in range(years):
        total += round(invest * 12, 2)
        total += round(total * (interest / 100), 2)

    return round(total, 2)


def get_investment():
    investment = float(input("Enter monthly investment:\t"))
    interest = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter number of years:\t\t"))

    return investment, interest, years


def main():
    invest, interest, years = get_investment()
    future_value = get_value(invest, interest, years)
    print("Future value:\t\t\t\t${:,.2f}".format(future_value))

    logger.info(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S") +
                f" - {invest}|{interest}|{years}|{future_value}")


if __name__ == "__main__":
    logger.basicConfig(handlers=[logger.FileHandler('11-3.log', 'a', 'utf-8')],
                       level=logger.INFO)
    main()
