star_pyramid = int(input("Enter number of rows: "))

for i in range(star_pyramid):
    for x in range(i+1):
        print("* ", end="")
    print("")

rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for x in range(0, i):
        print("* ", end=" ")
    
    print("")