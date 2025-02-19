# Start with your program from Exercise 4-1 (page 56). 
pizzas = ['Portuguese','Parma','Shredded Beef']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print(f"Recently, I've been enjoying Parma pizza more than the others, specially the ones of Italian dough, but I also used to like Portuguese pizza a lot and Shredded Beef from some pizzeria.\n")
print("Who doesn't love pizza!?")

# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
friend_pizzas = pizzas[:]

# Add a new pizza to the original list.
pizzas.append('Pepperoni')

# Add a different pizza to the list friend_pizzas.
friend_pizzas.append('Margherita')

# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. 
print(f"My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
# Print the message My friend’s favorite pizzas are:, 
# and then use a for loop to print the second list. 
# Make sure each new pizza is stored in the appropriate list.
print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)