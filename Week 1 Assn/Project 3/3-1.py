
while 1:
    grade = input("Enter numerical grade: ")
    grade = int(grade)

    if grade >= 88:
        print("Letter grade: A")
    if 80 <= grade <= 87:
        print("Letter grade: B")
    if 67 <= grade <= 79:
        print("Letter grade: C")
    if 60 <= grade <= 66:
        print("Letter grade: D")
    if grade <= 60:
        print("Letter grade: F")

    iterate = input("Continue? (y/n): ")
    if iterate.lower() == "n":
        break

print("Bye!")
