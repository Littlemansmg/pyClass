# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def math(sales):
    total = 0
    # total
    for i in sales:
        total += i

    # average
    average = round(total / 4, 2)
    print("Total: \t\t\t{}\n"
          "Average Quarter: {}\n"
          "Lowest Quarter:  {}\n"
          "Highest Quarter: {}".format(total, average, min(sales), max(sales)))


def get_sales():
    Q1 = round(float(input("Enter sales for Q1: ")), 2)
    Q2 = round(float(input("Enter sales for Q2: ")), 2)
    Q3 = round(float(input("Enter sales for Q3: ")), 2)
    Q4 = round(float(input("Enter sales for Q4: ")), 2)

    return [Q1, Q2, Q3, Q4]


def main():
    sales = get_sales()
    math(sales)


if __name__ == "__main__":
    main()
