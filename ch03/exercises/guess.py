import random
list = (range(0,11 ))
randys = random.choice(list)
randys = int(randys)
print(randys)
num_guesses = 0
for i in [randys]*10:
  guess = input("What is your guess?")
  guess = int(guess)
  num_guesses += 1
  if guess < randys:
    print("TOO LOW")
  if guess > randys: 
    print("WAY TOO HIGH")
  if guess == randys: 
    print("YOU GOT IT!")
    break
print("It took you", num_guesses, " guess(es) to get it right" )