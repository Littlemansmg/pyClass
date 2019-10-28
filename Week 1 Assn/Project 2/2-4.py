
print("Price Comparison")

detergent64 = input("Price of 64 oz size: ")
detergent32 = input("Price of 32 oz size: ")

print("\nPrice per oz (64 oz): \t{}\n"
      "Price per oz (32 oz): \t{}".format(round(float(detergent64)/64, 2),
                                          round(float(detergent32)/32, 2)))
