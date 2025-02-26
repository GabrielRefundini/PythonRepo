# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list
# at least three times. Add code near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.
print("The Dali is out of pastrami!")
sandwich_orders = ['BLT', 'pastrami', 'Turkey', 'Veggie', 'pastrami', 'Ham and Cheese', 'Chicken', 'Tuna', 'pastrami']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f'I have made your {sandwich}')
    finished_sandwiches.append(sandwich)