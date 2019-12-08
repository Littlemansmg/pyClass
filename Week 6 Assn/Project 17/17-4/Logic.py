# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY

import DB


def view(cursor):
    cats = DB.get_cats(cursor)
    cat_list = {}
    for cat in cats:
        cat_list[cat[1]] = cat[0]
        print(cat[1] + " | ", end='')
    print()
    try:
        cat_name = input("Category name: ").capitalize()
        if cat_name not in cat_list.keys():
            raise ValueError

        cat_id = cat_list[cat_name]

    except ValueError:
        print("Invalid category")
        return

    results = DB.view(cursor, cat_id)

    print("Code\t\tName\t\t\t\t\tPrice\n"
          "--------------------------------------------------------------")
    for result in results:
        print(f"{result[0]} | {result[1]} | {result[2]}")


def update(connect, cursor):
    code = input("Product code: ").lower()
    price = input("New price: ")

    DB.update(connect, cursor, code, price)
    print("Product updated")


def end():
    print("Bye!")
    exit()
