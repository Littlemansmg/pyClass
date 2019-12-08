import sqlite3
import csv


def main():
    connect = sqlite3.connect("customers.sqlite")
    cursor = connect.cursor()

    cursor.execute("DELETE FROM Customer")

    i = 100
    with open('customers.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            i += 1
            keys = list(row.keys())

            cursor.execute("INSERT INTO Customer Values(?,?,?,?,?,?,?,?)",
                           (i, row[keys[0]], row[keys[1]], row[keys[2]], row[keys[3]],
                            row[keys[4]], row[keys[5]], row[keys[6]]))
            cursor.execute("Select * from customer")

        connect.commit()

    print("Customer Data Importer.\n\n"
          "CSV file:\tcustomers.csv\n"
          "DB file:\tcustomers.sqlite\n"
          "Table name: Customer\n\n"
          "All old rows deleted from Customer table.\n"
          "{} rows(s) inserted into Customer table.".format(i-100))


if __name__ == "__main__":
    main()
