# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

toppings = []

while True:
   message = input("Enter one topping at a time but feel free to add as many as you want! When you have finish, type 'finish' ")
   if message == 'finish':
       break
   toppings.append(message)

print(f"The choosen Toppings are: {', '.join(toppings)}")