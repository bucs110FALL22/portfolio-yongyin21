import requests

class BreakingBadQuotes:
  """
  This class provides access to quotes from the Breaking Bad Quotes API.
  """

  def __init__(self):
    """
    Initialize the base URL for the Breaking Bad Quotes API.
    """
    pass

  def get_quotes(self, character_id):
    """
    Get a list of quotes for a given character.
    
    Args:
      character_id (int): The ID of the character.

    Returns:
      list: A list of dictionaries containing a and its author.
    """
    # Make a request to the Breaking Bad Quotes API to get a list of quotes for the given character
    response = requests.get(f"https://api.breakingbadquotes.xyz/v1/quotes/{character_id}")

    # Get the list of quotes
    quotes = response.json()

    # Return the list of quotes
    return quotes