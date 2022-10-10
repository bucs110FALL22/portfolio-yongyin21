var = print("print")
print(var)
def my_funct():#defining the function always goes before the function
  print("statement")
  print("other statement")
my_funct()
print("done")
my_funct()

def findMin():
  print("Enter 3 numbers")
  num_a = int(input(":"))
  num_b = int(input(":"))
  num_c = int(input(":"))

  lowest = num_a

  if num_b < lowest:
      lowest = num_b

  if num_c < lowest:
    lowest = num_c
  if num_c < lowest:
    lowest = num_c
  print(lowest)

findMin()