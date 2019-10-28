
print("Tip Calculator")

cost = input("Cost of meal: ")
tip_percent = input("Tip percent: ")

cost = float(cost)
tip_percent = float(tip_percent)

tip_total = cost * (tip_percent / 100)
cost_total = cost + tip_total

print("\nTip amount: \t{}\n"
      "Total amount: \t{}".format(round(tip_total, 2), round(cost_total, 2)))

