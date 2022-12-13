import requests

class BobBurgAtts:
  """
  This class provides access to attributes of Bob's Burgers characters from the Bob's Burgers API.
  """

  def __init__(self):
    """
    Initialize the base URL for the Bob's Burgers API.
    """
    self.base_url = "https://bobsburgers-api.herokuapp.com/characters/"
    

  def get_atts(self, character_id):
    """
    Get the attributes of a Bob's Burgers character with the given ID.
    
    Args:
      character_id (int): The ID of the character.

    Returns:
      dict: A dictionary containing the character's attributes.
    """
    # Make a request to the Bob's Burgers API to get the attributes of the character with the given ID
    response = requests.get(f"https://bobsburgers-api.herokuapp.com/characters/{character_id}")

    # Get the character's attributes
    bobattrs = response.json()

    # Return the character's attributes
    return bobattrs