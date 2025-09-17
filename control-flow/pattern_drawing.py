size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:        # while loop for rows
    for col in range(size):   # for loop for columns
        print("*", end="")
    print()   # move to next line after each row
    row += 1