#imports
import requests 
from breakingBadQuotes import BreakingBadQuotes
from breakingbad import BBAttributes

def main():
  # Create the instance
  bbq = BreakingBadQuotes()

  # Get the quotes for the selected character
  quotes = bbq.get_quotes(1)

  # Print the quotes for the selected character
  for quote in quotes:
    print(f"{quote['author']}: {quote['quote']}")
    print(f"{quote['author']}")
  name = f"{quote['author']}"

  # Split the name into two parts
  first_half, second_half = name.split(" ", 1)

  # Print the first half and second half of the name
  print(f"{first_half}")
  print(f"{second_half}")
  # Create an instance of the Breaking Bad API class
  character_name = f"{first_half}" + " + " + f"{second_half}"
  bb = BBAttributes()
  character_name = bb.get_character()

  # Get the details for the given character

  response2 = requests.get(character_name)
  print(response2)
   #Print the attributes of the character
  print(f"Name: {character_name['name']}")
  print(f"Occupation: {character_name['occupation']}")
  print(f"Image: {character_name['img']}")
  return

main()


  