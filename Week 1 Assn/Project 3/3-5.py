
print("Table of Powers")

while 1:
    start = input("Start Number: ")
    start = int(start)
    stop = input("Stop Number:  ")
    stop = int(stop)

    if start > stop:
        print("You need to start before you end. (Start must be lower than stop number.)")
        continue
    break

print("Number\tSquared\tCubed\n"
      "======\t=======\t=====")

for i in range(start, stop+1):
    print("{}\t\t{}\t{}".format(i, i**2, i**3))
