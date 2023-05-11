number = int(input("Enter number of rows: "))

for column in range(1,number+1):
    for row in range(1, column+1):
        print(column, end=" ")
    print()