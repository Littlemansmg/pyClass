
print("Travel time Calculator")

distance = input("Enter miles: ")
mph = input("Enter miles per hour: ")

hours = int(distance) // int(mph)
minutes = int(distance) % int(mph)

print("\n Estimated travel time\n"
      "Hours: \t\t{}\n"
      "Minutes: \t{}".format(hours, minutes))
