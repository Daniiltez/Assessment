import requests
class Pokemon(object):
 
  def __init__(self, name, id1, weight, height):
    self.name = name
    self.id1 = id1
    self.height = height
    self.weight = weight


class BasePokemon(object):
 def __init__(self, name):
   self.name = name
  

result = requests.get("https://pokemondb.net/pokedex/all").json()


if __name__ == "__main__":
  print(result[hp])
