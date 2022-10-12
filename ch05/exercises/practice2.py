rows = int(input("Enter number of rows: "))

def star_pyramid():
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, rows):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("*", end="")
      
        # ending line after each row
        print("\r")

star_pyramid()