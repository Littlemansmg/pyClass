import sqlite3
import csv



def main():
    with sqlite3.connect('customers') as db:
        db.execute("SELECT * FROM Customer")
    # i = 100
    # mydb.execute("SELECT * FROM Customer")
    # with open('customers.csv', 'r') as file:
    #     reader = csv.DictReader(file)
    #     for row in reader:
    #         i += 1
    #         keys = list(row.keys())
    #
    #         test = f"INSERT INTO Customer Values(?,?,?,?,?,?,?,?),({i}, {row[keys[0]]}, {row[keys[1]]}," \
    #                f"{row[keys[2]]}, {row[keys[3]]}, {row[keys[4]]}, {row[keys[5]]}, {row[keys[6]]})"
    #
    #         # sqlstring = f'INSERT INTO Customer VALUES (' \
    #         #             f'{i},' \
    #         #             f'{row[keys[0]]},' \
    #         #             f'{row[keys[1]]},' \
    #         #             f'{row[keys[2]]},' \
    #         #             f'{row[keys[3]]},' \
    #         #             f'{row[keys[4]]},' \
    #         #             f'{row[keys[5]]},' \
    #         #             f'{row[keys[6]]};)'
    #         mydb.execute("INSERT INTO Customer Values(?,?,?,?,?,?,?,?)",
    #                      (i, row[keys[0]], row[keys[1]], row[keys[2]], row[keys[3]],
    #                       row[keys[4]], row[keys[5]], row[keys[6]]))


if __name__ == "__main__":
    main()
