import requests

class BBAttributes:
  def __init__(self):
    self.base_url = "https://www.breakingbadapi.com/api/"
    
    
  def get_character(self):
    # request to the Breaking Bad api
    
    url = self.base_url + "characters?name=" 
    response = requests.get(url)

     #Return the character details
    return response.json()


#bb = BreakingBadAPI()

# Get the details for the given character
#character_name = f"{quote['author']}"
#character = bb.get_character(character_name)

# Print the attributes of the character
#print(f"Name: {character['name']}")
#print(f"Occupation: {character['occupation']}")
#print(f"Image: {character['img']}")