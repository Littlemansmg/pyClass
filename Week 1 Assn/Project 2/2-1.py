

print("Registration Form")

f_name = input("First Name: ")
l_name = input("Last Name: ")
b_year = input("Birth Year: ")
pswd = f_name + "*" + b_year

print("\nWelcome %s %s!" % (f_name, l_name))
print("Your registration is complete")
print("Your temporary password is: %s" % pswd)
