# All versions of foods.py in this section have avoided using for loops when printing, to save space. 
# Choose a version of foods.py, and write two for loops to print each list of foods.
my_foods = ['pizza', 'falafel', 'carrot cake']
my_foods.append('Cheese Cake')

friend_foods = my_foods[:]
friend_foods.append('Lamen')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)