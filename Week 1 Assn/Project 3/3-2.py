
def tip_calc(price, tip_per):
    tip = price * (tip_per/100)
    total = tip + price
    return round(tip, 2), round(total, 2)


cost = input("Cost of meal: ")
cost = float(cost)
tip_percent = [15, 20, 25]

for i in range(0, 3):
    array = tip_calc(cost, tip_percent[i])
    print("\n{}%\n"
          "Tip amount:\t{}\n"
          "Total amount:\t{}".format(tip_percent[i],
                                     array[0],
                                     array[1]))

