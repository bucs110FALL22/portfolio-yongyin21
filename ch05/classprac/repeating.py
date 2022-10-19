def square(num):
  result = 0
  for i in range(num):
    result = result+num
  return result

def main():
  res = square(2)
  print(res)
  res = square(100)
  print(res)
  res = square(-1)
  print(res)

main()