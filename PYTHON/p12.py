class Pie:
  def _init_(self, flavor, ingredients):
    self.flavor = flavor
    self.ingredients = ingredients

  def print_ingredients(self):
    for i in self.ingredients:    
      print(i)

applePie = Pie('apple', ['flour', 'eggs', 'apples', 'butter'])

applePie.print_ingredients()

