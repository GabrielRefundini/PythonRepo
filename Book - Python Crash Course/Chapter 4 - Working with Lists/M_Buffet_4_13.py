# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
buffet_basic_foods = ('Rice','Beans','Eggs','Pasta','Potato')
# Use a for loop to print each food the restaurant offers.
for basic_food in buffet_basic_foods:
    print(basic_food)
# Try to modify one of the items, and make sure that Python rejects the change.

# buffet_basic_foods[1] = 'Cheese'

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, 
# and then use a for loop to print each of the items on the revised menu.
buffet_basic_foods = ('Rice','Beans','Fruits','Pasta','Meat')
for basic_food in buffet_basic_foods:
    print(basic_food)