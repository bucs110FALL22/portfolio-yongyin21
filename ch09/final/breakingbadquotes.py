import requests

class BreakingBadQuotes:
  def __init__(self):
    pass

  def get_quotes(self, character_id):
    # Make a request to the Breaking Bad API to get a list of quotes for the given character
    response = requests.get(f"https://api.breakingbadquotes.xyz/v1/quotes/{character_id}")

    # Get the list of quotes
    quotes = response.json()

    # Return the list of quotes
    return quotes