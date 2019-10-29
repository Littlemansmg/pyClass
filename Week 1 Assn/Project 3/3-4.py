
print("===============================================================\n"
      "Shipping Calculator\n"
      "===============================================================")

while 1:
    shipping_cost = 0.0
    cost = input("Cost of items ordered: ")
    cost = float(cost)

    if cost <= 0:
        print("You must enter a positive number. Please try again.")
        continue

    if cost < 30:
        shipping_cost = 5.95
    elif 30 <= cost <= 49.99:
        shipping_cost = 7.95
    elif 50 <= cost <= 74.99:
        shipping_cost = 9.95

    total_cost = cost + shipping_cost

    print("Shipping Cost:\t\t   {}\n"
          "Total cost:\t\t\t   {}".format(shipping_cost, round(total_cost, 2)))

    end = input("Continue? (y/n)")
    print("===============================================================")
    if end.lower() != 'n':
        continue
    print("Bye!")
    break



