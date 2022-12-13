# Import the requests module
import requests

class KanyeQuote:
  """
  This class provides access to quotes from Kanye West.
  """

  def __init__(self):
    """
    Initialize the API endpoint for the Kanye.Rest API.
    """
      # Define the API endpoint  
    self.endpoint = "https://api.kanye.rest"

  def get_quote(self):
    """
    Get a random quote from Kanye West.

    Returns:
      str: A quote from Kanye West.
    """
      # Send a GET request to the API endpoint
    response = requests.get(self.endpoint)

        # Extract the quote from the response
    quote = response.json()['quote']

        # Return the quote
    return quote

  def print_quote(self):
    """
    Print a random quote from Kanye West.
    """
        # Get the quote
    quote = self.get_quote()

        # Print the quote
    print(quote)