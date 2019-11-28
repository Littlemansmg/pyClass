# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


class Person:
    def __init__(self, id, first, last, company, address, city, state, zip):
        self.id = id
        self.first = first
        self.last = last
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def __str__(self):
        string = (self.id + ', ' + self.first + ', ' + self.last + ', ' +
                  self.company + ', ' + self.address + ', ' + self.city + ', ' +
                  self.state + ', ' + self.zip)
        return string

    def show_person(self):
        if self.company == '':
            return (self.first + ' ' + self.last + '\n' +
                    self.address + '\n' + self.city + ', ' +
                    self.state + ' ' + self.zip)
        else:
            return (self.first + ' ' + self.last + '\n' +
                    self.company + '\n' +
                    self.address + '\n' +
                    self.city + ', ' + self.state + ' ' + self.zip)


def main():
    print("Customer Viewer")
    while True:
        custid = input("\nEnter customer ID: ")
        for i in range(len(people)):
            if custid == people[i].id:
                print(Person.show_person(people[i]) + '\n')
                break

            if people[i] == people[-1]:
                print("\nNo customer with that ID.\n")
        end = input("Continue? (y/n): ")
        if end.lower() == 'n':
            print("Bye!")
            exit()


if __name__ == "__main__":
    customers = []
    people = []
    with open("./customers.csv") as file:
        records = file.readlines()
        for row in records:
            customers.append(row.strip().split(','))

    for customer in customers:
        people.append(Person(customer[0], customer[1], customer[2], customer[3],
                             customer[4], customer[5], customer[6], customer[7]))
    main()
