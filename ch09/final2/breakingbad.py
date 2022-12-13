import requests

class BBAttributes:
  """
  This class provides access to attributes of Breaking Bad characters from the Breaking Bad API.
  """

  def __init__(self):
    """
    Initialize the base URL for the Breaking Bad API.
    """
    self.base_url = "https://www.breakingbadapi.com/api/"
    
  def get_character(self):
    """
    Get the attributes of a Breaking Bad character with the given name.
    
    Returns:
      dict: A dictionary containing the character's attributes.
    """
    # Make a request to the Breaking Bad API to get the attributes of the character with the given name
    url = self.base_url + "characters?name=" 
    response = requests.get(url)

     #Return the character's attributes
    return response.json()