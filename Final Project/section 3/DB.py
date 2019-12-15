# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def get_money():
    with open('./money.txt', 'r') as file:
        return float(file.readline())

