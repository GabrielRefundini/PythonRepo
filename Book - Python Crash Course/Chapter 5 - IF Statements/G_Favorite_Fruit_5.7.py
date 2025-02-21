# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain
# fruits in your list.

# Make a list of your three favorite fruits and call it favorite_fruits.
# Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!
fruits = ["apple", "banana", "orange", "grape", "strawberry", "watermelon", 
          "pineapple", "pear", "mango", "kiwi", "peach", "plum", "cherry", 
          "guava", "papaya", "fig", "persimmon", "cashew", "passion fruit"]
favorite_fruits = ["apple", "kiwi", "melon"]

for fruit in favorite_fruits:
    if fruit in fruits:
        print(f"You really like {fruit}!")

