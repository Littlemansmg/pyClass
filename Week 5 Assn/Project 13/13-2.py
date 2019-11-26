# created by Scott "LittlemanSMG" Goes on DD/MM/YYYY


def display_branch(branch):
    if branch == 0:
        pass
    else:
        display_branch(branch - 1)
        print("*****" * branch)
        display_branch(branch - 1)


def main():
    print("Tree Pattern")
    branches = 1
    while True:
        try:
            branches = int(input("Enter number of branches: "))
            if branches < 0:
                raise ValueError
        except ValueError:
            print("You need to enter a number.")
            continue
        break
    display_branch(branches)



if __name__ == "__main__":
    main()
