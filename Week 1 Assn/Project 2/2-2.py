

tax_rate = 0.18

print("Pay Check Calculator")
hours_worked = input("Hours Worked: ")
pay_rate = input("Hourly Pay Rate: ")

gross_pay = float(hours_worked) * float(pay_rate)
tax_amount = gross_pay * tax_rate
net_pay = gross_pay - tax_amount

print("Gross Pay: \t\t{} \n"
      "Tax Rate: \t\t{}% \n"
      "Tax Amount: \t{} \n"
      "Take Home Pay: \t{} \n".format(gross_pay, tax_rate*100, tax_amount, net_pay))
