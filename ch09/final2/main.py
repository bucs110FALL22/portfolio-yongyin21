# imports
import time
from breakingbadquotes import BreakingBadQuotes
from bobsburgers import BobBurgAtts
from kanyewest import KanyeQuote

def main():
  # Create the instance
  bbq = BreakingBadQuotes()

  # Get the quotes for the selected character
  quotes = bbq.get_quotes(1)

  # Print the quotes for the selected character
  for quote in quotes:
    print(f"{quote['author']}: {quote['quote']}")
  
  name = f"{quote['author']}"

  # Split the name into two parts
  first_half, second_half = name.split(" ", 1)
  time.sleep(2)
  print("Well, this program was supposed to take a random Breaking Bad character from the Breaking Bad Quotes api and taking the author, and then printing attributes about the character from the Breaking Bad API but that decided not to work...")

  time.sleep(4)
  print("So now, we are going to have to make do with attributes from our favorite bob's burgers characters!")
  bba = BobBurgAtts()
 
  character_id = input("Pick a number from 1-500")
  url3 = bba.get_atts(character_id)
  # Extract the quote from the response
  bobquote = url3
  # Print the quote
  print(bobquote)
  time.sleep(3)
  kq = KanyeQuote()
  time.sleep(3)
  print("One last thing, I need you to choose a quote that you like the most")
  
  print ("Option 1:")
  kq.print_quote()


  time.sleep(3)
  print("Option 2: One of the key problems today is that politics is such a disgrace, good people don't go into government." )
  time.sleep(1.5)
  choice = input("Which quote do you like the most ? (Option 1 or Option 2)")
  if choice == "Option 1":
    print("CONGRATULATIONS YOU ARE AN OFFICIAL KANYE FAN WHOSE BREAKING BAD CHARACTER IS " + name)
  elif choice == "Option 2":
    print("You don't want to know whose quote this is, Ima just say your Breaking Bad character is "+ name)
  
  return

main()
