def multiply(arg1=0, arg2=0):
  accumulator = 0 
  for i in range(arg2):
    accumulator = accumulator + arg1

  return accumulator

def square(num):
  return multiply(num,num)

def main():
  result = multiply(arg1=5, arg2=7)
  print(result)

  result = multiply()
  print(result)

  result = multiply(arg1=5, arg2=7)
  print(result)

  result = exponent(arg1=2, arg2=3)
  print(result)

  result = multiply()
  print(result)

  

  