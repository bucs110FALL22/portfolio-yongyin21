import random
list = (range(0,10 ))
randys = random.choice(list)
randys = int(randys)
print(randys)

for i in [randys]*3:
  guess = input("What is your guess?")
  guess = int(guess)
  if guess < randys:
    print("TOO LOW")
  if guess > randys: 
    print("WAY TOO HIGH")
  if guess == randys: 
    print("YOU GOT IT!")
    break
    