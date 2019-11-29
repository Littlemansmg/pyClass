# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


class Person:
    def __init__(self, f_name, l_name, email):
        self.f_name = f_name
        self.l_name = l_name
        self.email = email


class Customer(Person):
    def __init__(self, f_name, l_name, email, number, title='Customer'):
        super().__init__(f_name, l_name, email)
        self.number = number
        self.title = title


class Employee(Person):
    def __init__(self, f_name, l_name, email, ssn, title='Employee'):
        super().__init__(f_name, l_name, email)
        self.ssn = ssn
        self.title = title


def customer_display():
    fname = input("First name: ")
    lname = input("Last name: ")
    email = input("Email: ")
    number = input("Number: ")
    cust = Customer(fname, lname, email, number)

    if isinstance(cust, Customer):

        print(f"{cust.title}\n"
              f"First name: {cust.f_name}\n"
              f"Last name:  {cust.l_name}\n"
              f"Email:\t\t{cust.email}\n"
              f"Number:\t\t{cust.number}\n")


def employee_display():
    fname = input("First name: ")
    lname = input("Last name: ")
    email = input("Email: ")
    ssn = input("Ssn: ")
    employ = Employee(fname, lname, email, ssn)

    if isinstance(employ, Employee):
        print(f"{employ.title}\n"
              f"First name: {employ.f_name}\n"
              f"Last name:  {employ.l_name}\n"
              f"Email:\t\t{employ.email}\n"
              f"Ssn:\t\t{employ.ssn}\n")


def main():
    print("Customer/Employee Data Entry")
    while True:
        try:
            cust_employ = input("Customer or Employee? (c/e): ").lower()
            if cust_employ != 'c' and cust_employ != 'e':
                raise ValueError
        except ValueError:
            print("You must type c or e.")
            continue

        if cust_employ == 'c':
            customer_display()
        if cust_employ == 'e':
            employee_display()

        end = input("\nContinue? (y/n): ")
        if end.lower() == 'n':
            print("Bye!")
            exit()


if __name__ == "__main__":
    main()
